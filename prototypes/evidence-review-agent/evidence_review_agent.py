#!/usr/bin/env python3
"""
OpenLab Evidence Review Agent (Prototype v0.1)
S.A.T. Labs / OpenLab — Proof-of-Learning Framework

Reviews SYNTHETIC or DE-IDENTIFIED student evidence packages, maps them to the
Proof-of-Learning Rubric, flags missing evidence, and prepares a Teacher Review
Packet wrapped in an OLA Trust Envelope.

Core principle:
    AI assists. Humans govern. Evidence speaks. Communities validate.

This agent NEVER issues final grades or badge decisions. Every output is
stamped `pending_teacher_review` and logged for auditability.

Usage:
    python evidence_review_agent.py sample_evidence_package.json
    python evidence_review_agent.py sample_evidence_package.json --ai   # optional Claude-assisted feedback draft

Offline mode has ZERO dependencies (Python 3.9+ stdlib only).
AI mode requires:  pip install anthropic   and  ANTHROPIC_API_KEY env var.
"""

import argparse
import json
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Rubric definition — mirrors framework/proof-of-learning-rubric.md
# ---------------------------------------------------------------------------

RUBRIC_DIMENSIONS = ["claim", "evidence", "reasoning", "revision", "validation"]

LEVELS = {1: "beginning", 2: "approaching", 3: "meeting", 4: "exceeding"}

# Evidence types the framework recognizes, and which rubric dimensions each
# type primarily supports. (Simple, inspectable mapping — by design.)
EVIDENCE_TYPE_MAP = {
    "learning_claim":     ["claim"],
    "reflection":         ["claim", "reasoning", "revision"],
    "data_table":         ["evidence"],
    "prototype_photo":    ["evidence"],
    "code_artifact":      ["evidence"],
    "draft":              ["evidence", "revision"],
    "revision_notes":     ["revision"],
    "peer_feedback":      ["validation"],
    "teacher_validation": ["validation"],
    "presentation":       ["evidence", "reasoning"],
    "cer_explanation":    ["claim", "evidence", "reasoning"],
}

# Keywords that suggest reasoning / revision depth inside free-text evidence.
REASONING_SIGNALS = ["because", "so that", "which means", "explain", "compare",
                     "support", "shows that", "data", "conclude"]
REVISION_SIGNALS = ["next time", "improve", "changed", "revised", "iterate",
                    "failed", "tried again", "feedback", "would collect"]
AI_DISCLOSURE_SIGNALS = ["ai helped", "i used ai", "chatgpt", "claude",
                         "ai suggested", "i chose", "i decided", "myself"]


# ---------------------------------------------------------------------------
# Core review logic (rule-based, fully offline, fully inspectable)
# ---------------------------------------------------------------------------

def load_package(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        pkg = json.load(f)
    for key in ("project_id", "mission", "learner_id", "evidence_items"):
        if key not in pkg:
            sys.exit(f"[error] evidence package missing required field: '{key}'")
    return pkg


def collect_text(pkg: dict) -> str:
    """All free-text content in the package, lowercased, for signal scanning."""
    chunks = [item.get("content", "") for item in pkg["evidence_items"]]
    chunks.append(pkg.get("ai_use_disclosure_text", ""))
    return " ".join(chunks).lower()


def score_dimensions(pkg: dict) -> dict:
    """Suggest (not decide) a rubric level per dimension based on evidence
    coverage and text signals. Levels are capped at 3 ('meeting') — level 4
    ('exceeding') is reserved for human judgment only."""
    provided_types = {i["type"] for i in pkg["evidence_items"]
                      if i.get("status", "provided") == "provided"}
    text = collect_text(pkg)

    coverage = {dim: 0 for dim in RUBRIC_DIMENSIONS}
    for etype in provided_types:
        for dim in EVIDENCE_TYPE_MAP.get(etype, []):
            coverage[dim] += 1

    suggested = {}
    for dim in RUBRIC_DIMENSIONS:
        hits = coverage[dim]
        level = 1 if hits == 0 else 2 if hits == 1 else 3

        # Text-signal boosts (still capped at 3)
        if dim == "reasoning" and sum(s in text for s in REASONING_SIGNALS) >= 2:
            level = max(level, 3 if hits else 2)
        if dim == "revision" and any(s in text for s in REVISION_SIGNALS):
            level = max(level, 2 if hits == 0 else 3)

        suggested[dim] = {
            "suggested_level": level,
            "label": LEVELS[level],
            "supporting_items": sorted(
                t for t in provided_types if dim in EVIDENCE_TYPE_MAP.get(t, [])
            ),
            "note": "Suggested by agent from evidence coverage. Teacher decides final level, including any 'exceeding' rating.",
        }
    return suggested


def flag_missing(pkg: dict, scores: dict) -> list:
    """Identify evidence gaps a teacher may want the learner to fill."""
    provided = {i["type"] for i in pkg["evidence_items"]
                if i.get("status", "provided") == "provided"}
    explicitly_missing = [i["type"] for i in pkg["evidence_items"]
                          if i.get("status") == "missing"]
    gaps = list(explicitly_missing)

    if scores["validation"]["suggested_level"] == 1 and not any(
            "validation" in g for g in gaps):
        gaps.append("teacher_or_peer_validation")
    if scores["revision"]["suggested_level"] == 1:
        gaps.append("revision_notes")
    if "learning_claim" not in provided and scores["claim"]["suggested_level"] < 3:
        gaps.append("explicit_learning_claim")
    if not pkg.get("ai_use_disclosure_text") and pkg.get("ai_use_disclosure") != "provided":
        gaps.append("ai_use_disclosure")

    # de-duplicate, preserve order
    seen, out = set(), []
    for g in gaps:
        if g not in seen:
            seen.add(g)
            out.append(g)
    return out


def check_ai_transparency(pkg: dict) -> dict:
    text = (pkg.get("ai_use_disclosure_text") or "").lower()
    signals = sum(s in text for s in AI_DISCLOSURE_SIGNALS)
    if not text:
        status = "missing"
    elif signals >= 2:
        status = "clear — learner explains both AI's role and their own decisions"
    else:
        status = "present but thin — consider asking learner to explain what THEY decided"
    return {"status": status, "disclosure_text": pkg.get("ai_use_disclosure_text", "")}


def draft_feedback_offline(pkg: dict, scores: dict, gaps: list) -> str:
    """Growth-language feedback draft. Rule-based; teacher edits before use."""
    strong = [d for d in RUBRIC_DIMENSIONS if scores[d]["suggested_level"] >= 3]
    growing = [d for d in RUBRIC_DIMENSIONS if scores[d]["suggested_level"] == 2]
    lines = [f"Great work on the '{pkg['mission']}' mission!"]
    if strong:
        lines.append(f"Your {', '.join(strong)} evidence stands out — it clearly shows your thinking.")
    if growing:
        lines.append(f"Your next growth step is strengthening {', '.join(growing)}.")
    if gaps:
        friendly = ", ".join(g.replace("_", " ") for g in gaps[:3])
        lines.append(f"Before validation, please add: {friendly}.")
    lines.append("Keep building — your learning trail is what makes this real.")
    return " ".join(lines)


def draft_feedback_ai(pkg: dict, scores: dict, gaps: list) -> str:
    """Optional Claude-assisted feedback draft. Teacher always edits/approves."""
    try:
        import anthropic
    except ImportError:
        return "[ai mode unavailable — run: pip install anthropic]  " + \
               draft_feedback_offline(pkg, scores, gaps)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return "[ai mode unavailable — set ANTHROPIC_API_KEY]  " + \
               draft_feedback_offline(pkg, scores, gaps)

    client = anthropic.Anthropic()
    summary = {d: scores[d]["label"] for d in RUBRIC_DIMENSIONS}
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        system=("You are OpenLab's warm, growth-oriented teacher assistant. "
                "Draft 2-4 sentences of feedback for a K-8 learner using growth "
                "language, never deficit language. Never assign grades or final "
                "decisions. The teacher will edit and approve before sending."),
        messages=[{"role": "user", "content":
                   f"Mission: {pkg['mission']}\n"
                   f"Suggested rubric levels: {json.dumps(summary)}\n"
                   f"Evidence gaps: {', '.join(gaps) or 'none'}\n"
                   f"Learner reflection excerpt: {collect_text(pkg)[:500]}\n\n"
                   "Draft the feedback now."}],
    )
    return msg.content[0].text.strip()


# ---------------------------------------------------------------------------
# OLA Trust Envelope + audit log + teacher packet
# ---------------------------------------------------------------------------

def build_trust_envelope(pkg: dict, mode: str) -> dict:
    return {
        "trust_envelope_id": f"OLA-TE-{uuid.uuid4().hex[:8]}",
        "mission_id": pkg["project_id"],
        "agent_name": "Evidence Review Agent v0.1",
        "action_type": "teacher_review_packet",
        "risk_level": "medium",
        "mode": mode,
        "data_class": "synthetic_or_deidentified_only",
        "approval_required": True,
        "approval_status": "pending_teacher_review",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def render_packet_md(pkg, scores, gaps, transparency, feedback, envelope) -> str:
    md = [
        f"# Teacher Review Packet — {pkg['mission']}",
        "",
        f"**Learner:** {pkg['learner_id']} (synthetic/de-identified)  ",
        f"**Project:** {pkg['project_id']}  ",
        f"**Status:** ⏳ PENDING TEACHER REVIEW — the agent suggests; you decide.",
        "",
        "## Suggested Rubric Alignment (agent suggestions, capped at 'meeting')",
        "",
        "| Dimension | Suggested Level | Supporting Evidence |",
        "|---|---|---|",
    ]
    for d in RUBRIC_DIMENSIONS:
        s = scores[d]
        items = ", ".join(s["supporting_items"]) or "—"
        md.append(f"| {d.title()} | {s['suggested_level']} — {s['label']} | {items} |")
    md += [
        "",
        "> Level 4 ('exceeding') is reserved for human judgment and is never suggested by the agent.",
        "",
        "## Missing / Requested Evidence",
        "",
    ]
    md += [f"- {g.replace('_', ' ')}" for g in gaps] if gaps else ["- None flagged."]
    md += [
        "",
        "## AI Transparency Check",
        "",
        f"- **Status:** {transparency['status']}",
        f"- **Learner disclosure:** \"{transparency['disclosure_text']}\"" if transparency["disclosure_text"] else "- **Learner disclosure:** (none provided)",
        "",
        "## Draft Feedback (edit before sending — growth language)",
        "",
        f"> {feedback}",
        "",
        "## Teacher Decision (complete by hand)",
        "",
        "- [ ] Approve badge recommendation",
        "- [ ] Request additional evidence",
        "- [ ] Revise rubric levels: ______",
        "- [ ] Notes: ______",
        "",
        "---",
        "",
        "### OLA Trust Envelope",
        "",
        "```json",
        json.dumps(envelope, indent=2),
        "```",
    ]
    return "\n".join(md)


def append_audit_log(out_dir: Path, envelope: dict, pkg: dict):
    log = out_dir / "audit-log.jsonl"
    entry = {**envelope, "learner_id": pkg["learner_id"],
             "evidence_item_count": len(pkg["evidence_items"])}
    with open(log, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="OpenLab Evidence Review Agent v0.1")
    ap.add_argument("package", help="Path to evidence package JSON (synthetic/de-identified only)")
    ap.add_argument("--ai", action="store_true", help="Use Claude to draft feedback (optional)")
    ap.add_argument("--out", default="review_output", help="Output directory")
    args = ap.parse_args()

    pkg = load_package(Path(args.package))
    mode = "ai_assisted" if args.ai else "offline_rule_based"

    scores = score_dimensions(pkg)
    gaps = flag_missing(pkg, scores)
    transparency = check_ai_transparency(pkg)
    feedback = draft_feedback_ai(pkg, scores, gaps) if args.ai \
        else draft_feedback_offline(pkg, scores, gaps)
    envelope = build_trust_envelope(pkg, mode)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    packet_md = render_packet_md(pkg, scores, gaps, transparency, feedback, envelope)
    packet_path = out_dir / f"review-packet-{pkg['project_id']}.md"
    packet_path.write_text(packet_md, encoding="utf-8")

    machine = {
        "trust_envelope": envelope,
        "rubric_alignment": {d: scores[d]["label"] for d in RUBRIC_DIMENSIONS},
        "missing_evidence": gaps,
        "ai_transparency": transparency["status"],
        "recommendation": "teacher review needed",
    }
    json_path = out_dir / f"review-{pkg['project_id']}.json"
    json_path.write_text(json.dumps(machine, indent=2), encoding="utf-8")

    append_audit_log(out_dir, envelope, pkg)

    print(f"✔ Teacher review packet: {packet_path}")
    print(f"✔ Machine-readable output: {json_path}")
    print(f"✔ Audit log updated: {out_dir / 'audit-log.jsonl'}")
    print(f"  Mode: {mode} | Status: pending_teacher_review")


if __name__ == "__main__":
    main()

# OpenLab Evidence Review Agent — Prototype v0.1

**S.A.T. Labs / OpenLab · Proof-of-Learning Framework**

> AI assists. Humans govern. Evidence speaks. Communities validate.

A working prototype that reviews **synthetic or de-identified** student evidence packages, maps them to the OpenLab Proof-of-Learning Rubric, flags missing evidence, checks AI-use transparency, and prepares a **Teacher Review Packet** — wrapped in an OLA Trust Envelope and logged for auditability.

The agent **never issues grades or badge decisions.** Every output is stamped `pending_teacher_review`. Rubric suggestions are capped at level 3 ("meeting"); level 4 ("exceeding") is reserved for human judgment only.

## Quick start (zero dependencies)

```bash
python3 evidence_review_agent.py sample_evidence_package.json
```

Outputs to `review_output/`:

| File | Purpose |
|---|---|
| `review-packet-<id>.md` | Human-readable teacher review packet with rubric table, gaps, draft feedback, and decision checklist |
| `review-<id>.json` | Machine-readable summary (matches `schema.json`) |
| `audit-log.jsonl` | Append-only audit trail of every agent action (OLA requirement) |

## Optional: AI-assisted feedback drafts

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your-key
python3 evidence_review_agent.py sample_evidence_package.json --ai
```

In `--ai` mode, Claude drafts a warmer feedback note using growth language. The teacher **always edits and approves** before anything reaches a learner. If the key or library is missing, the agent gracefully falls back to offline mode.

## How it works

1. **Load** an evidence package JSON (mission, learner ID, evidence items, AI-use disclosure).
2. **Map** each evidence type to the rubric dimensions it supports (claim, evidence, reasoning, revision, validation) — a simple, fully inspectable mapping table, no black box.
3. **Scan** free-text evidence for reasoning and revision signals.
4. **Flag** missing evidence a teacher may want the learner to add.
5. **Check** AI-use transparency: did the learner explain what AI did *and* what they decided themselves?
6. **Draft** growth-language feedback (rule-based, or Claude-assisted with `--ai`).
7. **Wrap** everything in an OLA Trust Envelope and append to the audit log.

## Governance boundaries

This prototype follows the OpenLab governance docs (`governance/`):

- Synthetic or de-identified data **only** — never real student PII
- No final grades, no automated badge decisions, no high-stakes automation
- Human approval gate on every output
- Append-only audit log for every agent action
- Explainable by design: the rubric mapping is a readable table in the source

## Evidence package format

See `sample_evidence_package.json`. Required fields: `project_id`, `mission`, `learner_id`, `evidence_items` (each with `type` and `status`). Recognized evidence types: `learning_claim`, `reflection`, `data_table`, `prototype_photo`, `code_artifact`, `draft`, `revision_notes`, `peer_feedback`, `teacher_validation`, `presentation`, `cer_explanation`.

## Roadmap

- v0.2 — batch mode (review a whole class folder of packages)
- v0.3 — Human-AI Collaboration Rubric as a second scoring lens
- v0.4 — badge metadata generation using `badges/badge-metadata-schema.json`
- v0.5 — teacher web UI (connects to the OpenLab School Demo)

---

Part of the [OpenLab Agentic Education](../..) research framework · Roger Vargas, S.A.T. Labs / OpenLab

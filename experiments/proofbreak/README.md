# 🎮 ProofBreak — Can You Fool the Proof?

> **Future Collaboration Mission / Research Challenge**

**Status:** Proposed — intentionally not implementation-ready  
**Project:** OpenLab Agentic Education  
**Target:** Proof-of-Learning Rubric (PoLR)  
**Safety mode:** Synthetic evidence only  
**Discussion:** [Issue #4](../../issues/4)

## Mission

Do not try to prove that PoLR works.

**Try to break it.**

ProofBreak is an adversarial, game-like research mission for educators, learners, researchers, accessibility advocates, designers, and AI builders. Participants attempt to make a Proof-of-Learning system support learning that did not occur — or fail to recognize learning that did.

> **Under what conditions does PoLR fail to distinguish credible evidence of learning from evidence that merely looks credible?**

Failure discovery is progress.

---

## 🔨 Attack Deck

- 🎭 **The Perfect Fake** — beautiful evidence for learning that never occurred.
- 🤖 **AI Ghost Student** — AI does most of the work while the portfolio appears learner-owned.
- 🧠 **Different Brain** — genuine learning appears in a modality the rubric handles poorly.
- 😈 **Rubric Gamer** — obtain `SUPPORTED` with the smallest amount of actual understanding possible.
- 👥 **Group Parasite** — hide individual uncertainty inside excellent collaborative work.
- ✨ **Polish Trap** — make weak understanding look strong through presentation quality.
- 🗣 **Invisible Expert** — deep understanding with weak conventional evidence production.
- 🧑‍🏫 **30-Kid Meltdown** — rigorous validation that becomes impossible at classroom scale.
- 🕵 **Surveillance Creep** — keep requesting useful-looking evidence until proof becomes monitoring.
- 🏆 **Hierarchy Attack** — test whether `SUPPORTED_WITH_EXTENSION` becomes the new A+.

---

## ⚔️ Agent Arena

### RED — Proof Hacker
Receives a mission, PoLR, and synthetic learner history. Attempts to construct the smallest Evidence Set capable of receiving `SUPPORTED` despite a hidden weakness in the claimed understanding.

### BLUE — Evidence Reviewer
Receives only the Learning Claim, Evidence Set, and PoLR. It may return `NOT_YET_REVIEWABLE`, `MORE_EVIDENCE_NEEDED`, `SUPPORTED`, or `SUPPORTED_WITH_EXTENSION`, while exposing missing evidence, contradictions, questions, and uncertainty.

Blue does **not** receive hidden ground truth.

### ⚖️ ORACLE — Synthetic Ground Truth
The experiment retains a controlled synthetic record of what actually occurred so researchers can identify disagreement between evidence review and the known experimental condition.

**The Oracle is an experimental mechanism, not a model of real-world omniscience. Real learners do not come with ground-truth labels.**

---

## ☠️ Critical failure classes

### False Proof

```text
Weak / unsupported understanding
        ↓
      PoLR
        ↓
   SUPPORTED ❌
```

### Invisible Learning

```text
Credible understanding
        ↓
      PoLR
        ↓
MORE_EVIDENCE_NEEDED ❌
```

Both matter. Invisible Learning is especially important when testing accessibility, multilingual evidence, neurodivergent learners, and learning demonstrated through making, speaking, movement, performance, or interaction.

---

## 📉 Minimum Sufficient Evidence (MSE)

ProofBreak explores a candidate OpenLab principle:

> **Collect the minimum sufficient evidence needed to make a defensible claim — then stop collecting.**

More data is not automatically better evidence.

A future game may expose competing costs:

```text
Teacher Time       █████░░░
Student Burden     ███░░░░░
Privacy Cost       ██░░░░░░
Evidence Strength  ██████░░
```

The objective is:

> **The strongest defensible learning claim with the least intrusive evidence.**

---

## 👹 Boss Levels

1. **AI Kid** — AI generated most of the artifact, but the learner genuinely understands it. Does PoLR examine understanding or punish tool use?
2. **Brilliant Nonwriter** — the learner struggles with written reflection but convincingly demonstrates the concept another way.
3. **Beautiful Fraud** — perfect artifact, portfolio, and reflection; the learner cannot explain why key decisions were made.
4. **Teacher Knows** — submitted evidence is ambiguous, but sustained professional observation indicates genuine reasoning and revision.
5. **The Group** — extraordinary collaborative work obscures what each learner can claim individually.
6. **Final Boss: MIRA** — MIRA helps the learner reflect and organize so effectively that it changes the evidence-generating process itself.

Final-boss questions:

> **Are we examining the learner's capability, the learner + AI system, or both?**

> **Can MIRA strengthen reflection without manufacturing the evidence it later helps review?**

---

## 🧪 Proposed progression

### ProofBreak 0.1 — Human Hackathon
10–20 synthetic cases. Humans attack PoLR.

### ProofBreak 0.2 — Agent Arena
Red agents generate adversarial Evidence Sets; Blue reviews them; the Oracle records synthetic ground truth.

### ProofBreak 0.3 — Human × Agent
Educators and AI independently review the same synthetic cases. Study disagreements rather than assuming either side is correct.

### ProofBreak 0.4 — MIRA
Test whether reflection assistance improves learner explanation and agency without manufacturing proof.

### ProofBreak 1.0 — Classroom-safe research pilot
Only after governance, accessibility, privacy, consent, and appropriate institutional/school review.

---

## 🧱 Future structure

```text
experiments/
└── proofbreak/
    ├── README.md
    ├── RULES.md
    ├── attack-cards/
    ├── synthetic-learners/
    ├── missions/
    ├── red-agent/
    ├── blue-agent/
    ├── oracle/
    └── results/
```

Compute may eventually include local/open models or research cloud infrastructure such as Lambda. The experiment should remain model-agnostic rather than becoming a benchmark for one vendor.

---

## 🛡 Non-negotiable safety rules

1. Synthetic evidence first.
2. No real student data in the public repository.
3. No ranking real children.
4. No psychological, disability, motivation, intelligence, or emotion inference from learner artifacts.
5. **AI REVIEW ≠ HUMAN VALIDATION.**
6. Adversarial testing must not become a recipe for deceiving actual schools or assessment systems.
7. Accessibility failures count as system failures, not learner failures.
8. Record uncertainty rather than hiding it behind confidence scores.

---

## 🏁 What winning means

There is no prize for making PoLR look robust.

A successful round produces a reproducible failure, unresolved ambiguity, accessibility problem, excessive workload requirement, privacy problem, false-positive/false-negative claim, proposed guardrail, or better research question.

> # **If you break the proof, you improve the proof.**

## Collaboration invitation

Future collaborators are invited to challenge assumptions, design synthetic attack cases, propose accessibility tests, build game mechanics, create adversarial agents, and help define responsible evaluation methods.

The purpose is not to automate judgment.

**It is to discover where our evidence and governance fail before those failures reach learners.**
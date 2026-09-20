# OpenLab Vocabulary & Terminology v0.1

**Status:** Review draft  
**Scope:** Agentic Education / OpenLab / S.A.T. / Proof-of-Learning

Language shapes architecture. This file defines the canonical vocabulary for OpenLab so the project does not accidentally become the thing it is trying to avoid: a token economy, an automated grading system, or a surveillance layer wearing an AI label.

> **Evidence is collected. Claims are examined. AI assists review. Humans validate. Trust is earned. Recognition follows.**

## Generative and agentic distinction

OpenLab distinguishes **generative capability**, **agentic capability**, and **Agentic Education**.

| Term | Working meaning |
|---|---|
| **Generative AI** | Systems used to generate or transform content such as text, images, code, explanations, questions, simulations, or feedback. |
| **Agentic AI** | Systems that can pursue goals and take actions with some degree of autonomy within defined tools, context, permissions, and governance boundaries. |
| **Generative Education** | A useful descriptive frame for educational practice in which generative systems support creation, explanation, feedback, simulation, and other learning activities. It is not currently OpenLab's canonical framework name. |
| **Agentic Education** | The OpenLab educational and research framework centered on learner agency, meaningful action, evidence of learning, reflection, human validation, human-AI collaboration, and human governance. |

Generative AI can operate **inside** Agentic Education. A companion may generate a question, a reflection prompt, an explanation, or a summary of evidence. Generation, however, is not itself the learning loop.

OpenLab's working distinction is:

> **Generative AI makes things. Agentic AI can pursue goals and take actions. Agentic Education designs the learning system so that increased machine agency strengthens rather than replaces human agency.**

This creates a design test for new technologies and capabilities:

> **Does this increase meaningful learner agency, strengthen credible proof-of-learning, or improve learner-controlled trust?**

A technology should not become part of the canonical architecture merely because it is novel or technically possible.

## Core terms

| Term | Canonical meaning |
|---|---|
| **OpenLab** | The learning ecosystem connecting authentic missions, evidence, reflection, human validation, recognition, and learner pathways. |
| **Agentic Education** | The educational and research framework centered on learner agency, human-AI collaboration, evidence of learning, and human governance. |
| **S.A.T.** | **Skills, Agency & Trust.** The trust/proof layer connecting demonstrated skills, learner agency, evidence provenance, validation, and recognition. |
| **Proof-of-Learning (PoL)** | A structured, inspectable argument that a learning claim is supported by evidence, reasoning, reflection, iteration, and appropriate human validation. |
| **Proof-of-Learning Rubric (PoLR)** | The rubric/protocol used to examine whether an Evidence Set supports a Learning Claim. |
| **STEER** | Governance loop: Specify → Target evidence → Establish quality bar → Evaluate with humans → Review/refine. |

## Evidence language

| Term | Canonical meaning |
|---|---|
| **Learning Claim** | A learner-authored or learner-confirmed statement of what the learner claims to understand, explain, create, investigate, or do. |
| **Evidence Set** | Artifacts, observations, demonstrations, data, revisions, reflections, and other material offered in support of a Learning Claim. |
| **Evidence Review** | Examination of an Evidence Set. AI may assist; review is not validation. |
| **Human Validation** | An authorized human judgment describing what the available evidence supports, does not support, or leaves uncertain. |
| **Learning Proof** | A validated, inspectable record linking a Learning Claim to evidence, reasoning, provenance, uncertainty, and validation. |
| **Trust Envelope** | Governance/provenance wrapper around a Learning Proof: evidence references, provenance, permissions, AI involvement, criteria, human validation, uncertainty, and lifecycle metadata. |
| **Recognition** | Badge, credential, acknowledgment, unlock, or other downstream representation of validated learning. Recognition is not the evidence itself. |
| **Learning Portfolio** | A learner-centered collection of Learning Proofs, artifacts, reflections, and pathways. |

## Agent language

### MIRA — Meaningful Intelligence for Reflection and Agency

MIRA is the proposed learner-facing OpenLab companion and orchestration interface. Its purpose is not to judge the learner. Its purpose is to help the learner **notice, question, connect, reflect, and act**.

MIRA may coordinate mission context, reflection, evidence organization, questions, agent handoffs, and learner-facing explanations. MIRA must never become an autonomous evaluator, hidden authority, behavioral surveillance system, or high-stakes decision-maker.

### Mr. V Orchestrator

Mr. V is retained as an **experimental orchestration prototype**, not the canonical learner-facing identity of OpenLab.

This distinction is intentional: MIRA represents the pedagogical relationship; orchestration is an implementation detail. Mr. V can remain a useful architecture experiment behind the orchestration layer while the system evolves.

```text
Learner / Educator
        ↓
       MIRA
Reflection + Agency Interface
        ↓
OpenLab Orchestration Layer
        ↓
Specialized Agents / Tools
        ↓
AI-assisted Evidence Review
        ↓
HUMAN VALIDATION GATE
        ↓
Learning Proof → Recognition → Learning Portfolio
```

### Evidence Review Agent

Canonical name for AI functionality previously described as a **Validator Agent**. It may inspect rubric structure, surface missing or contradictory evidence, generate questions, summarize evidence, and identify uncertainty. It cannot issue final validation.

### Portfolio Curator Agent

Organizes evidence and Learning Proofs into learner-centered portfolio structures. It does not determine whether learning occurred.

### Reflection Coach

Prompts reflection and metacognition without scoring reflection or inferring hidden learner traits.

## Canonical replacements

| Deprecated / ambiguous | Use instead |
|---|---|
| Smart Academic Token | **Skills, Agency & Trust (S.A.T.)** |
| Smart Academic Trust | **Skills, Agency & Trust (S.A.T.)** |
| SAT token / academic token | **Learning Proof** or **Recognition**, depending on meaning |
| token validation | **Evidence Review** / **Human Validation** |
| wallet | **Learning Portfolio** unless an actual technical wallet is meant |
| mint / minting | **issue**, **recognize**, or **publish** |
| token holder | **learner** |
| Validator Agent | **Evidence Review Agent** |
| AI validation | **AI-assisted Evidence Review** |
| proof score | **evidence state** / **validation state** |
| student profile | **Learning Portfolio** when referring to the evidence record |

## Terms allowed in safety statements

Do not mechanically replace every occurrence of *token*, *wallet*, *score*, or *surveillance*. These words remain appropriate when explicitly documenting what OpenLab rejects—for example: **OpenLab does not issue financialized learning tokens to children.**

## Architecture invariants

> **AI REVIEW ≠ HUMAN VALIDATION**

> **A polished artifact is not proof of learning.**

> **Recognition follows evidence; it does not manufacture evidence.**

> **A learner is not a score, profile, token holder, or prediction.**

> **Proof-of-Learning is not a score assigned to a learner. It is a transparent argument supported by evidence that people can examine, question, validate, and revise.**

## Version note

**v0.1** establishes the initial vocabulary. It should evolve through educator, learner, family, accessibility, research, and community critique alongside PoLR and classroom testing.

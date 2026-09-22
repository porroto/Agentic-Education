# AGENTS.md — OpenLab Agentic Education

This file provides operating guidance for AI coding and research agents working in this repository.

OpenLab Agentic Education is a research and prototype framework for human-governed, evidence-centered learning.

## North Star

> AI assists. Humans govern. Evidence speaks. Communities validate.

The purpose of this repository is not to automate judgment about learners.

The purpose is to explore how learners, educators, families, communities, institutions, and AI systems can create, examine, reflect on, and validate learning evidence while preserving human agency.

When intelligence becomes abundant, human agency becomes the curriculum.

## Read Before Making Changes

Before substantial work, read the documents relevant to the task.

Start with:

1. `README.md` — repository overview and current architecture
2. `VISION.md` — mission and protected values
3. `MANIFESTO.md` — principles that should not be casually compromised
4. `docs/TERMINOLOGY.md` — canonical project vocabulary
5. `ROADMAP.md` — current development sequence
6. `CONTRIBUTING.md` — contribution expectations

For learning-evidence work, also inspect:

- `framework/`
- `governance/`
- `missions/`

For agent work, inspect:

- `agents/README.md`
- the relevant specification under `agents/`

Do not silently redefine established terminology.

## Repository Architecture

The project currently moves through three connected layers:

```text
RESEARCH
papers/
proposals/
docs/

    ↓

FRAMEWORK
framework/
governance/
missions/

    ↓

PROTOTYPE
agents/
badges/
prototypes/
data/
```

Human governance applies across all three layers.

Do not introduce a new top-level architecture merely because it is convenient for one experiment. Prefer extending the existing structure unless a documented architectural change justifies otherwise.

## Core Invariants

### Human Validation Is Final

AI may:

- organize evidence
- summarize evidence
- identify missing evidence
- ask questions
- surface contradictions
- support reflection
- suggest interpretations
- communicate uncertainty

AI must not become the final authority declaring that a learner has demonstrated mastery.

Preserve:

```text
AI REVIEW ≠ HUMAN VALIDATION
```

### Evidence Before Recognition

Badges, credentials, unlocks, portfolio artifacts, or other recognition should follow validated learning evidence.

Recognition is not itself evidence.

### Preserve Learner Agency

Learners should be able to:

- understand what evidence is being considered
- explain their process
- reflect and revise
- question AI suggestions
- challenge incorrect interpretations
- participate in how their learning is represented

Do not design systems where an opaque model silently defines the learner.

### Minimum Necessary Evidence

More learner data is not automatically better evidence.

Prefer the minimum information necessary to support the Learning Claim.

### No Hidden Profiling

Do not introduce hidden behavioral, biometric, emotional, psychological, or personality profiling.

Do not infer sensitive learner characteristics merely because sensors or models make such inference technically possible.

### Synthetic Data by Default

This public repository uses synthetic and appropriately de-identified examples.

Do not add real student records, identifying learner data, private classroom artifacts, credentials, secrets, or access tokens.

## Canonical Learning Flow

Preserve the conceptual distinction between these stages:

```text
Mission
   ↓
Learning Claim
   ↓
Evidence
   ↓
Reflection / Iteration
   ↓
AI-assisted Evidence Review
   ↓
HUMAN VALIDATION GATE
   ↓
Learning Proof
   ↓
Recognition / Portfolio / Next Pathway
```

Agents may assist multiple stages, but assistance does not collapse these stages into one automated judgment.

## MIRA

MIRA means:

**Meaningful Intelligence for Reflection and Agency**

MIRA is a learner-facing companion concept.

MIRA may help learners:

- reflect
- notice patterns
- organize evidence
- explore questions
- navigate missions
- understand possible next steps

MIRA should not become an autonomous evaluator of the learner.

Before modifying MIRA concepts or implementations, read:

`agents/mira.md`

## Experimental Hardware and Embodied AI

OpenLab may explore Companion hardware, sensors, robotics, physical AI, simulation, NFC interactions, environmental sensing, computer vision, or biological/connectome-inspired controllers.

These are experimental extensions of the learning architecture.

When working on such experiments:

- preserve the human-governance model
- prefer simulation before committing to new physical hardware
- separate experimental cognition from safety-critical control
- do not convert sensing into surveillance
- use deliberate evidence-capture interactions rather than continuous observation where practical
- document what is experimental versus established
- avoid making one experimental platform the identity of the entire project

For robotics, high-level experimental intelligence should generally select intentions or behaviors while proven lower-level systems retain responsibility for safe actuation.

## Hardware Design Principle

Prefer modular capability over unnecessary core complexity.

A learner-facing Companion should remain as practical as possible:

- affordable
- durable
- responsive
- emotionally expressive
- privacy-conscious
- modular
- useful without requiring continuous cloud connectivity

When heavier computation is needed, consider delegation to appropriate edge, educator, laboratory, or cloud systems rather than automatically increasing the requirements of every learner device.

## Experiments

Experimental work should make its status obvious.

Where practical, document:

- question or hypothesis
- architecture
- assumptions
- simulation or test environment
- evidence collected
- limitations
- safety/privacy considerations
- result
- next decision

A successful experiment may inform the framework.

An interesting experiment does not automatically become product architecture.

## Documentation Discipline

Prefer repository documentation over assumptions carried only in conversations.

When an important architectural decision becomes stable, document it.

When implementation and documentation disagree, investigate rather than silently choosing whichever is easier.

Do not erase historical context simply because a concept evolved. Deprecate or supersede clearly when appropriate.

## Agent Behavior

When working in this repository:

1. Inspect before modifying.
2. Preserve canonical terminology.
3. Make the smallest coherent change.
4. Separate evidence from inference.
5. State uncertainty.
6. Do not fabricate research findings, citations, learner evidence, test results, or hardware capabilities.
7. Do not claim a prototype works unless it has actually been tested.
8. Prefer reversible experiments.
9. Preserve human governance boundaries.
10. Leave the repository easier for the next human or agent to understand.

## Definition of Success

A technically impressive contribution is not sufficient.

A successful contribution should strengthen at least one of:

- learner agency
- quality or inspectability of evidence
- human judgment
- reflection
- accessibility
- privacy
- provenance
- trust
- responsible experimentation

without quietly weakening the others.

The system should make learning more human-visible without surrendering human agency.

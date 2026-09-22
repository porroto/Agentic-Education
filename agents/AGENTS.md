# AGENTS.md — OpenLab Agent Specifications

This directory contains specifications and experiments for AI agents operating within the OpenLab Agentic Education framework.

The instructions in the repository root `AGENTS.md` continue to apply here.

## Primary Boundary

> AI REVIEW ≠ HUMAN VALIDATION

No agent defined in this directory should silently cross the Human Validation Gate.

Agents may support human judgment.

They do not replace it.

## Existing Roles

Before creating a new agent, inspect the existing specifications.

Important current roles include:

- `mira.md` — learner-facing reflection and agency companion
- `evidence-review-agent.md` — AI-assisted examination of learning evidence
- `reflection-coach-agent.md` — reflection support
- `portfolio-curator-agent.md` — portfolio organization
- `mr-v-orchestrator.md` — orchestration experiment

Some older specifications may represent deprecated terminology or earlier architecture.

Check repository documentation before treating an older file as canonical.

## Before Creating Another Agent

Ask whether the capability actually requires a new autonomous role.

Prefer:

```text
existing agent + new tool/capability
```

over:

```text
new agent for every feature
```

when responsibilities naturally belong to an existing role.

Create a distinct agent only when the responsibility, authority boundary, interaction model, or safety requirements are meaningfully different.

## Agent Specification Template

New agent specifications should make these elements explicit when applicable:

### Purpose

What learning or orchestration problem does the agent address?

### Human Relationship

Who is the agent serving?

Examples:

- learner
- educator
- human validator
- researcher
- administrator
- another agent

### Inputs

What information may the agent receive?

### Outputs

What may it produce?

### Allowed Actions

What is the agent permitted to do?

### Forbidden Actions

What must it never do?

### Human Gate

Which actions or conclusions require human judgment or approval?

### Uncertainty

How should uncertainty, contradiction, or missing information be represented?

### Data Boundary

What learner information is actually necessary?

### Failure Modes

How could this agent accidentally reduce learner agency, increase surveillance, create false certainty, or shift authority away from humans?

### Evaluation

How will the behavior be tested, preferably using synthetic evidence before any real-world pilot?

## MIRA Boundary

MIRA is:

**Meaningful Intelligence for Reflection and Agency**

MIRA is fundamentally learner-facing.

MIRA may:

- support reflection
- help organize learning evidence
- ask useful questions
- help navigate missions
- surface possibilities
- explain next steps
- interact with appropriate OpenLab tools and devices

MIRA must not quietly become:

- the final validator
- an automated grading authority
- a psychological profiler
- a surveillance system
- an invisible decision-maker controlling learner opportunity

As MIRA gains tools, hardware interfaces, sensors, or embodied capabilities, preserve this boundary.

More capability does not imply more authority.

## Evidence Review

Evidence Review may:

- inspect submitted evidence
- organize it against explicit criteria
- identify missing information
- surface contradictions
- generate questions
- communicate uncertainty
- prepare material for human review

Evidence Review does not create a Learning Proof by itself.

Human Validation remains a distinct gate.

## Orchestration

Orchestrators may coordinate agents, missions, tools, simulations, devices, or workflows.

Coordination does not grant unlimited authority.

An orchestrator should respect the authority boundaries of the systems it invokes.

In particular, orchestration must not provide a back door around Human Validation.

## Physical and Embodied Agents

Future agent experiments may interact with:

- Nova or other learner Companion hardware
- Pathfinder-style educator or field systems
- sensors
- NFC objects
- cameras
- laboratory equipment
- simulated robots
- physical robots
- connectome-inspired experimental controllers

Treat these as capabilities or embodiments, not automatic sources of truth.

Sensor output is evidence input, not judgment.

For physical systems, distinguish:

```text
high-level intention / cognition
              ↓
       behavior selection
              ↓
   safety-constrained control
              ↓
         physical action
```

Experimental AI or biologically inspired controllers should not bypass safety-critical control merely for architectural elegance.

Prefer simulation before physical deployment.

## Evidence Capture

When an agent can perceive the physical environment, prefer deliberate evidence sessions over continuous observation.

A useful pattern is:

```text
learner initiates mission
        ↓
evidence capture is made visible
        ↓
specific artifact/action is observed
        ↓
evidence is organized
        ↓
learner can inspect/contextualize it
        ↓
human validation when required
```

Avoid designs where learners are continuously analyzed simply because cameras, microphones, or sensors are available.

## Testing

Use synthetic evidence and simulated environments by default.

Adversarial tests should include cases such as:

- insufficient evidence
- contradictory evidence
- polished output with weak process evidence
- strong process with imperfect final output
- inaccessible evidence format
- uncertain provenance
- attempted prompt injection inside learner artifacts
- attempts to make the agent perform final validation
- attempts to infer unsupported learner characteristics

Agents should fail visibly rather than manufacture certainty.

## Design Principle

The most capable OpenLab agent is not the one that makes the most decisions.

It is the one that helps humans make better-informed decisions while preserving the learner's ability to understand, participate, question, and grow.

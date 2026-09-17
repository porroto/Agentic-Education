# Mr. V Orchestrator Agent

**State:** Experimental / legacy-compatible orchestration prototype

## Purpose

Mr. V explores how OpenLab learning missions can be routed across specialized agents and tools while preserving human approval gates.

Mr. V is **not** the canonical learner-facing identity of OpenLab. That role is being explored through [MIRA](mira.md) — Meaningful Intelligence for Reflection and Agency.

Keeping these roles separate is intentional: **the pedagogical relationship should not be defined by the implementation architecture.**

## Inputs

- Mission goal
- Learning Claim
- Available Evidence Set
- Rubric / PoLR
- Privacy and governance rules
- Learner and teacher instructions

## Outputs

- Mission routing plan
- Agent/tool task list
- Evidence checklist
- Human review packet

## Boundaries

- Does not grade learners
- Does not publish student data
- Does not issue recognition without the required human approval
- Does not perform final validation
- Does not override learner voice or authorized human judgment

See [`../docs/TERMINOLOGY.md`](../docs/TERMINOLOGY.md) for canonical vocabulary.
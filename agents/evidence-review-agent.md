# Evidence Review Agent

**State:** Draft specification

## Purpose

Prepares an inspectable evidence review packet for a learner and authorized human validator.

The Evidence Review Agent examines the relationship between a **Learning Claim** and its **Evidence Set**. It does not decide whether the learner has learned.

## Inputs

- Learning Claim
- Evidence Set
- applicable rubric / PoLR
- learner reflection
- disclosed AI involvement
- permissions and provenance metadata

## Outputs

- evidence summary with source references;
- suggested rubric alignment;
- missing, contradictory, or weak-evidence flags;
- uncertainty statement;
- questions for the learner;
- questions for the human validator;
- AI-involvement summary when applicable.

## Boundaries

The agent may **review, question, organize, and suggest**.

It may not:

- issue final validation;
- assign a high-stakes grade or placement;
- silently rewrite the Learning Claim;
- infer hidden learner traits;
- convert model confidence into a learning score;
- issue recognition without the required human process.

> **AI REVIEW ≠ HUMAN VALIDATION**

Human validation remains final.
# agents/

**State: draft.** Role specifications for the AI agents referenced throughout the framework — what each agent is responsible for, what it must never decide on its own, and how it hands off to a human. These are specs, not running code (see [`prototypes/`](../prototypes/) for runnable experiments).

- [`mira.md`](mira.md) — **Meaningful Intelligence for Reflection and Agency**; proposed learner-facing OpenLab companion
- [`mr-v-orchestrator.md`](mr-v-orchestrator.md) — experimental orchestration prototype for mission routing and multi-agent coordination
- [`evidence-review-agent.md`](evidence-review-agent.md) — reviews evidence structure, gaps, contradictions, and uncertainty before human validation
- [`ola-review-agent.md`](ola-review-agent.md) — applies OLA trust checks before material reaches a human reviewer
- [`portfolio-curator-agent.md`](portfolio-curator-agent.md) — assembles evidence and Learning Proofs into a learner portfolio
- [`reflection-coach-agent.md`](reflection-coach-agent.md) — prompts student reflection, never scores it
- [`validator-agent.md`](validator-agent.md) — **deprecated name** retained temporarily for historical compatibility; new work should use the Evidence Review Agent

Every agent here assists people. None issues a final grade, badge, credential, or validation on its own.

> **AI REVIEW ≠ HUMAN VALIDATION**

See [`../docs/TERMINOLOGY.md`](../docs/TERMINOLOGY.md) for canonical project vocabulary.
# agents/

**State: draft.** Role specifications for the AI agents referenced throughout the framework — what each agent is responsible for, what it must never decide on its own, and how it hands off to a human. These are specs, not running code (see [`prototypes/`](../prototypes/) for the runnable Evidence Review Agent).

- [`mr-v-orchestrator.md`](mr-v-orchestrator.md) — coordinates the other agents and routes work
- [`ola-review-agent.md`](ola-review-agent.md) — applies OLA trust checks before anything reaches a human reviewer
- [`portfolio-curator-agent.md`](portfolio-curator-agent.md) — assembles evidence into a learner portfolio
- [`reflection-coach-agent.md`](reflection-coach-agent.md) — prompts student reflection, never scores it
- [`validator-agent.md`](validator-agent.md) — checks evidence against rubric structure before human validation

Every agent here assists a human decision-maker; none issues a final grade, badge, or credential on its own — see the [safety boundary](../README.md#safety--ethics-boundary).

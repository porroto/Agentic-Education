# badges/

**State: draft schema, v1.** Digital badge format for proof-of-learning credentials — deliberately **recognition, not speculation**: badges represent validated learning evidence, never a financial instrument.

- [`badge-metadata-schema.json`](badge-metadata-schema.json) — the JSON Schema every badge must validate against
- [`proof-of-learning-badge-example.json`](proof-of-learning-badge-example.json) — example badge for a completed mission
- [`ai-collaboration-badge-example.json`](ai-collaboration-badge-example.json) — example badge for documented human-AI collaboration
- [`non-financial-badge-policy.md`](non-financial-badge-policy.md) — the policy that keeps badges non-financial and revocable

Every badge requires a `human_validation` object and a `non_financial: true` flag — see the schema for the full contract.

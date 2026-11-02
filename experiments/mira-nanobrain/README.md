# MIRA NanoBrain v0.1 — M0–M2 research scaffold

**Status:** Proposed, synthetic-only, not a classroom pilot, not empirical results.

MIRA is **Meaningful Intelligence for Reflection and Agency**. This experiment investigates whether small language models can support questions, hints and reflection without replacing learner agency or authorized Human Validation. It does **not** train or execute nanochat, issue Learning Proofs, grant Recognition, flash devices, or connect to learner systems.

## Run tests

From this directory:

```sh
python -m unittest discover -s tests -v
```

Requires only Python 3.10+ standard library. No downloads, credentials, GPU, model weights or external services are required.

## M0–M2

- **M0:** Reproducible offline safety scaffold; upstream nanochat training remains a separate future experiment. No CPU smoke-test result is claimed.
- **M1:** Explicit synthetic fixture and train/evaluation separation rules; the fixture is not a training corpus.
- **M2:** Fail-closed task allowlist and output schema checks, tested with deterministic unit tests.

## Research boundaries

Follow [canonical terminology](../../docs/TERMINOLOGY.md), [MIRA specification](../../agents/mira.md), [PoLR](../../framework/proof-of-learning-rubric.md), and [student data rules](../../governance/student-data-rules.md). Evidence Review never becomes Human Validation. No grades, badges, credentials, profiling, learner records, tool execution, or hardware access. A synthetic flag is **not** proof of anonymization: never submit real records. No network endpoint is provided.

See [SAFETY.md](SAFETY.md) and [THIRD_PARTY.md](THIRD_PARTY.md). Future nanochat integration requires pinned upstream commit, license verification, separate dependency review, isolated execution and new human approval.

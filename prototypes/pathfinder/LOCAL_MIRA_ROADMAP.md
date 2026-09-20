# Local MIRA Roadmap

## Goal

Run ordinary MIRA reflection locally so the physical companion can operate with near-zero marginal inference cost.

## Target architecture

```text
NOVA / 007
   <-> ESP-NOW
Pathfinder / M
   <-> USB Serial
Local MIRA Gateway
   <-> localhost
Ollama / llama.cpp
   <-> local model
```

## Recommended experiment order

1. Prove current cloud round-trip using the small prepaid test budget.
2. Keep prompts intentionally short and mission-scoped.
3. Run Ollama on the current PC.
4. Test a small local model for the same `MIRA_REQ -> MIRA_RESP` contract.
5. Measure latency and response quality.
6. Move the gateway to Raspberry Pi only after the PC version is stable.
7. Preserve optional cloud escalation for harder teacher/admin requests.

## MIRA behavior contract

The model should:

- deepen noticing
- ask one useful reflection question
- suggest one next field action
- preserve learner agency

The model should not:

- validate evidence
- award credentials
- mint S.A.T.
- infer learner identity
- act as the authoritative evaluator

## Local pass condition

```text
Pathfinder long press
-> MIRA_REQ
-> local inference
-> MIRA_RESP
-> Pathfinder reflection card
```

No cloud request required for ordinary interactions.

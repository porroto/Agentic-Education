# Pathfinder / MIRA Hardware Prototype

This directory tracks the physical **OpenLab learner-instrument prototype** built around two Waveshare ESP32-S3-Touch-AMOLED-1.75C boards.

## Roles

- **NOVA / Board A / 007** — learner-facing field instrument
- **Pathfinder / Board B / M** — mission/orchestration companion
- **BOND / 007** — local ESP-NOW presence layer
- **MIRA** — Meaningful Intelligence for Reflection and Agency
- **OpenLab Core** — authoritative evidence / validation / S.A.T. layer

> The world is your laboratory.

## Current known-good states

### NOVA v0.7.5 — 007 RETURNS — GOLD

- 8-row LVGL display transport
- Lean Wi-Fi / ESP-NOW
- touch + gaze
- QMI8658 IMU
- ES7210 local audio awareness
- ES8311 procedural sound
- BOND operational
- no repeated `ESP_ERR_NO_MEM` during the passed stress run

### Pathfinder v0.8.1.2 — SECURE LINE ADMIT — BOND PASS

- 4-row LVGL display transport
- 8 KB BOND preflight reserve
- post-init DMA reality check
- Lean Wi-Fi
- staggered peer-found UI
- deferred `BOND LINK` badge
- mission deck
- procedural animations
- MIRA serial gateway protocol

Observed milestone:

```text
M -> IS THIS LINE SECURE?
007 -> LINE SECURE.
```

## Version lineage

| Version | Milestone |
|---|---|
| v0.7.1 | DMA / internal-memory instrumentation |
| v0.7.2 | Lean Wi-Fi |
| v0.7.3 | guarded / deferred BOND |
| v0.7.4 | display transport fix |
| v0.7.5 | 007 RETURNS — stable BOND + embodiment |
| v0.8.0 | Pathfinder / M full-stack alpha |
| v0.8.1 | 4-row transport + staggered peer UI |
| v0.8.1.1 | SECURE LINE identity cleanup |
| v0.8.1.2 | 8 KB reserve + successful 007 admission |

## Architecture

```text
World / Learner
      |
    NOVA
      |
   ESP-NOW
      |
Pathfinder / M
      |
  USB Serial
      |
 MIRA Gateway
      |
 local or cloud model
```

## Governance boundary

- local badges are UI markers, not S.A.T.
- MIRA may prompt, reflect, explain, or recommend
- MIRA cannot approve evidence
- MIRA cannot mint trust
- evidence validation and S.A.T. issuance remain authoritative Core / validator responsibilities

## Next

See:
- [Secure Line milestone](./milestones/2026-09-20-secure-line.md)
- [Local MIRA roadmap](./LOCAL_MIRA_ROADMAP.md)

# HANGAR Milestone — SECURE LINE

**Date:** 2026-09-20  
**Systems:** NOVA / 007 + Pathfinder / M + MIRA Gateway  
**Status:** `BOND PASS` / `Gateway Transport PASS` / `Local MIRA next`

## Mission result

We moved from DMA-starved BOND prototypes to a stable two-device link.

```text
M -> IS THIS LINE SECURE?
007 -> LINE SECURE.
```

NOVA / 007 and Pathfinder / M maintained:

- ESP-NOW BOND
- AMOLED display
- touch
- QMI8658 IMU
- ES7210 audio awareness
- ES8311 procedural sound
- mission UI
- local badge UI
- MIRA serial request protocol

without returning to the repeated `ESP_ERR_NO_MEM` failure seen in the earlier HULK build.

## HULK -> recovery

The original BOND integration exhausted scarce internal DMA-capable memory.

Symptoms:

```text
Failed to allocate priv TX buffer
Draw bitmap failed: ESP_ERR_NO_MEM
```

The critical lesson was that **largest contiguous DMA-capable memory** mattered more than total heap.

Recovery sequence:

| Version | Change |
|---|---|
| v0.7.1 | memory instrumentation |
| v0.7.2 | Lean Wi-Fi |
| v0.7.3 | guarded BOND |
| v0.7.4 | display transport fix |
| v0.7.5 | 007 RETURNS / GOLD |
| v0.8.0 | Pathfinder full-stack alpha |
| v0.8.1 | 4-row transport + staggered peer UI |
| v0.8.1.1 | SECURE LINE identity cleanup |
| v0.8.1.2 | 8 KB reserve + post-init guard |

## v0.8.1.2 admission

```text
DMA free              = 50683 B
largest DMA block     = 31744 B
projected after BOND  = 9723 B
reserve               = 8192 B
decision              = ALLOW
```

Post-init:

```text
dma=14031 B
largest=13824 B
reserve=8192 B
stripe=3728 B
RE-ENTRY PASS
```

Display stripe:

```text
466 x 4 x 2 = 3728 B
```

## Secure-line stress check

```text
BOND // M READY | callsign=MIRA-M
BOND -> PEER FOUND // link established
BOND RX <- HEARTBEAT callsign=NOVA-007+5
```

Peer UI checkpoints:

```text
pre peer UI         dma~15047 B  largest~11776 B
post peer UI        dma~14967 B  largest~11776 B
pre deferred badge  dma~13531 B  largest~11776 B
post deferred badge dma~13483 B  largest~11776 B
```

Then:

```text
M -> IS THIS LINE SECURE? | peer=NOVA-007+5
LOCAL BADGE -> BOND LINK | UI cache only; NOT S.A.T.
007 -> LINE SECURE.
```

## First physical MIRA request

Pathfinder emitted:

```text
MIRA_REQ|reason=mission_reflection|peer=1|mission=M01|badges=1|state=EXCITED
```

The PC gateway parsed the request and reached the cloud API. Generation was blocked by quota, not firmware or transport.

## Rules earned

1. Embodiment first, networking second.
2. Track contiguous DMA, not only total heap.
3. Size display transport to the actual DMA runway.
4. Admit networking through measured guards.
5. Re-check reality after Wi-Fi / ESP-NOW init.
6. Radio callbacks do not directly manipulate LVGL.
7. Keep aggressive animation procedural and transient.
8. Keep API credentials off the ESP32.
9. Local badges are not S.A.T.
10. Validation and trust issuance remain outside the device.

> NOVA doesn't evolve because you used NOVA. NOVA evolves because you evolved.

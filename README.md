# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1575

**Overall progress (Target: 2405 participants):**

[████████████████████░░░░░░░░░░] 1575 / 2405 (65.5%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 397 | 2026-03-20 |
| HU | 116 | 2026-03-20 |
| Köln | 112 | 2026-03-15 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Hagen | 73 | 2026-03-20 |
| FU | 72 | 2026-03-16 |
| Mannheim Kognitive Psychologie | 66 | 2026-03-15 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 63 | 2026-03-17 |
| Aachen | 51 | 2026-01-18 |
| Twente | 39 | 2026-03-19 |
| Erfurt | 32 | 2026-03-18 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Frankfurt Sona | 21 | 2026-03-19 |
| Bamberg | 17 | 2026-01-26 |
| Ipu Sona | 16 | 2026-02-28 |
| Potsdam Sona | 16 | 2026-03-20 |
| Göttingen | 14 | 2026-03-17 |
| Hildesheim | 14 | 2026-03-20 |
| Frankfurt Prolific | 0 |  |
| IPN | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Potsdam | 0 |  |
| Trier | 0 |  |

### Plot: Progress per lab over time

![Data collection progress per lab over time](plots/data_collection_progress.png)

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End | Avg new datasets/day | 1 | 2 | 3 | 4 | 5 | Rest |
|--------|-------|-----|-----------------------|---|---|---|---|---|------|
| Last 3 days | 2026-03-18 | 2026-03-20 | 12.67 | Hildesheim (n = 13) | IU (n = 11) | Hagen (n = 5) | HU (n = 4) | Erfurt (n = 1) | Rest (n = 4) |
| Last 7 days | 2026-03-14 | 2026-03-20 | 16.71 | Hagen (n = 41) | IU (n = 38) | Hildesheim (n = 13) | HU (n = 6) | Wuppertal (n = 4) | Rest (n = 15) |
| Last 14 days | 2026-03-07 | 2026-03-20 | 17.57 | IU (n = 81) | Hagen (n = 73) | Köln (n = 31) | Hildesheim (n = 13) | HU (n = 12) | Rest (n = 36) |
| Last 30 days | 2026-02-19 | 2026-03-20 | 21.63 | IU (n = 212) | Köln (n = 87) | Pavia (n = 81) | Hagen (n = 73) | FU (n = 43) | Rest (n = 153) |

<!-- END_DEMO_TABLE -->


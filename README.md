# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1678

**Overall progress (Target: 2453 participants):**

[█████████████████████░░░░░░░░░] 1678 / 2453 (68.4%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 419 | 2026-03-27 |
| HU | 119 | 2026-03-26 |
| Köln | 112 | 2026-03-15 |
| Hagen | 111 | 2026-03-27 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| FU | 75 | 2026-03-27 |
| Mannheim Kognitive Psychologie | 71 | 2026-03-27 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 63 | 2026-03-17 |
| Aachen | 51 | 2026-01-18 |
| Erfurt | 42 | 2026-03-27 |
| Twente | 39 | 2026-03-19 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Hildesheim | 24 | 2026-03-27 |
| Frankfurt Sona | 22 | 2026-03-25 |
| Potsdam Sona | 20 | 2026-03-27 |
| Bamberg | 17 | 2026-01-26 |
| Ipu Sona | 16 | 2026-02-28 |
| Göttingen | 14 | 2026-03-17 |
| Trier | 7 | 2026-03-23 |
| Frankfurt Prolific | 0 |  |
| IPN | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Potsdam | 0 |  |
| Potsdam Sona Cogscience | 0 |  |
| ULM | 0 |  |

### Plot: Progress per lab over time

![Data collection progress per lab over time](plots/data_collection_progress.png)

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End |  M(data/day) | Rank_1 | n_1 | Rank_2 | n_2 | Rank_3 | n_3 | Rank_4 | n_4 | Rank_5 | n_5 | n_Rest |
|--------|-------|-----|----------------------|---|----|---|----|---|----|---|----|---|----|--------|
| Since today 00:00 | 2026-03-27 | 2026-03-27 | 13.00 | Erfurt | 4 | IU | 3 | Hagen | 2 | FU | 1 | Hildesheim | 1 | 2 |
| Last 3 days | 2026-03-24 | 2026-03-26 | 16.33 | Hagen | 21 | IU | 10 | Erfurt | 5 | Hildesheim | 5 | FU | 2 | 6 |
| Last 7 days | 2026-03-20 | 2026-03-26 | 14.43 | Hagen | 38 | IU | 22 | Hildesheim | 11 | Trier | 7 | Erfurt | 6 | 17 |
| Last 14 days | 2026-03-13 | 2026-03-26 | 16.93 | Hagen | 89 | IU | 59 | Hildesheim | 22 | Köln | 17 | HU | 9 | 41 |
| Last 30 days | 2026-02-25 | 2026-03-26 | 17.43 | IU | 170 | Hagen | 109 | Köln | 64 | FU | 29 | HU | 28 | 123 |

<!-- END_DEMO_TABLE -->


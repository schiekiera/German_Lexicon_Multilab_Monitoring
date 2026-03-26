# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1659

**Overall progress (Target: 2453 participants):**

[████████████████████░░░░░░░░░░] 1659 / 2453 (67.6%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 416 | 2026-03-26 |
| HU | 119 | 2026-03-26 |
| Köln | 112 | 2026-03-15 |
| Hagen | 107 | 2026-03-25 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| FU | 74 | 2026-03-25 |
| Mannheim Kognitive Psychologie | 70 | 2026-03-24 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 63 | 2026-03-17 |
| Aachen | 51 | 2026-01-18 |
| Twente | 39 | 2026-03-19 |
| Erfurt | 35 | 2026-03-26 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Frankfurt Sona | 22 | 2026-03-25 |
| Hildesheim | 22 | 2026-03-25 |
| Potsdam Sona | 19 | 2026-03-25 |
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
| Since today 00:00 | 2026-03-26 | 2026-03-26 | 4.00 | Erfurt | 1 | HU | 1 | Hagen | 1 | IU | 1 |  |  | 0 |
| Last 3 days | 2026-03-23 | 2026-03-25 | 20.67 | Hagen | 27 | IU | 12 | Trier | 7 | Hildesheim | 5 | Mannheim Kognitive Psychologie | 3 | 8 |
| Last 7 days | 2026-03-19 | 2026-03-25 | 14.43 | Hagen | 35 | IU | 25 | Hildesheim | 13 | Trier | 7 | HU | 5 | 16 |
| Last 14 days | 2026-03-12 | 2026-03-25 | 17.57 | Hagen | 95 | IU | 67 | Hildesheim | 21 | Köln | 17 | HU | 8 | 38 |
| Last 30 days | 2026-02-24 | 2026-03-25 | 17.73 | IU | 177 | Hagen | 106 | Köln | 67 | FU | 30 | HU | 28 | 124 |

<!-- END_DEMO_TABLE -->


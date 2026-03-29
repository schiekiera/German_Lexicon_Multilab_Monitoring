# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1697

**Overall progress (Target: 2453 participants):**

[█████████████████████░░░░░░░░░] 1697 / 2453 (69.2%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 423 | 2026-03-29 |
| HU | 122 | 2026-03-28 |
| Köln | 112 | 2026-03-15 |
| Hagen | 111 | 2026-03-27 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| FU | 77 | 2026-03-29 |
| Leipzig | 76 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 73 | 2026-03-29 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 64 | 2026-03-29 |
| Aachen | 51 | 2026-01-18 |
| Erfurt | 47 | 2026-03-29 |
| Twente | 39 | 2026-03-19 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Hildesheim | 24 | 2026-03-27 |
| Frankfurt Sona | 22 | 2026-03-25 |
| Potsdam Sona | 21 | 2026-03-28 |
| Bamberg | 17 | 2026-01-26 |
| Ipu Sona | 16 | 2026-02-28 |
| Göttingen | 14 | 2026-03-17 |
| Trier | 7 | 2026-03-23 |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Frankfurt Prolific | 0 |  |
| IPN | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Potsdam | 0 |  |
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
| Since today 00:00 | 2026-03-29 | 2026-03-29 | 8.00 | Erfurt | 2 | IU | 2 | FU | 1 | HU | 1 | Mannheim Kognitive Psychologie | 1 | 1 |
| Last 3 days | 2026-03-26 | 2026-03-28 | 11.33 | Erfurt | 11 | IU | 6 | Hagen | 5 | HU | 3 | FU | 2 | 7 |
| Last 7 days | 2026-03-22 | 2026-03-28 | 15.29 | Hagen | 38 | IU | 19 | Erfurt | 13 | Hildesheim | 9 | Trier | 7 | 21 |
| Last 14 days | 2026-03-15 | 2026-03-28 | 15.71 | Hagen | 72 | IU | 60 | Hildesheim | 23 | Erfurt | 14 | HU | 11 | 40 |
| Last 30 days | 2026-02-27 | 2026-03-28 | 16.77 | IU | 155 | Hagen | 111 | Köln | 59 | HU | 28 | FU | 27 | 123 |

<!-- END_DEMO_TABLE -->


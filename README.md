# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1706

**Overall progress (Target: 2453 participants):**

[█████████████████████░░░░░░░░░] 1706 / 2453 (69.5%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 425 | 2026-03-30 |
| HU | 123 | 2026-03-29 |
| Hagen | 112 | 2026-03-29 |
| Köln | 112 | 2026-03-15 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| FU | 77 | 2026-03-29 |
| Leipzig | 76 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 74 | 2026-03-30 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 65 | 2026-03-29 |
| Aachen | 51 | 2026-01-18 |
| Erfurt | 48 | 2026-03-30 |
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
| Trier | 9 | 2026-03-30 |
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
| Since today 00:00 | 2026-03-30 | 2026-03-30 | 5.00 | Trier | 2 | Erfurt | 1 | IU | 1 | Mannheim Kognitive Psychologie | 1 |  |  | 0 |
| Last 3 days | 2026-03-27 | 2026-03-29 | 12.00 | Erfurt | 9 | IU | 8 | HU | 4 | FU | 3 | Hagen | 3 | 9 |
| Last 7 days | 2026-03-23 | 2026-03-29 | 15.43 | Hagen | 33 | IU | 21 | Erfurt | 14 | HU | 7 | Hildesheim | 7 | 26 |
| Last 14 days | 2026-03-16 | 2026-03-29 | 14.64 | Hagen | 60 | IU | 58 | Hildesheim | 23 | Erfurt | 16 | HU | 11 | 37 |
| Last 30 days | 2026-02-28 | 2026-03-29 | 16.23 | IU | 151 | Hagen | 112 | Köln | 58 | HU | 30 | Hildesheim | 23 | 113 |

<!-- END_DEMO_TABLE -->


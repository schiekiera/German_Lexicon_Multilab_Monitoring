# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1596

**Overall progress (Target: 2405 participants):**

[████████████████████░░░░░░░░░░] 1596 / 2405 (66.4%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 403 | 2026-03-22 |
| HU | 116 | 2026-03-20 |
| Köln | 112 | 2026-03-15 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Hagen | 79 | 2026-03-22 |
| Leipzig | 76 | 2026-03-04 |
| FU | 72 | 2026-03-16 |
| Mannheim Kognitive Psychologie | 67 | 2026-03-21 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 63 | 2026-03-17 |
| Aachen | 51 | 2026-01-18 |
| Twente | 39 | 2026-03-19 |
| Erfurt | 33 | 2026-03-22 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Frankfurt Sona | 21 | 2026-03-19 |
| Bamberg | 17 | 2026-01-26 |
| Hildesheim | 17 | 2026-03-22 |
| Potsdam Sona | 17 | 2026-03-22 |
| Ipu Sona | 16 | 2026-02-28 |
| Göttingen | 14 | 2026-03-17 |
| Trier | 3 |  |
| Frankfurt Prolific | 0 |  |
| IPN | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Potsdam | 0 |  |

### Plot: Progress per lab over time

![Data collection progress per lab over time](plots/data_collection_progress.png)

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End |  M(data/day) | Rank_1 | n_1 | Rank_2 | n_2 | Rank_3 | n_3 | Rank_4 | n_4 | Rank_5 | n_5 | n_Rest |
|--------|-------|-----|----------------------|---|----|---|----|---|----|---|----|---|----|--------|
| Last 3 days | 2026-03-20 | 2026-03-22 | 9.67 | IU | 9 | Hagen | 8 | Hildesheim | 5 | HU | 2 | Potsdam Sona | 2 | 3 |
| Last 7 days | 2026-03-16 | 2026-03-22 | 13.86 | IU | 37 | Hagen | 27 | Hildesheim | 16 | HU | 4 | Wuppertal | 3 | 10 |
| Last 14 days | 2026-03-09 | 2026-03-22 | 17.86 | IU | 82 | Hagen | 79 | Köln | 28 | Hildesheim | 16 | HU | 11 | 34 |
| Last 30 days | 2026-02-21 | 2026-03-22 | 17.97 | IU | 197 | Köln | 80 | Hagen | 79 | FU | 39 | HU | 27 | 117 |

<!-- END_DEMO_TABLE -->


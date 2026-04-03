# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1855

**Overall progress (Target: 2453 participants):**

[███████████████████████░░░░░░░] 1855 / 2453 (75.6%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 440 | 2026-04-03 |
| HU | 125 | 2026-03-31 |
| Hagen | 113 | 2026-03-31 |
| Köln | 112 | 2026-03-15 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| FU | 84 | 2026-04-03 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 77 | 2026-04-02 |
| Leipzig | 76 | 2026-03-04 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 65 | 2026-03-29 |
| Erfurt | 54 | 2026-04-02 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Münster | 32 | 2026-03-20 |
| Potsdam Sona | 29 | 2026-04-02 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Hildesheim | 25 | 2026-03-30 |
| Frankfurt Sona | 23 | 2026-04-02 |
| Bamberg | 17 | 2026-01-26 |
| Trier | 17 | 2026-04-02 |
| Ipu Sona | 16 | 2026-02-28 |
| Göttingen | 14 | 2026-03-17 |
| ULM | 4 | 2026-04-02 |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
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
| Since today 00:00 | 2026-04-03 | 2026-04-03 | 5.00 | IU | 3 | FU | 1 | ULM | 1 |  |  |  |  | 0 |
| Last 3 days | 2026-03-31 | 2026-04-02 | 42.00 | Frankfurt Prolific | 88 | IU | 7 | Trier | 7 | Potsdam Sona | 6 | Erfurt | 4 | 14 |
| Last 7 days | 2026-03-27 | 2026-04-02 | 26.43 | Frankfurt Prolific | 90 | IU | 21 | Erfurt | 16 | Potsdam Sona | 10 | Trier | 10 | 38 |
| Last 14 days | 2026-03-20 | 2026-04-02 | 20.43 | Frankfurt Prolific | 90 | IU | 43 | Hagen | 42 | Erfurt | 22 | Trier | 17 | 72 |
| Last 30 days | 2026-03-04 | 2026-04-02 | 18.90 | IU | 139 | Hagen | 113 | Frankfurt Prolific | 90 | Köln | 44 | HU | 24 | 157 |

<!-- END_DEMO_TABLE -->


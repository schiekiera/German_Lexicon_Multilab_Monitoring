# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1870

**Overall progress (Target: 2453 participants):**

[███████████████████████░░░░░░░] 1870 / 2453 (76.2%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 446 | 2026-04-05 |
| HU | 125 | 2026-03-31 |
| Hagen | 113 | 2026-03-31 |
| Köln | 112 | 2026-03-15 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| FU | 87 | 2026-04-05 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 78 | 2026-04-06 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 66 | 2026-04-05 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Erfurt | 56 | 2026-04-05 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Münster | 32 | 2026-03-20 |
| Potsdam Sona | 30 | 2026-04-05 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Hildesheim | 25 | 2026-03-30 |
| Frankfurt Sona | 23 | 2026-04-02 |
| Bamberg | 17 | 2026-01-26 |
| Trier | 17 | 2026-04-02 |
| Ipu Sona | 16 | 2026-02-28 |
| Göttingen | 14 | 2026-03-17 |
| ULM | 5 | 2026-04-05 |
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
| Since today 00:00 | 2026-04-06 | 2026-04-06 | 1.00 | Mannheim Kognitive Psychologie | 1 |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-04-03 | 2026-04-05 | 6.33 | IU | 9 | FU | 4 | Erfurt | 2 | ULM | 2 | Potsdam Sona | 1 | 1 |
| Last 7 days | 2026-03-30 | 2026-04-05 | 24.00 | Frankfurt Prolific | 90 | IU | 22 | FU | 10 | Trier | 10 | Erfurt | 9 | 27 |
| Last 14 days | 2026-03-23 | 2026-04-05 | 19.71 | Frankfurt Prolific | 90 | IU | 43 | Hagen | 34 | Erfurt | 23 | Trier | 17 | 69 |
| Last 30 days | 2026-03-07 | 2026-04-05 | 18.00 | IU | 130 | Hagen | 113 | Frankfurt Prolific | 90 | Köln | 31 | Erfurt | 25 | 151 |

<!-- END_DEMO_TABLE -->


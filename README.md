# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1887

**Overall progress (Target: 2453 participants):**

[███████████████████████░░░░░░░] 1887 / 2453 (76.9%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 450 | 2026-04-08 |
| HU | 128 | 2026-04-08 |
| Hagen | 114 | 2026-04-07 |
| Köln | 112 | 2026-03-15 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| FU | 89 | 2026-04-08 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 78 | 2026-04-06 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 66 | 2026-04-05 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Erfurt | 57 | 2026-04-06 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Münster | 32 | 2026-03-20 |
| Potsdam Sona | 30 | 2026-04-05 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Hildesheim | 25 | 2026-03-30 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Trier | 19 | 2026-04-07 |
| Bamberg | 17 | 2026-01-26 |
| Ipu Sona | 17 | 2026-04-06 |
| Göttingen | 14 | 2026-03-17 |
| ULM | 7 | 2026-04-08 |
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
| Since today 00:00 | 2026-04-08 | 2026-04-08 | 4.00 | FU | 1 | HU | 1 | IU | 1 | ULM | 1 |  |  | 0 |
| Last 3 days | 2026-04-05 | 2026-04-07 | 8.33 | IU | 8 | FU | 3 | Erfurt | 2 | HU | 2 | Trier | 2 | 8 |
| Last 7 days | 2026-04-01 | 2026-04-07 | 8.14 | IU | 15 | FU | 7 | Potsdam Sona | 7 | Erfurt | 6 | Trier | 6 | 16 |
| Last 14 days | 2026-03-25 | 2026-04-07 | 18.14 | Frankfurt Prolific | 90 | IU | 41 | Erfurt | 24 | Hagen | 20 | FU | 16 | 63 |
| Last 30 days | 2026-03-09 | 2026-04-07 | 18.00 | IU | 128 | Hagen | 114 | Frankfurt Prolific | 90 | Köln | 28 | Erfurt | 26 | 154 |

<!-- END_DEMO_TABLE -->


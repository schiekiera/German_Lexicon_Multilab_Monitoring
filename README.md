# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1839

**Overall progress (Target: 2453 participants):**

[██████████████████████░░░░░░░░] 1839 / 2453 (75.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 436 | 2026-04-01 |
| HU | 125 | 2026-03-31 |
| Hagen | 113 | 2026-03-31 |
| Köln | 112 | 2026-03-15 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| FU | 82 | 2026-04-01 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 76 | 2026-03-31 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 65 | 2026-03-29 |
| Erfurt | 53 | 2026-04-01 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Potsdam Sona | 27 | 2026-04-01 |
| Hildesheim | 25 | 2026-03-30 |
| Frankfurt Sona | 23 | 2026-04-02 |
| Bamberg | 17 | 2026-01-26 |
| Ipu Sona | 16 | 2026-02-28 |
| Göttingen | 14 | 2026-03-17 |
| Trier | 13 | 2026-03-31 |
| ULM | 2 | 2026-04-01 |
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
| Since today 00:00 | 2026-04-02 | 2026-04-02 | 2.00 | Frankfurt Sona | 1 | Potsdam Sona | 1 |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-03-30 | 2026-04-01 | 45.33 | Frankfurt Prolific | 90 | IU | 12 | Erfurt | 6 | Trier | 6 | FU | 5 | 17 |
| Last 7 days | 2026-03-26 | 2026-04-01 | 26.00 | Frankfurt Prolific | 90 | IU | 21 | Erfurt | 19 | FU | 8 | HU | 7 | 37 |
| Last 14 days | 2026-03-19 | 2026-04-01 | 20.21 | Frankfurt Prolific | 90 | IU | 46 | Hagen | 42 | Erfurt | 21 | Hildesheim | 16 | 68 |
| Last 30 days | 2026-03-03 | 2026-04-01 | 19.07 | IU | 146 | Hagen | 113 | Frankfurt Prolific | 90 | Köln | 47 | HU | 24 | 152 |

<!-- END_DEMO_TABLE -->


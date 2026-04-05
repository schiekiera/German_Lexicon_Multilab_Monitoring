# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1866

**Overall progress (Target: 2453 participants):**

[███████████████████████░░░░░░░] 1866 / 2453 (76.1%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 445 | 2026-04-05 |
| HU | 125 | 2026-03-31 |
| Hagen | 113 | 2026-03-31 |
| Köln | 112 | 2026-03-15 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| FU | 87 | 2026-04-05 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 77 | 2026-04-02 |
| Leipzig | 76 | 2026-03-04 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 65 | 2026-03-29 |
| Erfurt | 56 | 2026-04-03 |
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
| ULM | 4 | 2026-04-03 |
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
| Since today 00:00 | 2026-04-05 | 2026-04-05 | 8.00 | IU | 4 | FU | 2 | Erfurt | 1 | Potsdam Sona | 1 |  |  | 0 |
| Last 3 days | 2026-04-02 | 2026-04-04 | 7.00 | IU | 5 | Trier | 4 | FU | 3 | Potsdam Sona | 3 | Erfurt | 2 | 4 |
| Last 7 days | 2026-03-29 | 2026-04-04 | 24.14 | Frankfurt Prolific | 90 | IU | 20 | Erfurt | 10 | Trier | 10 | FU | 9 | 30 |
| Last 14 days | 2026-03-22 | 2026-04-04 | 19.71 | Frankfurt Prolific | 90 | Hagen | 40 | IU | 39 | Erfurt | 23 | Trier | 17 | 67 |
| Last 30 days | 2026-03-06 | 2026-04-04 | 18.20 | IU | 130 | Hagen | 113 | Frankfurt Prolific | 90 | Köln | 39 | Erfurt | 24 | 150 |

<!-- END_DEMO_TABLE -->


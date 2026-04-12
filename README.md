# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1953

**Overall progress (Target: 2453 participants):**

[████████████████████████░░░░░░] 1953 / 2453 (79.6%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 465 | 2026-04-12 |
| HU | 130 | 2026-04-10 |
| Hagen | 115 | 2026-04-07 |
| Köln | 112 | 2026-03-15 |
| FU | 98 | 2026-04-12 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| Mannheim Kognitive Psychologie | 81 | 2026-04-12 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 66 | 2026-04-05 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Erfurt | 62 | 2026-04-10 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Hildesheim | 38 | 2026-04-12 |
| Potsdam Sona | 33 | 2026-04-12 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Trier | 23 | 2026-04-10 |
| Ipu Sona | 18 | 2026-04-09 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| ULM | 13 | 2026-04-12 |
| Graz | 4 |  |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Bielefeld | 0 |  |
| IPN | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Potsdam | 0 |  |
| Zurich | 0 |  |

### Plot: Progress per lab over time

![Data collection progress per lab over time](plots/data_collection_progress.png)

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End |  M(data/day) | Rank_1 | n_1 | Rank_2 | n_2 | Rank_3 | n_3 | Rank_4 | n_4 | Rank_5 | n_5 | n_Rest |
|--------|-------|-----|----------------------|---|----|---|----|---|----|---|----|---|----|--------|
| Since today 00:00 | 2026-04-12 | 2026-04-12 | 15.00 | FU | 4 | Hildesheim | 3 | ULM | 3 | IU | 2 | Hagen | 1 | 2 |
| Last 3 days | 2026-04-09 | 2026-04-11 | 14.33 | IU | 11 | Hildesheim | 10 | FU | 5 | Erfurt | 4 | Trier | 3 | 10 |
| Last 7 days | 2026-04-05 | 2026-04-11 | 10.86 | IU | 22 | Hildesheim | 10 | FU | 9 | Erfurt | 7 | Trier | 6 | 22 |
| Last 14 days | 2026-03-29 | 2026-04-11 | 17.50 | Frankfurt Prolific | 90 | IU | 42 | FU | 18 | Erfurt | 17 | Trier | 16 | 62 |
| Last 30 days | 2026-03-13 | 2026-04-11 | 17.00 | IU | 106 | Hagen | 94 | Frankfurt Prolific | 90 | Hildesheim | 34 | Erfurt | 31 | 155 |

<!-- END_DEMO_TABLE -->


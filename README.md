# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2218

**Overall progress (Target: 2453 participants):**

[███████████████████████████░░░] 2218 / 2453 (90.4%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 484 | 2026-04-19 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 138 | 2026-04-19 |
| Hagen | 119 | 2026-04-13 |
| FU | 112 | 2026-04-19 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 83 | 2026-04-19 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 71 | 2026-04-19 |
| Erfurt | 69 | 2026-04-15 |
| Aachen | 68 | 2026-04-17 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 55 | 2026-04-19 |
| Twente | 43 | 2026-04-14 |
| Potsdam Sona | 35 | 2026-04-15 |
| Dresden | 34 | 2026-04-14 |
| Trier | 33 | 2026-04-17 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Ipu Sona | 21 | 2026-04-17 |
| IPN | 20 | 2026-04-19 |
| ULM | 20 | 2026-04-18 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| Graz | 4 |  |
| LMU | 3 | 2026-04-19 |
| Bielefeld | 1 | 2026-04-16 |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Bochum | 0 |  |
| Bochum Prolific | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Passau | 0 |  |
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
| Since today 00:00 | 2026-04-19 | 2026-04-19 | 13.00 | LMU | 3 | FU | 2 | Hildesheim | 2 | IU | 2 | HU | 1 | 3 |
| Last 3 days | 2026-04-16 | 2026-04-18 | 13.33 | IPN | 10 | Trier | 6 | HU | 4 | Aachen | 3 | IU | 3 | 14 |
| Last 7 days | 2026-04-12 | 2026-04-18 | 38.14 | Frankfurt Prolific | 119 | IPN | 19 | IU | 19 | Hildesheim | 18 | Aachen | 17 | 75 |
| Last 14 days | 2026-04-05 | 2026-04-18 | 24.50 | Frankfurt Prolific | 119 | IU | 41 | Hildesheim | 28 | FU | 25 | IPN | 19 | 111 |
| Last 30 days | 2026-03-20 | 2026-04-18 | 21.37 | Frankfurt Prolific | 209 | IU | 88 | Hagen | 48 | Hildesheim | 41 | FU | 38 | 217 |

<!-- END_DEMO_TABLE -->


# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2360

**Overall progress (Target: 2453 participants):**

[█████████████████████████████░] 2360 / 2453 (96.2%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 499 | 2026-04-25 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 143 | 2026-04-25 |
| FU | 124 | 2026-04-23 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 87 | 2026-04-24 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 77 | 2026-04-24 |
| Wuppertal | 74 | 2026-04-24 |
| Erfurt | 72 | 2026-04-24 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 60 | 2026-04-23 |
| Trier | 51 | 2026-04-24 |
| Twente | 43 | 2026-04-14 |
| Münster | 41 | 2026-04-23 |
| Potsdam Sona | 41 | 2026-04-23 |
| Dresden | 34 | 2026-04-14 |
| ULM | 34 | 2026-04-24 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 25 | 2026-04-21 |
| IPN | 24 | 2026-04-24 |
| Ipu Sona | 23 | 2026-04-21 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| LMU | 15 | 2026-04-23 |
| Göttingen | 14 | 2026-03-17 |
| Graz | 5 | 2026-04-20 |
| Bielefeld | 3 | 2026-04-21 |
| Potsdam Sona Cogscience | 3 | 2026-04-21 |
| Bochum | 0 |  |
| Bochum Prolific | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Passau | 0 |  |
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
| Since today 00:00 | 2026-04-25 | 2026-04-25 | 2.00 | HU | 1 | IU | 1 |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-04-22 | 2026-04-24 | 25.00 | Potsdam | 20 | Trier | 14 | LMU | 10 | IU | 7 | ULM | 6 | 18 |
| Last 7 days | 2026-04-18 | 2026-04-24 | 23.00 | Potsdam | 20 | IU | 18 | Trier | 18 | ULM | 16 | FU | 15 | 74 |
| Last 14 days | 2026-04-11 | 2026-04-24 | 30.71 | Frankfurt Prolific | 119 | IU | 37 | FU | 32 | Hildesheim | 28 | Trier | 28 | 186 |
| Last 30 days | 2026-03-26 | 2026-04-24 | 23.30 | Frankfurt Prolific | 209 | IU | 83 | FU | 50 | Trier | 44 | Erfurt | 38 | 275 |

<!-- END_DEMO_TABLE -->


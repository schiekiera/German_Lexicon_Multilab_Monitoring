# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2374

**Overall progress (Target: 2453 participants):**

[█████████████████████████████░] 2374 / 2453 (96.8%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 501 | 2026-04-26 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 144 | 2026-04-26 |
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
| Münster | 42 | 2026-04-23 |
| Potsdam Sona | 41 | 2026-04-23 |
| ULM | 39 | 2026-04-26 |
| Dresden | 34 | 2026-04-14 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 25 | 2026-04-21 |
| IPN | 24 | 2026-04-24 |
| Ipu Sona | 23 | 2026-04-21 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| LMU | 15 | 2026-04-23 |
| Göttingen | 14 | 2026-03-17 |
| Potsdam Sona Cogscience | 7 | 2026-04-26 |
| Graz | 5 | 2026-04-20 |
| Bielefeld | 4 | 2026-04-26 |
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
| Since today 00:00 | 2026-04-26 | 2026-04-26 | 14.00 | ULM | 5 | Potsdam Sona Cogscience | 4 | IU | 2 | Bielefeld | 1 | HU | 1 | 1 |
| Last 3 days | 2026-04-23 | 2026-04-25 | 11.67 | Trier | 8 | IU | 6 | ULM | 5 | LMU | 3 | HU | 2 | 11 |
| Last 7 days | 2026-04-19 | 2026-04-25 | 22.14 | Potsdam | 20 | Trier | 18 | IU | 17 | LMU | 15 | FU | 14 | 71 |
| Last 14 days | 2026-04-12 | 2026-04-25 | 30.14 | Frankfurt Prolific | 119 | IU | 36 | FU | 30 | Trier | 28 | Hildesheim | 25 | 184 |
| Last 30 days | 2026-03-27 | 2026-04-25 | 23.03 | Frankfurt Prolific | 209 | IU | 83 | FU | 50 | Trier | 44 | Hildesheim | 37 | 268 |

<!-- END_DEMO_TABLE -->


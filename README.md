# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2335

**Overall progress (Target: 2453 participants):**

[█████████████████████████████░] 2335 / 2453 (95.2%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 495 | 2026-04-23 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 142 | 2026-04-22 |
| FU | 124 | 2026-04-22 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 85 | 2026-04-21 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 73 | 2026-04-21 |
| Aachen | 71 | 2026-04-19 |
| Erfurt | 71 | 2026-04-21 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 59 | 2026-04-21 |
| Trier | 46 | 2026-04-23 |
| Twente | 43 | 2026-04-14 |
| Münster | 40 | 2026-04-22 |
| Potsdam Sona | 40 | 2026-04-22 |
| Dresden | 34 | 2026-04-14 |
| ULM | 30 | 2026-04-23 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 25 | 2026-04-21 |
| Ipu Sona | 23 | 2026-04-21 |
| IPN | 22 | 2026-04-21 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| LMU | 14 | 2026-04-23 |
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
| Since today 00:00 | 2026-04-23 | 2026-04-23 | 10.00 | Trier | 3 | IU | 2 | LMU | 2 | FU | 1 | HU | 1 | 1 |
| Last 3 days | 2026-04-20 | 2026-04-22 | 33.33 | Potsdam | 20 | FU | 10 | Trier | 10 | LMU | 9 | ULM | 9 | 42 |
| Last 7 days | 2026-04-16 | 2026-04-22 | 22.86 | Potsdam | 20 | Trier | 16 | FU | 15 | IU | 14 | IPN | 13 | 82 |
| Last 14 days | 2026-04-09 | 2026-04-22 | 30.71 | Frankfurt Prolific | 119 | IU | 41 | FU | 34 | Hildesheim | 34 | Trier | 23 | 179 |
| Last 30 days | 2026-03-24 | 2026-04-22 | 23.63 | Frankfurt Prolific | 209 | IU | 87 | FU | 51 | Hildesheim | 41 | Erfurt | 38 | 283 |

<!-- END_DEMO_TABLE -->


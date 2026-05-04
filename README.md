# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2459

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2459 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 145 | 2026-05-02 |
| FU | 132 | 2026-04-29 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 91 | 2026-05-04 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 78 | 2026-04-30 |
| Wuppertal | 77 | 2026-04-28 |
| Erfurt | 75 | 2026-04-30 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 61 | 2026-05-03 |
| Trier | 52 | 2026-04-27 |
| Twente | 45 | 2026-04-29 |
| Münster | 44 | 2026-05-03 |
| Potsdam Sona | 42 | 2026-04-29 |
| ULM | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 29 | 2026-05-03 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 25 | 2026-04-21 |
| Ipu Sona | 25 | 2026-04-28 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Potsdam Sona Cogscience | 16 | 2026-04-30 |
| Göttingen | 15 | 2026-04-27 |
| Graz | 12 | 2026-05-04 |
| Bielefeld | 6 | 2026-04-27 |
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
| Since today 00:00 | 2026-05-04 | 2026-05-04 | 3.00 | Graz | 1 | Ipu Sona | 1 | Mannheim Kognitive Psychologie | 1 |  |  |  |  | 0 |
| Last 3 days | 2026-05-01 | 2026-05-03 | 2.67 | Graz | 2 | IPN | 2 | HU | 1 | Hildesheim | 1 | LMU | 1 | 1 |
| Last 7 days | 2026-04-27 | 2026-05-03 | 11.71 | IU | 15 | LMU | 14 | Potsdam Sona Cogscience | 9 | FU | 8 | Graz | 6 | 30 |
| Last 14 days | 2026-04-20 | 2026-05-03 | 16.50 | IU | 31 | LMU | 26 | ULM | 22 | Potsdam | 20 | FU | 19 | 113 |
| Last 30 days | 2026-04-04 | 2026-05-03 | 19.87 | Frankfurt Prolific | 119 | IU | 76 | FU | 48 | ULM | 38 | Hildesheim | 36 | 279 |

<!-- END_DEMO_TABLE -->


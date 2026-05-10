# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2542

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2542 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 146 | 2026-05-09 |
| HU | 146 | 2026-05-07 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 92 | 2026-05-06 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 79 | 2026-05-05 |
| Erfurt | 78 | 2026-05-08 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| Trier | 52 | 2026-04-27 |
| Münster | 49 | 2026-05-10 |
| Twente | 47 | 2026-05-07 |
| ULM | 47 | 2026-05-08 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 29 | 2026-05-03 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 27 | 2026-05-07 |
| Ipu Sona | 25 | 2026-05-04 |
| Bochum Prolific | 23 | 2026-05-05 |
| Potsdam | 20 | 2026-04-22 |
| Graz | 18 | 2026-05-10 |
| Potsdam Sona Cogscience | 18 | 2026-05-05 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Zurich | 12 | 2026-05-10 |
| Bielefeld | 6 | 2026-04-27 |
| Bochum | 2 | 2026-05-08 |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Passau | 0 |  |

### Plot: Progress per lab over time

![Data collection progress per lab over time](plots/data_collection_progress.png)

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End |  M(data/day) | Rank_1 | n_1 | Rank_2 | n_2 | Rank_3 | n_3 | Rank_4 | n_4 | Rank_5 | n_5 | n_Rest |
|--------|-------|-----|----------------------|---|----|---|----|---|----|---|----|---|----|--------|
| Since today 00:00 | 2026-05-10 | 2026-05-10 | 5.00 | Graz | 3 | Münster | 1 | Zurich | 1 |  |  |  |  | 0 |
| Last 3 days | 2026-05-07 | 2026-05-09 | 8.33 | Zurich | 10 | FU | 3 | Graz | 2 | Münster | 2 | ULM | 2 | 6 |
| Last 7 days | 2026-05-03 | 2026-05-09 | 12.14 | Bochum Prolific | 23 | FU | 14 | Zurich | 11 | Münster | 5 | ULM | 5 | 27 |
| Last 14 days | 2026-04-26 | 2026-05-09 | 12.64 | Bochum Prolific | 23 | FU | 22 | IU | 17 | Potsdam Sona Cogscience | 15 | LMU | 14 | 86 |
| Last 30 days | 2026-04-10 | 2026-05-09 | 20.93 | Frankfurt Prolific | 119 | IU | 58 | FU | 56 | ULM | 39 | Hildesheim | 38 | 318 |

<!-- END_DEMO_TABLE -->


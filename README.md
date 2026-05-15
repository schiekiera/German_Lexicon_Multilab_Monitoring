# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2591

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2591 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 153 | 2026-05-14 |
| HU | 146 | 2026-05-07 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 93 | 2026-05-14 |
| Pavia | 81 | 2026-02-20 |
| Erfurt | 80 | 2026-05-14 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| Trier | 52 | 2026-04-27 |
| Münster | 51 | 2026-05-13 |
| ULM | 51 | 2026-05-14 |
| Twente | 47 | 2026-05-07 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 30 | 2026-05-11 |
| Frankfurt Sona | 29 | 2026-05-13 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Ipu Sona | 27 | 2026-05-14 |
| Zurich | 25 | 2026-05-14 |
| Bochum Prolific | 23 | 2026-05-05 |
| Graz | 23 | 2026-05-13 |
| Potsdam Sona Cogscience | 22 | 2026-05-14 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Bielefeld | 6 | 2026-04-27 |
| Bochum | 5 | 2026-05-13 |
| Lüneburg Credit | 1 | 2026-05-14 |
| Lüneburg Paid | 1 | 2026-05-12 |
| Ipu Prolific | 0 |  |
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
| Since today 00:00 | 2026-05-15 | 2026-05-15 | 0.00 |  |  |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-05-12 | 2026-05-14 | 10.00 | Zurich | 7 | FU | 5 | Potsdam Sona Cogscience | 3 | Bochum | 2 | Ipu Sona | 2 | 11 |
| Last 7 days | 2026-05-08 | 2026-05-14 | 9.71 | Zurich | 17 | FU | 10 | Graz | 10 | Münster | 5 | ULM | 5 | 21 |
| Last 14 days | 2026-05-01 | 2026-05-14 | 10.21 | Zurich | 25 | Bochum Prolific | 23 | FU | 21 | Graz | 14 | ULM | 9 | 51 |
| Last 30 days | 2026-04-15 | 2026-05-14 | 14.93 | FU | 47 | IU | 39 | ULM | 35 | LMU | 29 | Trier | 28 | 270 |

<!-- END_DEMO_TABLE -->


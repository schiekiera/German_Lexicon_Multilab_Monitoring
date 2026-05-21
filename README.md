# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2674

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2674 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 154 | 2026-05-15 |
| HU | 147 | 2026-05-17 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 94 | 2026-05-15 |
| Erfurt | 83 | 2026-05-19 |
| Pavia | 81 | 2026-02-20 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| ULM | 54 | 2026-05-20 |
| Münster | 52 | 2026-05-19 |
| Trier | 52 | 2026-04-27 |
| Twente | 47 | 2026-05-07 |
| Zurich | 43 | 2026-05-21 |
| Potsdam Sona | 42 | 2026-04-29 |
| Graz | 41 | 2026-05-20 |
| Dresden | 35 | 2026-05-20 |
| IPN | 32 | 2026-05-18 |
| Frankfurt Sona | 29 | 2026-05-13 |
| Ipu Sona | 29 | 2026-05-18 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Potsdam Sona Cogscience | 26 | 2026-05-20 |
| Bochum Prolific | 23 | 2026-05-05 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Lüneburg Credit | 15 | 2026-05-21 |
| Lüneburg Paid | 11 | 2026-05-20 |
| Bochum | 9 | 2026-05-20 |
| Bielefeld | 6 | 2026-04-27 |
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
| Since today 00:00 | 2026-05-21 | 2026-05-21 | 4.00 | Zurich | 2 | Lüneburg Credit | 1 | Lüneburg Paid | 1 |  |  |  |  | 0 |
| Last 3 days | 2026-05-18 | 2026-05-20 | 16.33 | Lüneburg Credit | 13 | Zurich | 10 | Graz | 7 | Lüneburg Paid | 7 | Potsdam Sona Cogscience | 3 | 9 |
| Last 7 days | 2026-05-14 | 2026-05-20 | 13.00 | Graz | 18 | Zurich | 17 | Lüneburg Credit | 14 | Lüneburg Paid | 9 | Potsdam Sona Cogscience | 6 | 27 |
| Last 14 days | 2026-05-07 | 2026-05-20 | 11.29 | Zurich | 40 | Graz | 28 | Lüneburg Credit | 14 | FU | 11 | Lüneburg Paid | 10 | 55 |
| Last 30 days | 2026-04-21 | 2026-05-20 | 14.17 | Zurich | 41 | FU | 36 | Graz | 36 | IU | 31 | ULM | 31 | 250 |

<!-- END_DEMO_TABLE -->


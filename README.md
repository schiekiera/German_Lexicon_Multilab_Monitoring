# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2562

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2562 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 148 | 2026-05-11 |
| HU | 146 | 2026-05-07 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 92 | 2026-05-06 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Erfurt | 79 | 2026-05-11 |
| Leipzig | 79 | 2026-05-05 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| Trier | 52 | 2026-04-27 |
| Münster | 49 | 2026-05-10 |
| ULM | 49 | 2026-05-11 |
| Twente | 47 | 2026-05-07 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 30 | 2026-05-11 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 28 | 2026-05-10 |
| Ipu Sona | 25 | 2026-05-04 |
| Bochum Prolific | 23 | 2026-05-05 |
| Graz | 22 | 2026-05-11 |
| Potsdam | 20 | 2026-04-22 |
| Potsdam Sona Cogscience | 19 | 2026-05-11 |
| Zurich | 18 | 2026-05-11 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Bielefeld | 6 | 2026-04-27 |
| Bochum | 4 | 2026-05-12 |
| Ipu Prolific | 0 |  |
| Lüneburg Credit | 0 |  |
| Lüneburg Paid | 0 |  |
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
| Since today 00:00 | 2026-05-12 | 2026-05-12 | 1.00 | Bochum | 1 |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-05-09 | 2026-05-11 | 9.67 | Zurich | 9 | Graz | 7 | FU | 4 | Münster | 2 | ULM | 2 | 5 |
| Last 7 days | 2026-05-05 | 2026-05-11 | 14.29 | Bochum Prolific | 23 | Zurich | 18 | FU | 16 | Graz | 10 | ULM | 7 | 26 |
| Last 14 days | 2026-04-28 | 2026-05-11 | 11.86 | Bochum Prolific | 23 | FU | 20 | Zurich | 18 | Graz | 17 | LMU | 13 | 75 |
| Last 30 days | 2026-04-12 | 2026-05-11 | 20.77 | Frankfurt Prolific | 119 | FU | 54 | IU | 53 | ULM | 39 | IPN | 30 | 328 |

<!-- END_DEMO_TABLE -->


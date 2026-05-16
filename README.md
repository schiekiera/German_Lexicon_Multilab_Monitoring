# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2608

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2608 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 154 | 2026-05-15 |
| HU | 146 | 2026-05-07 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 94 | 2026-05-15 |
| Erfurt | 81 | 2026-05-15 |
| Pavia | 81 | 2026-02-20 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| Trier | 52 | 2026-04-27 |
| ULM | 52 | 2026-05-15 |
| Münster | 51 | 2026-05-13 |
| Twente | 47 | 2026-05-07 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 31 | 2026-05-15 |
| Graz | 30 | 2026-05-16 |
| Frankfurt Sona | 29 | 2026-05-13 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Ipu Sona | 28 | 2026-05-15 |
| Zurich | 28 | 2026-05-16 |
| Bochum Prolific | 23 | 2026-05-05 |
| Potsdam Sona Cogscience | 22 | 2026-05-14 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Bielefeld | 6 | 2026-04-27 |
| Bochum | 6 | 2026-05-15 |
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
| Since today 00:00 | 2026-05-16 | 2026-05-16 | 3.00 | Graz | 2 | Zurich | 1 |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-05-13 | 2026-05-15 | 11.33 | Zurich | 7 | Graz | 6 | FU | 5 | Bochum | 2 | Erfurt | 2 | 12 |
| Last 7 days | 2026-05-09 | 2026-05-15 | 10.43 | Zurich | 18 | Graz | 13 | FU | 10 | ULM | 5 | Bochum | 4 | 23 |
| Last 14 days | 2026-05-02 | 2026-05-15 | 11.00 | Zurich | 27 | Bochum Prolific | 23 | FU | 22 | Graz | 17 | ULM | 10 | 55 |
| Last 30 days | 2026-04-16 | 2026-05-15 | 14.67 | FU | 46 | IU | 37 | ULM | 35 | LMU | 29 | Zurich | 27 | 266 |

<!-- END_DEMO_TABLE -->


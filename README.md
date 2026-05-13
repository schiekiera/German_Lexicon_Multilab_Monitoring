# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2578

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2578 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 149 | 2026-05-12 |
| HU | 146 | 2026-05-07 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 92 | 2026-05-06 |
| Pavia | 81 | 2026-02-20 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Erfurt | 79 | 2026-05-11 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| Trier | 52 | 2026-04-27 |
| Münster | 51 | 2026-05-13 |
| ULM | 50 | 2026-05-12 |
| Twente | 47 | 2026-05-07 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 30 | 2026-05-11 |
| Frankfurt Sona | 29 | 2026-05-13 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Ipu Sona | 26 | 2026-05-12 |
| Zurich | 24 | 2026-05-13 |
| Bochum Prolific | 23 | 2026-05-05 |
| Graz | 23 | 2026-05-13 |
| Potsdam | 20 | 2026-04-22 |
| Potsdam Sona Cogscience | 20 | 2026-05-12 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Bielefeld | 6 | 2026-04-27 |
| Bochum | 4 | 2026-05-12 |
| Lüneburg Paid | 1 | 2026-05-12 |
| Ipu Prolific | 0 |  |
| Lüneburg Credit | 0 |  |
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
| Since today 00:00 | 2026-05-13 | 2026-05-13 | 7.00 | Zurich | 4 | Frankfurt Sona | 1 | Graz | 1 | Münster | 1 |  |  | 0 |
| Last 3 days | 2026-05-10 | 2026-05-12 | 11.33 | Zurich | 9 | Graz | 7 | FU | 3 | ULM | 3 | Bochum | 2 | 10 |
| Last 7 days | 2026-05-06 | 2026-05-12 | 10.00 | Zurich | 19 | FU | 11 | Graz | 9 | ULM | 7 | Bochum | 4 | 20 |
| Last 14 days | 2026-04-29 | 2026-05-12 | 11.57 | Bochum Prolific | 23 | Zurich | 20 | FU | 19 | Graz | 17 | LMU | 13 | 70 |
| Last 30 days | 2026-04-13 | 2026-05-12 | 20.57 | Frankfurt Prolific | 119 | FU | 51 | IU | 50 | ULM | 37 | IPN | 30 | 330 |

<!-- END_DEMO_TABLE -->


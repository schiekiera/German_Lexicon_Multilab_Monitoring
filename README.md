# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2510

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2510 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 145 | 2026-05-02 |
| FU | 142 | 2026-05-06 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 92 | 2026-05-06 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 79 | 2026-05-05 |
| Erfurt | 77 | 2026-05-05 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-05 |
| Trier | 52 | 2026-04-27 |
| Münster | 46 | 2026-05-05 |
| Twente | 45 | 2026-04-29 |
| ULM | 45 | 2026-05-06 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 29 | 2026-05-03 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 26 | 2026-05-04 |
| Ipu Sona | 25 | 2026-05-04 |
| Bochum Prolific | 23 | 2026-05-05 |
| Potsdam | 20 | 2026-04-22 |
| Potsdam Sona Cogscience | 18 | 2026-05-05 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 16 | 2026-05-04 |
| Graz | 13 | 2026-05-05 |
| Bielefeld | 6 | 2026-04-27 |
| Bochum | 1 | 2026-05-06 |
| Zurich | 1 | 2026-05-05 |
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
| Since today 00:00 | 2026-05-06 | 2026-05-06 | 9.00 | FU | 4 | ULM | 2 | Bochum | 1 | Hildesheim | 1 | Mannheim Kognitive Psychologie | 1 | 0 |
| Last 3 days | 2026-05-03 | 2026-05-05 | 16.33 | Bochum Prolific | 23 | FU | 6 | Münster | 3 | Erfurt | 2 | Graz | 2 | 13 |
| Last 7 days | 2026-04-29 | 2026-05-05 | 13.14 | Bochum Prolific | 23 | LMU | 13 | FU | 8 | Graz | 8 | IU | 7 | 33 |
| Last 14 days | 2026-04-22 | 2026-05-05 | 15.57 | IU | 25 | LMU | 24 | Bochum Prolific | 23 | Potsdam | 20 | FU | 17 | 109 |
| Last 30 days | 2026-04-06 | 2026-05-05 | 20.93 | Frankfurt Prolific | 119 | IU | 70 | FU | 51 | ULM | 38 | Hildesheim | 37 | 313 |

<!-- END_DEMO_TABLE -->


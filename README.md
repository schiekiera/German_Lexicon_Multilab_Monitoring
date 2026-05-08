# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2523

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2523 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 146 | 2026-05-07 |
| FU | 143 | 2026-05-06 |
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
| Hildesheim | 63 | 2026-05-06 |
| Trier | 52 | 2026-04-27 |
| Twente | 47 | 2026-05-07 |
| Münster | 46 | 2026-05-05 |
| ULM | 46 | 2026-05-07 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| IPN | 29 | 2026-05-03 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 27 | 2026-05-07 |
| Ipu Sona | 25 | 2026-05-04 |
| Bochum Prolific | 23 | 2026-05-05 |
| Potsdam | 20 | 2026-04-22 |
| Potsdam Sona Cogscience | 18 | 2026-05-05 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 16 | 2026-05-04 |
| Graz | 13 | 2026-05-05 |
| Zurich | 8 | 2026-05-07 |
| Bielefeld | 6 | 2026-04-27 |
| Bochum | 1 | 2026-05-06 |
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
| Since today 00:00 | 2026-05-08 | 2026-05-08 | 0.00 |  |  |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-05-05 | 2026-05-07 | 20.67 | Bochum Prolific | 23 | FU | 11 | Zurich | 8 | ULM | 4 | Erfurt | 2 | 14 |
| Last 7 days | 2026-05-01 | 2026-05-07 | 10.71 | Bochum Prolific | 23 | FU | 11 | Zurich | 8 | Graz | 4 | ULM | 4 | 25 |
| Last 14 days | 2026-04-24 | 2026-05-07 | 12.93 | Bochum Prolific | 23 | IU | 20 | FU | 19 | Potsdam Sona Cogscience | 15 | ULM | 15 | 89 |
| Last 30 days | 2026-04-08 | 2026-05-07 | 21.20 | Frankfurt Prolific | 119 | IU | 67 | FU | 55 | ULM | 40 | Hildesheim | 38 | 317 |

<!-- END_DEMO_TABLE -->


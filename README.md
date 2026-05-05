# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2500

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2500 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 145 | 2026-05-02 |
| FU | 138 | 2026-05-05 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 91 | 2026-05-04 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 78 | 2026-04-30 |
| Erfurt | 77 | 2026-05-05 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 62 | 2026-05-05 |
| Trier | 52 | 2026-04-27 |
| Münster | 46 | 2026-05-05 |
| Twente | 45 | 2026-04-29 |
| ULM | 43 | 2026-05-05 |
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
| Zurich | 1 | 2026-05-05 |
| Bochum | 0 |  |
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
| Since today 00:00 | 2026-05-05 | 2026-05-05 | 39.00 | Bochum Prolific | 23 | FU | 6 | Erfurt | 2 | Münster | 2 | Potsdam Sona Cogscience | 2 | 4 |
| Last 3 days | 2026-05-02 | 2026-05-04 | 3.33 | IPN | 2 | Frankfurt Sona | 1 | Graz | 1 | Göttingen | 1 | HU | 1 | 4 |
| Last 7 days | 2026-04-28 | 2026-05-04 | 9.43 | LMU | 13 | IU | 10 | Graz | 7 | Potsdam Sona Cogscience | 5 | FU | 4 | 27 |
| Last 14 days | 2026-04-21 | 2026-05-04 | 15.43 | IU | 31 | LMU | 25 | Potsdam | 20 | ULM | 19 | Trier | 18 | 103 |
| Last 30 days | 2026-04-05 | 2026-05-04 | 19.97 | Frankfurt Prolific | 119 | IU | 75 | FU | 47 | ULM | 38 | Hildesheim | 36 | 284 |

<!-- END_DEMO_TABLE -->


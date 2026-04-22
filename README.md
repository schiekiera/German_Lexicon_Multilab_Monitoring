# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2308

**Overall progress (Target: 2453 participants):**

[████████████████████████████░░] 2308 / 2453 (94.1%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 491 | 2026-04-21 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 141 | 2026-04-22 |
| FU | 123 | 2026-04-22 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 85 | 2026-04-21 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 73 | 2026-04-21 |
| Aachen | 71 | 2026-04-19 |
| Erfurt | 71 | 2026-04-21 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 59 | 2026-04-21 |
| Trier | 43 | 2026-04-22 |
| Twente | 43 | 2026-04-14 |
| Potsdam Sona | 40 | 2026-04-22 |
| Münster | 39 | 2026-04-21 |
| Dresden | 34 | 2026-04-14 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| ULM | 29 | 2026-04-21 |
| Frankfurt Sona | 25 | 2026-04-21 |
| Ipu Sona | 23 | 2026-04-21 |
| IPN | 22 | 2026-04-21 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| Potsdam | 10 | 2026-04-22 |
| LMU | 8 | 2026-04-22 |
| Graz | 5 | 2026-04-20 |
| Bielefeld | 3 | 2026-04-21 |
| Potsdam Sona Cogscience | 3 | 2026-04-21 |
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
| Since today 00:00 | 2026-04-22 | 2026-04-22 | 25.00 | Potsdam | 10 | Trier | 6 | LMU | 3 | FU | 2 | Potsdam Sona | 2 | 2 |
| Last 3 days | 2026-04-19 | 2026-04-21 | 26.00 | FU | 11 | IU | 9 | ULM | 8 | Münster | 7 | Hildesheim | 6 | 37 |
| Last 7 days | 2026-04-15 | 2026-04-21 | 20.00 | FU | 15 | IPN | 14 | IU | 14 | Trier | 13 | Aachen | 12 | 72 |
| Last 14 days | 2026-04-08 | 2026-04-21 | 28.29 | Frankfurt Prolific | 119 | IU | 42 | Hildesheim | 34 | FU | 33 | IPN | 22 | 146 |
| Last 30 days | 2026-03-23 | 2026-04-21 | 23.00 | Frankfurt Prolific | 209 | IU | 88 | FU | 49 | Hildesheim | 42 | Hagen | 40 | 262 |

<!-- END_DEMO_TABLE -->


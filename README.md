# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2199

**Overall progress (Target: 2453 participants):**

[███████████████████████████░░░] 2199 / 2453 (89.6%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 480 | 2026-04-16 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 137 | 2026-04-17 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| FU | 109 | 2026-04-17 |
| Mannheim Kognitive Psychologie | 82 | 2026-04-16 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Erfurt | 69 | 2026-04-15 |
| Wuppertal | 69 | 2026-04-17 |
| Aachen | 68 | 2026-04-17 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 53 | 2026-04-17 |
| Twente | 43 | 2026-04-14 |
| Potsdam Sona | 35 | 2026-04-15 |
| Dresden | 34 | 2026-04-14 |
| Trier | 33 | 2026-04-17 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Ipu Sona | 21 | 2026-04-17 |
| IPN | 19 | 2026-04-18 |
| ULM | 18 | 2026-04-17 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| Graz | 4 |  |
| Bielefeld | 1 | 2026-04-16 |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Bochum | 0 |  |
| Bochum Prolific | 0 |  |
| Ipu Prolific | 0 |  |
| LMU | 0 |  |
| Lüneburg | 0 |  |
| Passau | 0 |  |
| Potsdam | 0 |  |
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
| Since today 00:00 | 2026-04-18 | 2026-04-18 | 2.00 | IPN | 2 |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-04-15 | 2026-04-17 | 18.00 | Aachen | 9 | IPN | 9 | Trier | 9 | HU | 5 | Erfurt | 3 | 19 |
| Last 7 days | 2026-04-11 | 2026-04-17 | 38.43 | Frankfurt Prolific | 119 | Hildesheim | 21 | IU | 19 | Aachen | 17 | FU | 17 | 76 |
| Last 14 days | 2026-04-04 | 2026-04-17 | 24.07 | Frankfurt Prolific | 119 | IU | 40 | Hildesheim | 28 | FU | 25 | Aachen | 17 | 108 |
| Last 30 days | 2026-03-19 | 2026-04-17 | 21.43 | Frankfurt Prolific | 209 | IU | 90 | Hagen | 48 | Hildesheim | 44 | Erfurt | 37 | 215 |

<!-- END_DEMO_TABLE -->


# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2175

**Overall progress (Target: 2453 participants):**

[███████████████████████████░░░] 2175 / 2453 (88.7%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 480 | 2026-04-16 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 133 | 2026-04-15 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| FU | 108 | 2026-04-15 |
| Mannheim Kognitive Psychologie | 82 | 2026-04-12 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Erfurt | 69 | 2026-04-15 |
| Wuppertal | 67 | 2026-04-14 |
| Aachen | 65 | 2026-04-15 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 52 | 2026-04-15 |
| Twente | 43 | 2026-04-14 |
| Potsdam Sona | 35 | 2026-04-15 |
| Dresden | 34 | 2026-04-14 |
| Münster | 32 | 2026-03-20 |
| Trier | 29 | 2026-04-15 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Ipu Sona | 19 | 2026-04-13 |
| Bamberg | 17 | 2026-01-26 |
| ULM | 17 | 2026-04-15 |
| Göttingen | 14 | 2026-03-17 |
| IPN | 13 | 2026-04-16 |
| Graz | 4 |  |
| Bielefeld | 1 | 2026-04-16 |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Bochum | 0 |  |
| Bochum Prolific | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
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
| Since today 00:00 | 2026-04-16 | 2026-04-16 | 10.00 | IPN | 4 | Trier | 2 | Bielefeld | 1 | Hildesheim | 1 | IU | 1 | 1 |
| Last 3 days | 2026-04-13 | 2026-04-15 | 70.33 | Frankfurt Prolific | 119 | Aachen | 14 | Hildesheim | 13 | IU | 13 | FU | 10 | 42 |
| Last 7 days | 2026-04-09 | 2026-04-15 | 38.57 | Frankfurt Prolific | 119 | IU | 27 | Hildesheim | 26 | FU | 19 | Aachen | 14 | 65 |
| Last 14 days | 2026-04-02 | 2026-04-15 | 23.14 | Frankfurt Prolific | 119 | IU | 43 | FU | 26 | Hildesheim | 26 | Erfurt | 16 | 94 |
| Last 30 days | 2026-03-17 | 2026-04-15 | 21.40 | Frankfurt Prolific | 209 | IU | 100 | Hagen | 56 | Hildesheim | 50 | Erfurt | 38 | 189 |

<!-- END_DEMO_TABLE -->


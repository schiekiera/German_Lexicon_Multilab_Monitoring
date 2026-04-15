# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2165

**Overall progress (Target: 2453 participants):**

[██████████████████████████░░░░] 2165 / 2453 (88.3%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 479 | 2026-04-15 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 133 | 2026-04-15 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| FU | 108 | 2026-04-15 |
| Mannheim Kognitive Psychologie | 81 | 2026-04-12 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Erfurt | 69 | 2026-04-15 |
| Wuppertal | 67 | 2026-04-14 |
| Aachen | 65 | 2026-04-15 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 51 | 2026-04-15 |
| Twente | 43 | 2026-04-14 |
| Potsdam Sona | 35 | 2026-04-15 |
| Dresden | 34 | 2026-04-14 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Trier | 27 | 2026-04-15 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Ipu Sona | 19 | 2026-04-13 |
| Bamberg | 17 | 2026-01-26 |
| ULM | 17 | 2026-04-15 |
| Göttingen | 14 | 2026-03-17 |
| IPN | 9 | 2026-04-15 |
| Graz | 4 |  |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Bielefeld | 0 |  |
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
| Since today 00:00 | 2026-04-15 | 2026-04-15 | 22.00 | Aachen | 6 | Erfurt | 3 | Trier | 3 | FU | 2 | IU | 2 | 6 |
| Last 3 days | 2026-04-12 | 2026-04-14 | 68.33 | Frankfurt Prolific | 119 | Hildesheim | 15 | IU | 14 | FU | 12 | Aachen | 8 | 37 |
| Last 7 days | 2026-04-08 | 2026-04-14 | 36.57 | Frankfurt Prolific | 119 | IU | 28 | Hildesheim | 25 | FU | 18 | ULM | 10 | 56 |
| Last 14 days | 2026-04-01 | 2026-04-14 | 22.36 | Frankfurt Prolific | 119 | IU | 43 | FU | 25 | Hildesheim | 25 | ULM | 16 | 85 |
| Last 30 days | 2026-03-16 | 2026-04-14 | 21.57 | Frankfurt Prolific | 209 | IU | 111 | Hagen | 67 | Hildesheim | 49 | Erfurt | 35 | 176 |

<!-- END_DEMO_TABLE -->


# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2350

**Overall progress (Target: 2453 participants):**

[█████████████████████████████░] 2350 / 2453 (95.8%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 496 | 2026-04-23 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 142 | 2026-04-23 |
| FU | 124 | 2026-04-23 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 86 | 2026-04-23 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 77 | 2026-04-24 |
| Wuppertal | 73 | 2026-04-21 |
| Erfurt | 72 | 2026-04-21 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 60 | 2026-04-23 |
| Trier | 50 | 2026-04-24 |
| Twente | 43 | 2026-04-14 |
| Münster | 41 | 2026-04-23 |
| Potsdam Sona | 41 | 2026-04-23 |
| Dresden | 34 | 2026-04-14 |
| ULM | 33 | 2026-04-24 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 25 | 2026-04-21 |
| Ipu Sona | 23 | 2026-04-21 |
| IPN | 22 | 2026-04-21 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| LMU | 15 | 2026-04-23 |
| Göttingen | 14 | 2026-03-17 |
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
| Since today 00:00 | 2026-04-24 | 2026-04-24 | 8.00 | Trier | 4 | ULM | 2 | Erfurt | 1 | Leipzig | 1 |  |  | 0 |
| Last 3 days | 2026-04-21 | 2026-04-23 | 32.33 | Potsdam | 20 | Trier | 12 | IU | 11 | LMU | 11 | ULM | 8 | 35 |
| Last 7 days | 2026-04-17 | 2026-04-23 | 23.29 | Potsdam | 20 | FU | 16 | IU | 16 | Trier | 16 | LMU | 15 | 80 |
| Last 14 days | 2026-04-10 | 2026-04-23 | 30.93 | Frankfurt Prolific | 119 | IU | 38 | Hildesheim | 35 | FU | 34 | Trier | 24 | 183 |
| Last 30 days | 2026-03-25 | 2026-04-23 | 23.77 | Frankfurt Prolific | 209 | IU | 88 | FU | 52 | Hildesheim | 39 | Trier | 39 | 286 |

<!-- END_DEMO_TABLE -->


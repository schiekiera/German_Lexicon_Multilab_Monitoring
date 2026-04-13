# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1974

**Overall progress (Target: 2453 participants):**

[████████████████████████░░░░░░] 1974 / 2453 (80.5%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 470 | 2026-04-13 |
| HU | 131 | 2026-04-13 |
| Hagen | 117 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| FU | 101 | 2026-04-13 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| Mannheim Kognitive Psychologie | 81 | 2026-04-12 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 66 | 2026-04-05 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Erfurt | 62 | 2026-04-10 |
| Aachen | 54 | 2026-04-13 |
| Hildesheim | 42 | 2026-04-13 |
| Twente | 42 | 2026-04-01 |
| Potsdam Sona | 33 | 2026-04-12 |
| Münster | 32 | 2026-03-20 |
| Dresden | 29 | 2026-02-07 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Trier | 23 | 2026-04-10 |
| Ipu Sona | 19 | 2026-04-13 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| ULM | 14 | 2026-04-12 |
| Graz | 4 |  |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Bielefeld | 0 |  |
| Bochum | 0 |  |
| Bochum Prolific | 0 |  |
| IPN | 0 |  |
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
| Since today 00:00 | 2026-04-13 | 2026-04-13 | 20.00 | Hildesheim | 4 | IU | 4 | Aachen | 3 | FU | 3 | Hagen | 2 | 4 |
| Last 3 days | 2026-04-10 | 2026-04-12 | 15.00 | Hildesheim | 13 | FU | 8 | IU | 8 | ULM | 5 | Mannheim Kognitive Psychologie | 3 | 8 |
| Last 7 days | 2026-04-06 | 2026-04-12 | 11.57 | IU | 20 | Hildesheim | 13 | FU | 11 | ULM | 8 | Erfurt | 6 | 23 |
| Last 14 days | 2026-03-30 | 2026-04-12 | 17.79 | Frankfurt Prolific | 90 | IU | 42 | FU | 21 | Trier | 16 | Erfurt | 15 | 65 |
| Last 30 days | 2026-03-14 | 2026-04-12 | 16.53 | IU | 107 | Frankfurt Prolific | 90 | Hagen | 83 | Hildesheim | 37 | Erfurt | 31 | 148 |

<!-- END_DEMO_TABLE -->


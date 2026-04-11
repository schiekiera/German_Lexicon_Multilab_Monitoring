# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1934

**Overall progress (Target: 2453 participants):**

[████████████████████████░░░░░░] 1934 / 2453 (78.8%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 463 | 2026-04-11 |
| HU | 130 | 2026-04-10 |
| Hagen | 114 | 2026-04-07 |
| Köln | 112 | 2026-03-15 |
| FU | 93 | 2026-04-11 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 79 | 2026-04-10 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 66 | 2026-04-05 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Erfurt | 62 | 2026-04-10 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Hildesheim | 34 | 2026-04-11 |
| Münster | 32 | 2026-03-20 |
| Potsdam Sona | 31 | 2026-04-10 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Trier | 23 | 2026-04-10 |
| Ipu Sona | 18 | 2026-04-09 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| ULM | 10 | 2026-04-10 |
| Graz | 4 |  |
| Potsdam Sona Cogscience | 1 | 2026-03-28 |
| Bielefeld | 0 |  |
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
| Since today 00:00 | 2026-04-11 | 2026-04-11 | 6.00 | Hildesheim | 2 | IU | 2 | FU | 1 | ULM | 1 |  |  | 0 |
| Last 3 days | 2026-04-08 | 2026-04-10 | 13.67 | IU | 12 | Hildesheim | 7 | Erfurt | 5 | FU | 4 | Trier | 4 | 9 |
| Last 7 days | 2026-04-04 | 2026-04-10 | 9.71 | IU | 21 | FU | 8 | Erfurt | 7 | Hildesheim | 7 | Trier | 6 | 19 |
| Last 14 days | 2026-03-28 | 2026-04-10 | 17.50 | Frankfurt Prolific | 90 | IU | 42 | Erfurt | 20 | FU | 16 | Trier | 16 | 61 |
| Last 30 days | 2026-03-12 | 2026-04-10 | 17.30 | IU | 113 | Hagen | 103 | Frankfurt Prolific | 90 | Erfurt | 31 | Hildesheim | 31 | 151 |

<!-- END_DEMO_TABLE -->


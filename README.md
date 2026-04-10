# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1919

**Overall progress (Target: 2453 participants):**

[███████████████████████░░░░░░░] 1919 / 2453 (78.2%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 460 | 2026-04-10 |
| HU | 129 | 2026-04-09 |
| Hagen | 114 | 2026-04-07 |
| Köln | 112 | 2026-03-15 |
| FU | 92 | 2026-04-10 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 79 | 2026-04-10 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 66 | 2026-04-05 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Erfurt | 61 | 2026-04-10 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Münster | 32 | 2026-03-20 |
| Hildesheim | 31 | 2026-04-10 |
| Potsdam Sona | 31 | 2026-04-10 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Trier | 23 | 2026-04-10 |
| Ipu Sona | 18 | 2026-04-09 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 14 | 2026-03-17 |
| ULM | 8 | 2026-04-09 |
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
| Since today 00:00 | 2026-04-10 | 2026-04-10 | 14.00 | Hildesheim | 6 | FU | 2 | IU | 2 | Erfurt | 1 | Mannheim Kognitive Psychologie | 1 | 2 |
| Last 3 days | 2026-04-07 | 2026-04-09 | 10.00 | IU | 10 | Trier | 5 | HU | 4 | Erfurt | 3 | FU | 3 | 5 |
| Last 7 days | 2026-04-03 | 2026-04-09 | 7.86 | IU | 21 | FU | 7 | Erfurt | 6 | Trier | 5 | ULM | 5 | 11 |
| Last 14 days | 2026-03-27 | 2026-04-09 | 17.14 | Frankfurt Prolific | 90 | IU | 42 | Erfurt | 22 | FU | 16 | Trier | 15 | 55 |
| Last 30 days | 2026-03-11 | 2026-04-09 | 17.23 | IU | 116 | Hagen | 111 | Frankfurt Prolific | 90 | Erfurt | 29 | Hildesheim | 24 | 147 |

<!-- END_DEMO_TABLE -->


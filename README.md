# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1900

**Overall progress (Target: 2453 participants):**

[███████████████████████░░░░░░░] 1900 / 2453 (77.5%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 454 | 2026-04-09 |
| HU | 129 | 2026-04-09 |
| Hagen | 114 | 2026-04-07 |
| Köln | 112 | 2026-03-15 |
| FU | 90 | 2026-04-09 |
| Frankfurt Prolific | 90 | 2026-03-31 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Mannheim Kognitive Psychologie | 78 | 2026-04-06 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 66 | 2026-04-05 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Erfurt | 59 | 2026-04-09 |
| Aachen | 51 | 2026-01-18 |
| Twente | 42 | 2026-04-01 |
| Münster | 32 | 2026-03-20 |
| Potsdam Sona | 30 | 2026-04-05 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Hildesheim | 25 | 2026-03-30 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Trier | 22 | 2026-04-09 |
| Ipu Sona | 18 | 2026-04-06 |
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
| Since today 00:00 | 2026-04-09 | 2026-04-09 | 9.00 | IU | 2 | Trier | 2 | Erfurt | 1 | FU | 1 | HU | 1 | 2 |
| Last 3 days | 2026-04-06 | 2026-04-08 | 7.33 | IU | 6 | HU | 3 | Trier | 3 | Erfurt | 2 | FU | 2 | 6 |
| Last 7 days | 2026-04-02 | 2026-04-08 | 7.71 | IU | 16 | FU | 7 | Trier | 7 | Erfurt | 5 | ULM | 5 | 14 |
| Last 14 days | 2026-03-26 | 2026-04-08 | 16.86 | Frankfurt Prolific | 90 | IU | 37 | Erfurt | 24 | FU | 15 | Trier | 13 | 57 |
| Last 30 days | 2026-03-10 | 2026-04-08 | 17.43 | IU | 116 | Hagen | 114 | Frankfurt Prolific | 90 | Erfurt | 27 | Hildesheim | 24 | 152 |

<!-- END_DEMO_TABLE -->


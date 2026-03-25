# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 1657

**Overall progress (Target: 2453 participants):**

[████████████████████░░░░░░░░░░] 1657 / 2453 (67.5%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 415 | 2026-03-25 |
| HU | 118 | 2026-03-25 |
| Köln | 112 | 2026-03-15 |
| Hagen | 106 | 2026-03-25 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| FU | 72 | 2026-03-16 |
| Mannheim Kognitive Psychologie | 70 | 2026-03-24 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Wuppertal | 63 | 2026-03-17 |
| Aachen | 51 | 2026-01-18 |
| Twente | 39 | 2026-03-19 |
| Erfurt | 34 | 2026-03-25 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Dresden | 28 | 2026-02-07 |
| Frankfurt Sona | 22 | 2026-03-25 |
| Hildesheim | 22 | 2026-03-24 |
| Potsdam Sona | 19 | 2026-03-25 |
| Bamberg | 17 | 2026-01-26 |
| Ipu Sona | 16 | 2026-02-28 |
| Göttingen | 14 | 2026-03-17 |
| Trier | 7 | 2026-03-23 |
| Graz | 4 |  |
| Frankfurt Prolific | 0 |  |
| IPN | 0 |  |
| Ipu Prolific | 0 |  |
| Lüneburg | 0 |  |
| Potsdam | 0 |  |

### Plot: Progress per lab over time

![Data collection progress per lab over time](plots/data_collection_progress.png)

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End |  M(data/day) | Rank_1 | n_1 | Rank_2 | n_2 | Rank_3 | n_3 | Rank_4 | n_4 | Rank_5 | n_5 | n_Rest |
|--------|-------|-----|----------------------|---|----|---|----|---|----|---|----|---|----|--------|
| Since today 00:00 | 2026-03-25 | 2026-03-25 | 28.00 | Hagen | 12 | IU | 7 | Graz | 4 | Erfurt | 1 | Frankfurt Sona | 1 | 3 |
| Last 3 days | 2026-03-22 | 2026-03-24 | 15.67 | Hagen | 21 | Trier | 7 | Hildesheim | 6 | IU | 6 | Mannheim Kognitive Psychologie | 3 | 4 |
| Last 7 days | 2026-03-18 | 2026-03-24 | 13.14 | Hagen | 26 | IU | 22 | Hildesheim | 20 | Trier | 7 | HU | 5 | 12 |
| Last 14 days | 2026-03-11 | 2026-03-24 | 17.21 | Hagen | 91 | IU | 66 | Hildesheim | 20 | Köln | 20 | HU | 7 | 37 |
| Last 30 days | 2026-02-23 | 2026-03-24 | 17.97 | IU | 182 | Hagen | 94 | Köln | 74 | FU | 33 | HU | 28 | 128 |

<!-- END_DEMO_TABLE -->


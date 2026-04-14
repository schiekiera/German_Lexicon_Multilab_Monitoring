# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2142

**Overall progress (Target: 2453 participants):**

[██████████████████████████░░░░] 2142 / 2453 (87.3%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 477 | 2026-04-14 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 132 | 2026-04-14 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| FU | 106 | 2026-04-14 |
| Mannheim Kognitive Psychologie | 81 | 2026-04-12 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 76 | 2026-03-04 |
| Wuppertal | 67 | 2026-04-14 |
| Erfurt | 66 | 2026-04-14 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Aachen | 59 | 2026-04-14 |
| Hildesheim | 50 | 2026-04-14 |
| Twente | 43 | 2026-04-14 |
| Dresden | 34 | 2026-04-14 |
| Potsdam Sona | 33 | 2026-04-12 |
| Münster | 32 | 2026-03-20 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Frankfurt Sona | 24 | 2026-04-06 |
| Trier | 24 | 2026-04-14 |
| Ipu Sona | 19 | 2026-04-13 |
| Bamberg | 17 | 2026-01-26 |
| ULM | 16 | 2026-04-14 |
| Göttingen | 14 | 2026-03-17 |
| IPN | 7 | 2026-04-14 |
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
| Since today 00:00 | 2026-04-14 | 2026-04-14 | 160.00 | Frankfurt Prolific | 119 | IPN | 7 | IU | 7 | Hildesheim | 6 | Aachen | 5 | 16 |
| Last 3 days | 2026-04-11 | 2026-04-13 | 18.00 | Hildesheim | 12 | FU | 9 | IU | 9 | ULM | 6 | Hagen | 5 | 13 |
| Last 7 days | 2026-04-07 | 2026-04-13 | 14.71 | IU | 22 | Hildesheim | 19 | FU | 14 | ULM | 10 | Erfurt | 6 | 32 |
| Last 14 days | 2026-03-31 | 2026-04-13 | 18.14 | Frankfurt Prolific | 88 | IU | 40 | FU | 21 | Hildesheim | 19 | ULM | 15 | 71 |
| Last 30 days | 2026-03-15 | 2026-04-13 | 17.10 | IU | 109 | Frankfurt Prolific | 90 | Hagen | 80 | Hildesheim | 43 | Erfurt | 32 | 159 |

<!-- END_DEMO_TABLE -->


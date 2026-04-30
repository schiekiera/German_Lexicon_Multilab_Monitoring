# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2445

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2445 / 2453 (99.7%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 144 | 2026-04-26 |
| FU | 132 | 2026-04-29 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 90 | 2026-04-30 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 78 | 2026-04-30 |
| Wuppertal | 77 | 2026-04-28 |
| Erfurt | 75 | 2026-04-30 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 60 | 2026-04-23 |
| Trier | 52 | 2026-04-27 |
| Twente | 45 | 2026-04-29 |
| Münster | 43 | 2026-04-27 |
| Potsdam Sona | 42 | 2026-04-29 |
| ULM | 42 | 2026-04-29 |
| Dresden | 34 | 2026-04-14 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| IPN | 27 | 2026-04-28 |
| LMU | 26 | 2026-04-30 |
| Frankfurt Sona | 25 | 2026-04-21 |
| Ipu Sona | 24 | 2026-04-28 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 15 | 2026-04-27 |
| Potsdam Sona Cogscience | 15 | 2026-04-30 |
| Graz | 9 | 2026-04-30 |
| Bielefeld | 6 | 2026-04-27 |
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
| Since today 00:00 | 2026-04-30 | 2026-04-30 | 16.00 | LMU | 10 | Graz | 2 | Erfurt | 1 | Leipzig | 1 | Mannheim Kognitive Psychologie | 1 | 1 |
| Last 3 days | 2026-04-27 | 2026-04-29 | 18.33 | IU | 15 | FU | 8 | Potsdam Sona Cogscience | 7 | IPN | 3 | ULM | 3 | 19 |
| Last 7 days | 2026-04-23 | 2026-04-29 | 14.86 | IU | 23 | ULM | 13 | Potsdam Sona Cogscience | 11 | FU | 9 | Trier | 9 | 39 |
| Last 14 days | 2026-04-16 | 2026-04-29 | 18.86 | IU | 37 | Trier | 25 | ULM | 25 | FU | 24 | Potsdam | 20 | 133 |
| Last 30 days | 2026-03-31 | 2026-04-29 | 23.37 | Frankfurt Prolific | 207 | IU | 86 | FU | 52 | Trier | 42 | ULM | 42 | 272 |

<!-- END_DEMO_TABLE -->


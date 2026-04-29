# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2416

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2416 / 2453 (98.5%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 511 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| HU | 144 | 2026-04-26 |
| FU | 130 | 2026-04-28 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 88 | 2026-04-28 |
| Pavia | 81 | 2026-02-20 |
| Tübingen | 80 | 2026-03-04 |
| Leipzig | 77 | 2026-04-24 |
| Wuppertal | 77 | 2026-04-28 |
| Erfurt | 74 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 60 | 2026-04-23 |
| Trier | 52 | 2026-04-27 |
| Münster | 43 | 2026-04-27 |
| Twente | 43 | 2026-04-14 |
| Potsdam Sona | 42 | 2026-04-23 |
| ULM | 39 | 2026-04-26 |
| Dresden | 34 | 2026-04-14 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| IPN | 27 | 2026-04-28 |
| Frankfurt Sona | 25 | 2026-04-21 |
| Ipu Sona | 24 | 2026-04-28 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| LMU | 16 | 2026-04-27 |
| Göttingen | 15 | 2026-04-27 |
| Potsdam Sona Cogscience | 14 | 2026-04-29 |
| Graz | 7 | 2026-04-29 |
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
| Since today 00:00 | 2026-04-29 | 2026-04-29 | 7.00 | Graz | 2 | IU | 2 | Potsdam Sona Cogscience | 2 | Potsdam Sona | 1 |  |  | 0 |
| Last 3 days | 2026-04-26 | 2026-04-28 | 16.33 | IU | 10 | Potsdam Sona Cogscience | 9 | FU | 6 | ULM | 5 | Bielefeld | 3 | 16 |
| Last 7 days | 2026-04-22 | 2026-04-28 | 18.00 | Potsdam | 20 | IU | 18 | Trier | 15 | LMU | 11 | ULM | 11 | 51 |
| Last 14 days | 2026-04-15 | 2026-04-28 | 19.00 | IU | 32 | Trier | 28 | FU | 24 | ULM | 23 | Potsdam | 20 | 139 |
| Last 30 days | 2026-03-30 | 2026-04-28 | 23.47 | Frankfurt Prolific | 209 | IU | 85 | FU | 53 | Trier | 45 | ULM | 39 | 273 |

<!-- END_DEMO_TABLE -->


# German Lexicon Multilab Monitoring

This repository monitors the number of datasets collected across all participating labs in the German Lexicon Project. Data are tracked by reading directory listings on the HU Berlin server.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2641

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2641 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 154 | 2026-05-15 |
| HU | 147 | 2026-05-17 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 94 | 2026-05-15 |
| Erfurt | 81 | 2026-05-15 |
| Pavia | 81 | 2026-02-20 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| ULM | 53 | 2026-05-18 |
| Trier | 52 | 2026-04-27 |
| Münster | 51 | 2026-05-13 |
| Twente | 47 | 2026-05-07 |
| Potsdam Sona | 42 | 2026-04-29 |
| Graz | 39 | 2026-05-18 |
| Zurich | 36 | 2026-05-18 |
| Dresden | 34 | 2026-04-14 |
| IPN | 32 | 2026-05-18 |
| Frankfurt Sona | 29 | 2026-05-13 |
| Ipu Sona | 29 | 2026-05-18 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Bochum Prolific | 23 | 2026-05-05 |
| Potsdam Sona Cogscience | 23 | 2026-05-16 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Bochum | 8 | 2026-05-17 |
| Bielefeld | 6 | 2026-04-27 |
| Lüneburg Credit | 6 | 2026-05-18 |
| Lüneburg Paid | 5 | 2026-05-18 |
| Ipu Prolific | 0 |  |
| Passau | 0 |  |

### Plot: Progress per lab over time

![Data collection progress per lab over time](plots/data_collection_progress.png)

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End |  M(data/day) | Rank_1 | n_1 | Rank_2 | n_2 | Rank_3 | n_3 | Rank_4 | n_4 | Rank_5 | n_5 | n_Rest |
|--------|-------|-----|----------------------|---|----|---|----|---|----|---|----|---|----|--------|
| Since today 00:00 | 2026-05-19 | 2026-05-19 | 1.00 | Zurich | 1 |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-05-16 | 2026-05-18 | 11.67 | Graz | 11 | Zurich | 8 | Lüneburg Credit | 5 | Lüneburg Paid | 4 | Bochum | 2 | 5 |
| Last 7 days | 2026-05-12 | 2026-05-18 | 11.29 | Graz | 17 | Zurich | 17 | FU | 6 | Lüneburg Credit | 6 | Bochum | 5 | 28 |
| Last 14 days | 2026-05-05 | 2026-05-18 | 12.79 | Zurich | 35 | Graz | 27 | Bochum Prolific | 23 | FU | 22 | ULM | 11 | 61 |
| Last 30 days | 2026-04-19 | 2026-05-18 | 14.50 | FU | 44 | Graz | 35 | Zurich | 35 | IU | 34 | ULM | 33 | 254 |

<!-- END_DEMO_TABLE -->


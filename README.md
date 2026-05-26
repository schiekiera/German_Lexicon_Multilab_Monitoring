# German Lexicon Multilab Monitoring

This repository monitors data collection progress across all participating labs in the [German Lexicon Project](https://github.com/petrenca/German_Lexicon_Project). Dataset counts are derived from directory listings on the HU Berlin server, and data collection runs through **May 31, 2026**.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2708

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2708 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 154 | 2026-05-15 |
| HU | 148 | 2026-05-22 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 94 | 2026-05-15 |
| Erfurt | 86 | 2026-05-25 |
| Pavia | 81 | 2026-02-20 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| ULM | 54 | 2026-05-20 |
| Münster | 52 | 2026-05-19 |
| Trier | 52 | 2026-04-27 |
| Zurich | 50 | 2026-05-24 |
| Twente | 47 | 2026-05-07 |
| Graz | 43 | 2026-05-21 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 36 | 2026-05-21 |
| IPN | 32 | 2026-05-18 |
| LMU | 31 | 2026-05-23 |
| Frankfurt Sona | 30 | 2026-05-23 |
| Ipu Sona | 30 | 2026-05-23 |
| Potsdam Sona Cogscience | 30 | 2026-05-25 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Bochum Prolific | 23 | 2026-05-05 |
| Lüneburg Credit | 21 | 2026-05-25 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Lüneburg Paid | 15 | 2026-05-23 |
| Bochum | 11 | 2026-05-25 |
| Bielefeld | 6 | 2026-04-27 |
| Ipu Prolific | 0 |  |
| Passau | 0 |  |

### Plot: Overall progress over time

![Overall data collection progress over time](plots/overall_progress.png)

### Plot: New datasets collected per day

![New datasets collected per day](plots/new_datasets_per_day.png)

### Table: Average new datasets per day (rolling windows)

| Window | Start | End |  M(data/day) | Rank_1 | n_1 | Rank_2 | n_2 | Rank_3 | n_3 | Rank_4 | n_4 | Rank_5 | n_5 | n_Rest |
|--------|-------|-----|----------------------|---|----|---|----|---|----|---|----|---|----|--------|
| Since today 00:00 | 2026-05-26 | 2026-05-26 | 0.00 |  |  |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-05-23 | 2026-05-25 | 5.33 | Potsdam Sona Cogscience | 4 | Bochum | 2 | LMU | 2 | Lüneburg Credit | 2 | Zurich | 2 | 4 |
| Last 7 days | 2026-05-19 | 2026-05-25 | 9.71 | Lüneburg Credit | 15 | Zurich | 15 | Lüneburg Paid | 10 | Potsdam Sona Cogscience | 7 | Erfurt | 5 | 16 |
| Last 14 days | 2026-05-12 | 2026-05-25 | 10.50 | Zurich | 32 | Graz | 21 | Lüneburg Credit | 21 | Lüneburg Paid | 15 | Potsdam Sona Cogscience | 11 | 47 |
| Last 30 days | 2026-04-26 | 2026-05-25 | 11.60 | Zurich | 50 | Graz | 38 | FU | 30 | Potsdam Sona Cogscience | 27 | Bochum Prolific | 23 | 180 |

<!-- END_DEMO_TABLE -->


# German Lexicon Multilab Monitoring

This repository monitors data collection progress across all participating labs in the [German Lexicon Project](https://github.com/petrenca/German_Lexicon_Project). Dataset counts are derived from directory listings on the HU Berlin server, and data collection runs through **May 31, 2026**.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2752

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2752 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 154 | 2026-05-15 |
| HU | 150 | 2026-05-27 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 94 | 2026-05-15 |
| Erfurt | 87 | 2026-05-27 |
| Pavia | 81 | 2026-02-20 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Zurich | 65 | 2026-05-28 |
| Hildesheim | 63 | 2026-05-06 |
| ULM | 55 | 2026-05-26 |
| Münster | 52 | 2026-05-19 |
| Trier | 52 | 2026-04-27 |
| Twente | 47 | 2026-05-07 |
| Graz | 43 | 2026-05-21 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 36 | 2026-05-21 |
| LMU | 36 | 2026-05-26 |
| IPN | 32 | 2026-05-18 |
| Ipu Sona | 32 | 2026-05-26 |
| Frankfurt Sona | 31 | 2026-05-27 |
| Potsdam Sona Cogscience | 31 | 2026-05-28 |
| Lüneburg Credit | 30 | 2026-05-28 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Bochum Prolific | 23 | 2026-05-05 |
| Lüneburg Paid | 22 | 2026-05-28 |
| Potsdam | 20 | 2026-04-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
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
| Since today 00:00 | 2026-05-28 | 2026-05-28 | 17.00 | Lüneburg Credit | 6 | Zurich | 6 | Lüneburg Paid | 3 | LMU | 1 | Potsdam Sona Cogscience | 1 | 0 |
| Last 3 days | 2026-05-25 | 2026-05-27 | 10.67 | Zurich | 9 | LMU | 4 | Lüneburg Credit | 4 | Lüneburg Paid | 4 | Bochum | 2 | 9 |
| Last 7 days | 2026-05-21 | 2026-05-27 | 9.29 | Zurich | 18 | Lüneburg Credit | 10 | Lüneburg Paid | 9 | LMU | 6 | Erfurt | 4 | 18 |
| Last 14 days | 2026-05-14 | 2026-05-27 | 11.14 | Zurich | 35 | Lüneburg Credit | 24 | Graz | 20 | Lüneburg Paid | 18 | Potsdam Sona Cogscience | 10 | 49 |
| Last 30 days | 2026-04-28 | 2026-05-27 | 11.33 | Zurich | 59 | Graz | 38 | FU | 26 | Lüneburg Credit | 24 | Bochum Prolific | 23 | 170 |

<!-- END_DEMO_TABLE -->


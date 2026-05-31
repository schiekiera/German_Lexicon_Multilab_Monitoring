# German Lexicon Multilab Monitoring

This repository monitors data collection progress across all participating labs in the [German Lexicon Project](https://github.com/petrenca/German_Lexicon_Project). Dataset counts are derived from directory listings on the HU Berlin server, and data collection runs through **May 31, 2026**.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2829

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2829 / 2453 (100.0%)

### Table: Progress per lab

| Lab | *n* (Participants) | Last update (day) |
|-----|----------------------|-------------------|
| IU | 516 | 2026-04-29 |
| Frankfurt Prolific | 209 | 2026-04-14 |
| FU | 154 | 2026-05-15 |
| HU | 151 | 2026-05-29 |
| Hagen | 119 | 2026-04-13 |
| Köln | 112 | 2026-03-15 |
| Mannheim Kognitive Psychologie | 94 | 2026-05-15 |
| Zurich | 92 | 2026-05-31 |
| Erfurt | 89 | 2026-05-31 |
| Pavia | 81 | 2026-02-20 |
| Leipzig | 80 | 2026-05-12 |
| Tübingen | 80 | 2026-03-04 |
| Wuppertal | 77 | 2026-04-28 |
| Aachen | 71 | 2026-04-19 |
| Darmstadt | 65 | 2026-02-06 |
| Marburg | 65 | 2026-01-18 |
| Hildesheim | 63 | 2026-05-06 |
| LMU | 56 | 2026-05-31 |
| ULM | 56 | 2026-05-30 |
| Münster | 52 | 2026-05-19 |
| Trier | 52 | 2026-04-27 |
| Twente | 47 | 2026-05-07 |
| Graz | 45 | 2026-05-29 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 36 | 2026-05-21 |
| Lüneburg Credit | 36 | 2026-05-31 |
| Potsdam Sona Cogscience | 36 | 2026-05-31 |
| Ipu Sona | 34 | 2026-05-30 |
| Frankfurt Sona | 32 | 2026-05-27 |
| IPN | 32 | 2026-05-18 |
| Lüneburg Paid | 32 | 2026-05-31 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Bochum Prolific | 23 | 2026-05-05 |
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
| Since today 00:00 | 2026-05-31 | 2026-05-31 | 22.00 | Zurich | 9 | Potsdam Sona Cogscience | 5 | Lüneburg Paid | 3 | LMU | 2 | Erfurt | 1 | 2 |
| Last 3 days | 2026-05-28 | 2026-05-30 | 24.00 | Zurich | 24 | LMU | 19 | Lüneburg Credit | 11 | Lüneburg Paid | 10 | Graz | 2 | 6 |
| Last 7 days | 2026-05-24 | 2026-05-30 | 15.43 | Zurich | 34 | LMU | 23 | Lüneburg Credit | 16 | Lüneburg Paid | 14 | Ipu Sona | 4 | 17 |
| Last 14 days | 2026-05-17 | 2026-05-30 | 13.57 | Zurich | 54 | Lüneburg Credit | 34 | Lüneburg Paid | 26 | LMU | 25 | Graz | 11 | 40 |
| Last 30 days | 2026-05-01 | 2026-05-30 | 11.97 | Zurich | 83 | Graz | 36 | Lüneburg Credit | 35 | Lüneburg Paid | 29 | LMU | 26 | 150 |

<!-- END_DEMO_TABLE -->


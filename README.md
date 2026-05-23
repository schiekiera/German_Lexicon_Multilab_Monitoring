# German Lexicon Multilab Monitoring

This repository monitors data collection progress across all participating labs in the [German Lexicon Project](https://github.com/petrenca/German_Lexicon_Project). Dataset counts are derived from directory listings on the HU Berlin server, and data collection runs through **May 31, 2026**.

## Automated output

The following output is updated automatically every 10 minutes using GitHub Actions.

<!-- START_DEMO_TABLE -->

### Overall progress

**Total data files saved across all labs:** 2692

**Overall progress (Target: 2453 participants):**

[██████████████████████████████] 2692 / 2453 (100.0%)

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
| Erfurt | 85 | 2026-05-22 |
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
| Zurich | 48 | 2026-05-22 |
| Twente | 47 | 2026-05-07 |
| Graz | 43 | 2026-05-21 |
| Potsdam Sona | 42 | 2026-04-29 |
| Dresden | 36 | 2026-05-21 |
| IPN | 32 | 2026-05-18 |
| Frankfurt Sona | 29 | 2026-05-13 |
| Ipu Sona | 29 | 2026-05-18 |
| LMU | 29 | 2026-05-01 |
| Tübingen Not Sona | 29 | 2026-02-21 |
| Potsdam Sona Cogscience | 26 | 2026-05-20 |
| Bochum Prolific | 23 | 2026-05-05 |
| Potsdam | 20 | 2026-04-22 |
| Lüneburg Credit | 19 | 2026-05-22 |
| Bamberg | 17 | 2026-01-26 |
| Göttingen | 17 | 2026-05-08 |
| Lüneburg Paid | 14 | 2026-05-21 |
| Bochum | 9 | 2026-05-20 |
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
| Since today 00:00 | 2026-05-23 | 2026-05-23 | 0.00 |  |  |  |  |  |  |  |  |  |  | 0 |
| Last 3 days | 2026-05-20 | 2026-05-22 | 12.33 | Zurich | 10 | Lüneburg Paid | 7 | Lüneburg Credit | 6 | Graz | 4 | Potsdam Sona Cogscience | 3 | 7 |
| Last 7 days | 2026-05-16 | 2026-05-22 | 12.43 | Zurich | 21 | Lüneburg Credit | 18 | Graz | 15 | Lüneburg Paid | 13 | Erfurt | 4 | 16 |
| Last 14 days | 2026-05-09 | 2026-05-22 | 11.43 | Zurich | 39 | Graz | 28 | Lüneburg Credit | 19 | Lüneburg Paid | 14 | FU | 10 | 50 |
| Last 30 days | 2026-04-23 | 2026-05-22 | 12.23 | Zurich | 48 | Graz | 38 | FU | 31 | ULM | 25 | Bochum Prolific | 23 | 202 |

<!-- END_DEMO_TABLE -->


import requests
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE_URL = "https://amor.cms.hu-berlin.de/~petrenal/GermanLexiconProject/jspsych.8.2.1/data_collection_progress/"
MAPPING_URL = "https://raw.githubusercontent.com/petrenca/German_Lexicon_Project/refs/heads/main/consent_forms/combined_mapping.json"
TARGET_TOTAL_DEMO = 1440  # Gesamtziel für DEMO-Dateien

README_PATH = Path("README.md")
LATEST_CSV_PATH = Path("demo_counts_latest.csv")
HISTORY_CSV_PATH = Path("demo_counts_history.csv")
TABLE_MD_PATH = Path("demo_counts_table.md")
PLOTS_DIR = Path("plots")
PROGRESS_PLOT_PATH = PLOTS_DIR / "data_collection_progress.png"
OVERALL_PLOT_PATH = PLOTS_DIR / "overall_progress.png"

MARKER_START = "<!-- START_DEMO_TABLE -->"
MARKER_END = "<!-- END_DEMO_TABLE -->"


def clean_uni_label(uni_key):
    """
    Cosmetic transformation for display:
    - replace '_' with ' '
    - Title Case for names > 3 letters
    - ALL CAPS for 2–3 letter codes
    """
    label = uni_key.replace("_", " ").strip()

    label = label.replace("ue", "ü").strip()
    label = label.replace("ae", "ä").strip()
    label = label.replace("oe", "ö").strip()

    if len(label) <= 3:
        return label.upper()
    
    

    # Title case for longer words
    return label.title()


def abbreviate_plot_label(label):
    """
    Abbreviate words after the first one for plot legends.
    Example: "Mannheim Kognitive Psychologie" -> "Mannheim (KP)"
    """
    parts = label.split()
    if len(parts) <= 1:
        return label
    first = parts[0]
    abbrev = "".join(p[0] for p in parts[1:] if p)
    return f"{first} ({abbrev})"

def get_unis():
    """Lädt combined_mapping.json und gibt alle Keys außer 'default' zurück."""
    resp = requests.get(MAPPING_URL)
    resp.raise_for_status()
    mapping = resp.json()
    return [k for k in mapping.keys() if k != "default"]


def list_files_for_uni(uni_key):
    """
    Ruft das Verzeichnis-Listing für eine Uni ab und versucht,
    alle Dateinamen herauszuziehen, die mit glp_ anfangen.
    """
    url = f"{BASE_URL}{uni_key}/"
    resp = requests.get(url)
    if resp.status_code == 404:
        # Ordner existiert (noch) nicht
        return []
    resp.raise_for_status()
    html = resp.text

    files = []
    for line in html.splitlines():
        if "glp_" in line and ".txt" in line:
            start = line.find("glp_")
            end = line.find(".txt", start)
            if start != -1 and end != -1:
                filename = line[start:end + 4]  # inkl. ".txt"
                files.append(filename)
    return files


def count_demo_files(files):
    """Zählt alle Dateien, die 'demo' im Namen enthalten."""
    return sum(1 for f in files if "demo" in f)


def write_latest_csv(rows):
    """Schreibt demo_counts_latest.csv (aktuelle Übersicht)."""
    with LATEST_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["uni", "n_participants"])
        writer.writeheader()
        writer.writerows(rows)


def append_history_csv(rows, timestamp):
    """Hängt die aktuellen Counts an demo_counts_history.csv an."""
    new_file = not HISTORY_CSV_PATH.exists()
    with HISTORY_CSV_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "uni", "n_participants"])
        for r in rows:
            writer.writerow([timestamp, r["uni"], r["n_participants"]])


def make_markdown_table(rows):
    """Erzeugt eine Markdown-Tabelle aus den Rows.

    Sortierung:
    - zuerst nach n_participants (absteigend)
    - dann alphabetisch nach uni (aufsteigend)
    """
    rows_sorted = sorted(
        rows,
        key=lambda r: (-r["n_participants"], r["uni"])
    )

    header = "| Lab | *n* (Participants) |\n|-----|----------------------|\n"
    body_lines = [
        f"| {r['uni']} | {r['n_participants']} |"
        for r in rows_sorted
    ]
    return header + "\n".join(body_lines) + "\n"


def make_progress_bar(current, total, bar_length=30):
    """
    Erzeugt eine einfache Text-Fortschrittsleiste für Markdown.

    Beispiel:
    [██████████░░░░░░░░░░░░░░] 300 / 1440 (20.8%)
    """
    if total <= 0:
        return ""
    ratio = max(0.0, min(float(current) / float(total), 1.0))
    filled_len = int(round(bar_length * ratio))
    bar = "█" * filled_len + "░" * (bar_length - filled_len)
    percent = ratio * 100
    return f"[{bar}] {current} / {total} ({percent:.1f}%)"


def make_readme_section(rows, target_total=TARGET_TOTAL_DEMO):
    """
    Baut den Markdown-Block für die README:
    - Tabelle pro Uni
    - Gesamtsumme aller DEMO-Dateien
    - Gesamter Fortschritt als Fortschrittsbalken
    """
    total_current = sum(r["n_participants"] for r in rows)
    table_md = make_markdown_table(rows).rstrip()
    progress_bar = make_progress_bar(total_current, target_total)

    parts = [
        "### Overall progress",
        "",
        f"**Total data files saved across all labs:** {total_current}",
        "",
        f"**Overall progress (Target: {target_total} participants):**",
        "",
        progress_bar,
        "",
        "### Table: Progress per lab",
        "",
        table_md,
        "",
        "### Plot: Progress per lab over time",
        "",
        "![Data collection progress per lab over time](plots/data_collection_progress.png)",
        "",
        "### Plot: Overall progress over time",
        "",
        "![Overall data collection progress over time](plots/overall_progress.png)",
        "",
    ]

    return "\n".join(parts)


def create_progress_plot():
    """
    Erzeugt ein Liniendiagramm-PNG der Entwicklung der Teilnehmerzahlen
    pro Labor über die Zeit und speichert es unter
    plots/data_collection_progress.png.

    Logik (angelehnt an das Plotly-Skript):
    - liest demo_counts_history.csv
    - bestimmt den neuesten Zeitstempel
    - wählt nur Labs mit >= 1 Teilnehmer beim neuesten Zeitstempel
    - aggregiert pro Tag und Lab den letzten Stand dieses Tages
    - plottet Linien pro Lab über die Zeit
    """
    if not HISTORY_CSV_PATH.exists():
        return

    PLOTS_DIR.mkdir(exist_ok=True)

    # --- Daten einlesen ---
    records = []
    with HISTORY_CSV_PATH.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Überschriftenzeile überspringen
        for row in reader:
            if len(row) < 3:
                continue
            ts_str, uni, count_str = row[0], row[1], row[2]
            try:
                count = int(count_str)
            except ValueError:
                continue
            try:
                ts = datetime.strptime(ts_str, "%Y-%m-%dT%H-%M-%SZ")
            except ValueError:
                # Falls das Format sich einmal ändert, den Eintrag überspringen
                continue
            records.append({"timestamp": ts, "uni": uni, "count": count})

    if not records:
        return

    # --- aktive Labs (mit >= 1 Teilnehmer beim neuesten Zeitstempel) bestimmen ---
    latest_ts = max(r["timestamp"] for r in records)
    active_labs = {
        r["uni"]
        for r in records
        if r["timestamp"] == latest_ts and r["count"] >= 1
    }

    if not active_labs:
        return

    # Nur Datensätze der aktiven Labs verwenden
    active_records = [r for r in records if r["uni"] in active_labs]

    # --- tägliche Aggregation: pro Tag/Lab den letzten Stand des Tages ---
    per_lab_daily = defaultdict(dict)  # uni -> {date -> (timestamp, count)}
    for r in active_records:
        d = r["timestamp"].date()
        cur = per_lab_daily[r["uni"]].get(d)
        if cur is None or r["timestamp"] > cur[0]:
            per_lab_daily[r["uni"]][d] = (r["timestamp"], r["count"])

    # --- Plotten ---
    plt.figure(figsize=(10, 5), dpi=200)
    labs_sorted = sorted(per_lab_daily.keys())
    cmap = plt.cm.get_cmap("tab20", len(labs_sorted))

    for idx, uni in enumerate(labs_sorted):
        items = sorted(per_lab_daily[uni].items(), key=lambda x: x[0])
        dates = [d for d, _ in items]
        counts = [cnt for _, (_, cnt) in items]
        plt.plot(
            dates,
            counts,
            linewidth=2,
            label=abbreviate_plot_label(uni),
            color=cmap(idx),
        )

    plt.xlabel("Date")
    plt.ylabel("Number of participants")
    plt.grid(True, alpha=0.3)
    plt.gcf().autofmt_xdate()
    plt.legend(title="Lab", fontsize="small", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()

    plt.savefig(PROGRESS_PLOT_PATH, dpi=300)
    plt.close()

    # --- Zweiter Plot: Gesamtfortschritt ---
    # Wir berechnen die Tagessumme über alle aktiven Labs
    all_dates = sorted({d for lab_data in per_lab_daily.values() for d in lab_data.keys()})
    total_daily = {}
    
    for d in all_dates:
        day_total = 0
        for uni in active_labs:
            # Suche den neuesten Stand für diese Uni an oder vor diesem Tag
            lab_history = per_lab_daily[uni]
            past_dates = [ud for ud in lab_history.keys() if ud <= d]
            if past_dates:
                latest_ud = max(past_dates)
                day_total += lab_history[latest_ud][1]
        total_daily[d] = day_total

    plt.figure(figsize=(10, 5), dpi=200)
    items = sorted(total_daily.items())
    dates = [d for d, _ in items]
    counts = [cnt for _, cnt in items]
    
    plt.plot(dates, counts, marker="o", linewidth=3, color="#2c3e50", label="Total Progress")

    plt.xlabel("Date")
    plt.ylabel("Total participants")
    plt.title("Overall Data Collection Progress")
    plt.grid(True, alpha=0.3)
    plt.gcf().autofmt_xdate()
    plt.legend(loc="upper left")
    plt.tight_layout()

    plt.savefig(OVERALL_PLOT_PATH, dpi=300)
    plt.close()


def compact_history_csv():
    """
    Komprimiert demo_counts_history.csv, indem pro (Tag, Labor)
    nur der Eintrag mit dem neuesten Zeitstempel erhalten bleibt.

    Das hält die Datei klein, ohne die tägliche Verlaufinformation
    zu verlieren. Format und Spalten bleiben unverändert.
    """
    if not HISTORY_CSV_PATH.exists():
        return

    with HISTORY_CSV_PATH.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return

        # key: (uni, date) -> (timestamp_datetime, original_row)
        best_per_day = {}

        for row in reader:
            if len(row) < 3:
                continue
            ts_str, uni, count_str = row[0], row[1], row[2]
            try:
                ts = datetime.strptime(ts_str, "%Y-%m-%dT%H-%M-%SZ")
            except ValueError:
                # Fallback für ggf. anderes Format
                try:
                    ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                except Exception:
                    continue

            key = (uni, ts.date())
            current_best = best_per_day.get(key)
            if current_best is None or ts > current_best[0]:
                best_per_day[key] = (ts, [ts_str, uni, count_str])

    if not best_per_day:
        return

    # Sortiert nach Datum/Zeit, damit die Datei weiterhin chronologisch ist
    compacted_rows = sorted(best_per_day.values(), key=lambda x: x[0])

    with HISTORY_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for _ts, row in compacted_rows:
            writer.writerow(row)


def write_table_md(table_md):
    """Schreibt die Tabelle in eine eigene Markdown-Datei."""
    TABLE_MD_PATH.write_text(table_md, encoding="utf-8")


def update_readme(content_md):
    """
    Aktualisiert README.md:
    - Wenn README.md existiert und Marker vorhanden sind, ersetze den Block dazwischen.
    - Wenn README.md existiert, aber Marker fehlen, hänge einen Abschnitt mit Markern an.
    - Wenn README.md nicht existiert, erstelle eine minimale README mit Markern.
    """
    if README_PATH.exists():
        text = README_PATH.read_text(encoding="utf-8")
        if MARKER_START in text and MARKER_END in text:
            # Block ersetzen
            before, rest = text.split(MARKER_START, 1)
            _, after = rest.split(MARKER_END, 1)
            new_block = (
                f"{MARKER_START}\n\n"
                f"{content_md}\n"
                f"{MARKER_END}"
            )
            new_text = before.rstrip() + "\n\n" + new_block + "\n\n" + after.lstrip()
        else:
            # Marker noch nicht vorhanden → am Ende anhängen
            new_block = (
                "\n\n## Aktueller Stand der DEMO-Datensätze\n\n"
                f"{MARKER_START}\n\n"
                f"{content_md}\n"
                f"{MARKER_END}\n"
            )
            new_text = text.rstrip() + new_block
        README_PATH.write_text(new_text, encoding="utf-8")
    else:
        # README existiert nicht → neue, minimale README
        new_text = (
            "# German Lexicon Multilab Monitoring\n\n"
            "Dieses Repository trackt automatisiert die Anzahl an DEMO-Datensätzen pro Universität.\n\n"
            "## Aktueller Stand der DEMO-Datensätze\n\n"
            f"{MARKER_START}\n\n"
            f"{content_md}\n"
            f"{MARKER_END}\n"
        )
        README_PATH.write_text(new_text, encoding="utf-8")


def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
    unis = get_unis()

    rows = []
    for uni in unis:
        files = list_files_for_uni(uni)
        n_demo = count_demo_files(files)
        rows.append({"uni": clean_uni_label(uni), "n_participants": n_demo})

    # CSVs
    write_latest_csv(rows)
    append_history_csv(rows, timestamp)

    # Verlaufshistorie komprimieren (pro Tag/Lab nur letzter Stand)
    compact_history_csv()

    # Markdown-Tabelle erzeugen
    table_md = make_markdown_table(rows)
    write_table_md(table_md)

    # Liniendiagramm der Gesamtentwicklung erzeugen
    create_progress_plot()

    # README-Inhalt (Tabelle + Gesamtsumme + Fortschrittsbalken + Plot) erzeugen
    readme_section_md = make_readme_section(rows, TARGET_TOTAL_DEMO)
    update_readme(readme_section_md)


if __name__ == "__main__":
    main()
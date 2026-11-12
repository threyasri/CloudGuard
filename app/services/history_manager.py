import csv
import os

from app.config import Config


FIELDNAMES = [
    "Timestamp",
    "CPU Usage",
    "Memory Usage",
    "Status"
]


def initialize_history():
    """Create the monitoring history file if it does not exist."""

    file_exists = (
        os.path.exists(Config.HISTORY_FILE)
        and os.path.getsize(Config.HISTORY_FILE) > 0
    )

    if not file_exists:
        with open(Config.HISTORY_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def save_metrics(metrics, status):
    """Save a monitoring record to CSV."""

    initialize_history()

    record = {
        "Timestamp": metrics["timestamp"],
        "CPU Usage": metrics["cpu_usage"],
        "Memory Usage": metrics["memory_usage"],
        "Status": status
    }

    with open(Config.HISTORY_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(record)


def get_recent_history(limit=20):
    """Return the most recent monitoring records."""

    initialize_history()

    with open(Config.HISTORY_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    return records[-limit:][::-1]

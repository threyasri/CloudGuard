from flask import Blueprint, render_template

from app.config import Config


logs_bp = Blueprint("logs", __name__)


@logs_bp.route("/logs")
def event_logs():
    """Display recent CloudGuard application logs."""

    try:
        with open(Config.LOG_FILE, "r") as log_file:
            records = log_file.readlines()[-100:][::-1]

    except FileNotFoundError:
        records = []

    return render_template(
        "logs.html",
        records=records
    )

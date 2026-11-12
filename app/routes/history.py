from flask import Blueprint, render_template

from app.services.history_manager import get_recent_history


history_bp = Blueprint("history", __name__)


@history_bp.route("/history")
def monitoring_history():
    """Display recent system monitoring records."""

    records = get_recent_history(limit=50)

    return render_template(
        "history.html",
        records=records
    )

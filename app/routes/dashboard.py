from flask import Blueprint, render_template

from app.config import Config
from app.services.metrics_collector import collect_system_metrics
from app.services.incident_manager import detect_incidents
from app.services.application_state import application_state


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def overview():
    """Render the CloudGuard infrastructure dashboard."""

    metrics = collect_system_metrics()

    status = "FAILED" if application_state.is_failed else "RUNNING"

    incidents = detect_incidents(metrics, status)

    return render_template(
        "dashboard.html",
        metrics=metrics,
        status=status,
        incidents=incidents,
        cpu_limit=Config.CPU_LIMIT,
        memory_limit=Config.MEMORY_LIMIT
    )

from flask import Blueprint, jsonify

from app.services.metrics_collector import collect_system_metrics
from app.services.incident_manager import detect_incidents
from app.services.application_state import application_state


monitoring_bp = Blueprint("monitoring", __name__)


@monitoring_bp.route("/api/metrics", methods=["GET"])
def get_metrics():
    """Return current system metrics and detected incidents."""

    metrics = collect_system_metrics()

    status = "FAILED" if application_state.is_failed else "RUNNING"

    incidents = detect_incidents(metrics, status)

    return jsonify({
        "success": True,
        "status": status,
        "data": metrics,
        "incidents": incidents
    }), 200


@monitoring_bp.route("/api/health", methods=["GET"])
def get_health():
    """Return the current application health."""

    if application_state.is_failed:
        return jsonify({
            "success": False,
            "status": "unhealthy",
            "service": "CloudGuard Monitoring API"
        }), 503

    return jsonify({
        "success": True,
        "status": "healthy",
        "service": "CloudGuard Monitoring API"
    }), 200

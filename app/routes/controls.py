from flask import Blueprint, redirect, url_for

from app.services.application_state import application_state


controls_bp = Blueprint("controls", __name__)


@controls_bp.route("/simulate-failure", methods=["POST"])
def simulate_failure():
    """Simulate an application failure."""

    application_state.simulate_failure()

    return redirect(url_for("dashboard.overview"))


@controls_bp.route("/recover", methods=["POST"])
def recover_application():
    """Recover the application from a simulated failure."""

    application_state.recover()

    return redirect(url_for("dashboard.overview"))

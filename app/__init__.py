from flask import Flask

from app.config import Config
from app.routes.monitoring import monitoring_bp
from app.routes.dashboard import dashboard_bp
from app.routes.controls import controls_bp
from app.routes.history import history_bp
from app.routes.logs import logs_bp

def create_app():
    """Create and configure the CloudGuard Flask application."""

    application = Flask(__name__)

    application.config.from_object(Config)


    # Register application routes
    application.register_blueprint(monitoring_bp)
    application.register_blueprint(dashboard_bp)
    application.register_blueprint(controls_bp)
    application.register_blueprint(history_bp)
    application.register_blueprint(logs_bp)

    return application

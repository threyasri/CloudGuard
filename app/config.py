import os


class Config:
    """Central configuration for CloudGuard."""

    # Application settings
    APP_NAME = "CloudGuard"
    DEBUG = False

    # Monitoring thresholds
    CPU_LIMIT = float(os.getenv("CPU_LIMIT", 80))
    MEMORY_LIMIT = float(os.getenv("MEMORY_LIMIT", 85))

    # Storage settings
    HISTORY_FILE = os.getenv(
        "HISTORY_FILE",
        "monitoring_history.csv"
    )

    LOG_FILE = os.getenv(
        "LOG_FILE",
        "app.log"
    )

    # Server settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))

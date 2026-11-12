import psutil
from datetime import datetime


def collect_system_metrics():
    """
    Collect current system resource utilization.

    Returns:
        dict: CPU usage, memory usage and collection timestamp.
    """

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "timestamp": datetime.now().isoformat(timespec="seconds")
    }

from app.config import Config


def detect_incidents(metrics, application_status="RUNNING"):
    """
    Analyze system metrics and detect monitoring incidents.

    Returns:
        list: Detected incidents with severity and descriptions.
    """

    incidents = []

    cpu_usage = metrics["cpu_usage"]
    memory_usage = metrics["memory_usage"]

    if cpu_usage >= Config.CPU_LIMIT:
        incidents.append({
            "type": "HIGH_CPU_USAGE",
            "severity": "WARNING",
            "message": (
                f"CPU usage is {cpu_usage}%, "
                f"exceeding the configured limit of {Config.CPU_LIMIT}%."
            )
        })

    if memory_usage >= Config.MEMORY_LIMIT:
        incidents.append({
            "type": "HIGH_MEMORY_USAGE",
            "severity": "WARNING",
            "message": (
                f"Memory usage is {memory_usage}%, "
                f"exceeding the configured limit of {Config.MEMORY_LIMIT}%."
            )
        })

    if application_status == "FAILED":
        incidents.append({
            "type": "APPLICATION_FAILURE",
            "severity": "CRITICAL",
            "message": "Application failure has been detected."
        })

    return incidents

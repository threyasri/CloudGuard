
from flask import Flask, jsonify, render_template_string
import psutil
import logging
import csv
import os
from datetime import datetime

app = Flask(__name__)

failure = False

# Monitoring configuration
CPU_LIMIT = 80
MEMORY_LIMIT = 85
HISTORY_FILE = "monitoring_history.csv"

# Configure event logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create monitoring history file if it doesn't exist
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU Usage", "Memory Usage", "Status"])


dashboard = """
<!DOCTYPE html>
<html>
<head>
    <title>CloudGuard Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            padding: 30px;
        }
        .container {
            max-width: 750px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
        }
        .metric {
            background: #e8f0fe;
            padding: 15px;
            margin: 12px 0;
            border-radius: 8px;
        }
        button {
            padding: 12px;
            margin: 8px 5px 8px 0;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .fail { background: #ef4444; color: white; }
        .recover { background: #16a34a; color: white; }
        .alert {
            background: #fee2e2;
            padding: 12px;
            border-radius: 8px;
            color: #991b1b;
        }
        a { margin-right: 12px; }
    </style>
</head>
<body>
<div class="container">
    <h1>CloudGuard</h1>
    <p>Cloud Application Monitoring Prototype</p>

    <div class="metric">
        <h3>Application Status</h3>
        <h2>{{ status }}</h2>
    </div>

    <div class="metric">
        <h3>CPU Usage</h3>
        <h2>{{ cpu }}%</h2>
    </div>

    <div class="metric">
        <h3>Memory Usage</h3>
        <h2>{{ memory }}%</h2>
    </div>

    <div class="metric">
        <h3>Monitoring Time</h3>
        <p>{{ time }}</p>
    </div>

    {% if alerts %}
        <div class="alert">
            <h3>Monitoring Alerts</h3>
            {% for alert in alerts %}
                <p>{{ alert }}</p>
            {% endfor %}
        </div>
    {% else %}
        <p>All monitoring thresholds are normal.</p>
    {% endif %}

    <h3>Failure Simulation</h3>

    <form action="/simulate-failure" method="post">
        <button class="fail">Simulate Failure</button>
    </form>

    <form action="/recover" method="post">
        <button class="recover">Recover Application</button>
    </form>

    <p>Dashboard refreshes every 5 seconds.</p>

    <h3>CloudGuard Services</h3>
    <a href="/health">Health</a>
    <a href="/metrics">Metrics</a>
    <a href="/logs">Event Logs</a>
    <a href="/history">Monitoring History</a>
</div>
</body>
</html>
"""


@app.route("/")
def home():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent

    status = "FAILED" if failure else "RUNNING"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save monitoring data
    with open(HISTORY_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, cpu, memory, status])

    # Check monitoring thresholds
    alerts = []

    if cpu > CPU_LIMIT:
        alerts.append("High CPU usage detected!")
        logging.warning("High CPU usage: %s%%", cpu)

    if memory > MEMORY_LIMIT:
        alerts.append("High memory usage detected!")
        logging.warning("High memory usage: %s%%", memory)

    if failure:
        alerts.append("Application failure detected!")

    return render_template_string(
        dashboard,
        status=status,
        cpu=cpu,
        memory=memory,
        time=timestamp,
        alerts=alerts
    )


@app.route("/health")
def health():
    if failure:
        return jsonify({
            "status": "unhealthy",
            "message": "Simulated application failure"
        }), 503

    return jsonify({
        "status": "healthy",
        "message": "Application is running"
    })


@app.route("/metrics")
def metrics():
    return jsonify({
        "cpu_usage": psutil.cpu_percent(interval=0.5),
        "memory_usage": psutil.virtual_memory().percent,
        "timestamp": datetime.now().isoformat()
    })


@app.route("/simulate-failure", methods=["POST"])
def simulate_failure():
    global failure

    if not failure:
        failure = True
        logging.error("Application failure simulated")

    return "Failure simulated. <a href='/'>Return to dashboard</a>"


@app.route("/recover", methods=["POST"])
def recover():
    global failure

    if failure:
        failure = False
        logging.info("Application recovered successfully")

    return "Application recovered. <a href='/'>Return to dashboard</a>"


@app.route("/logs")
def logs():
    try:
        with open("app.log", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No events recorded yet."

    return "<h2>CloudGuard Event Logs</h2><pre>" + content + "</pre><a href='/'>Back</a>"


@app.route("/history")
def history():
    records = []

    with open(HISTORY_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            records.append(row)

    records = records[-20:]
    records.reverse()

    html = """
    <html>
    <head>
        <title>Monitoring History</title>
        <style>
            body { font-family: Arial; padding: 25px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 10px; }
            th { background: #e8f0fe; }
        </style>
    </head>
    <body>
        <h1>CloudGuard Monitoring History</h1>
        <p>Latest monitoring records</p>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>CPU Usage</th>
                <th>Memory Usage</th>
                <th>Status</th>
            </tr>
    """

    for row in records:
        html += "<tr>"
        for value in row:
            html += "<td>" + value + "</td>"
        html += "</tr>"

    html += """
        </table>
        <br>
        <a href="/">Back to Dashboard</a>
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    logging.info("CloudGuard application started")
    app.run(debug=False, host="0.0.0.0", port=5000)

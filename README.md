
# CloudGuard
### Cloud-Based Monitoring and Incident Detection System

CloudGuard is a Flask-based application monitoring system designed to monitor system resource utilization, check application health, simulate failures, and record monitoring activity.

The project demonstrates the fundamentals of application monitoring, logging, failure detection, recovery, and Docker-based containerization.

## Features

- CPU utilization monitoring
- Memory utilization monitoring
- Application health checks
- Real-time monitoring dashboard
- Automatic dashboard refresh
- CPU and memory threshold alerts
- Failure simulation and recovery
- Application event logging
- CSV-based monitoring history
- CPU and memory graph generation
- REST endpoints for health and metrics
- Docker-based application deployment
- Persistent storage using Docker bind mounts

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web framework |
| psutil | System resource monitoring |
| Matplotlib | Graph generation |
| CSV | Monitoring data storage |
| Docker | Application containerization |
| Git & GitHub | Version control |

## Project Structure

```text
CloudGuard/
│
├── app.py
├── graph.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── cpu_graph.png
└── memory_graph.png
```

## Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/threyasri/CloudGuard.git
cd CloudGuard
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the environment

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open the dashboard:

http://localhost:5000

## Docker Setup

### 1. Build the Docker image

```bash
docker build -t cloudguard:latest .
```

### 2. Run the container

```bash
docker run -d --name cloudguard -p 5000:5000 cloudguard:latest
```

### 3. Access the dashboard

http://localhost:5000

### 4. View container logs

```bash
docker logs cloudguard
```

## Monitoring Endpoints

| Endpoint | Description |
|---|---|
| `/` | Monitoring dashboard |
| `/health` | Application health status |
| `/metrics` | CPU and memory metrics |
| `/logs` | Application logs |
| `/history` | Recent monitoring history |
| `/simulate-failure` | Simulates an application failure |
| `/recover` | Recovers the application |

Note: Failure simulation and recovery use POST requests.

## Monitoring and Visualization

CloudGuard records monitoring information in CSV format and supports graphical representation of CPU and memory utilization through Matplotlib.

## Current Project Status

- Flask monitoring application implemented.
- CPU and memory monitoring implemented.
- Health checks and failure/recovery simulation implemented.
- Application logging and CSV history implemented.
- Docker image successfully built.
- Docker container successfully tested.
- Persistent storage verified using Docker bind mounts.
- GitHub repository initialized and synchronized.

## Future Enhancements

- Deploy CloudGuard on AWS EC2.
- Configure AWS IAM roles and permissions.
- Integrate Amazon CloudWatch.
- Implement centralized cloud monitoring.
- Introduce automated CI/CD using GitHub Actions.
- Improve alerting and incident notification capabilities.

## Author

**Threya Sri**

BCA Student  
ICFAI University Hyderabad

## Repository

https://github.com/threyasri/CloudGuard

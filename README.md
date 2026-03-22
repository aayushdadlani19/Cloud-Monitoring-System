# Cloud-Monitoring-System
Cloud Monitoring System using Prometheus and Grafana

Cloud Monitoring System (Prometheus + Grafana)

Project Overview

This project implements a cloud-based monitoring and observability system using Prometheus and Grafana. It monitors infrastructure, containers, application metrics, and logs in real time.

The system is deployed using Docker containers and hosted on AWS EC2.

Technologies Used
Prometheus – Metrics monitoring
Grafana – Visualization dashboards
Loki – Log aggregation
Promtail – Log collection
Node Exporter – System metrics
cAdvisor – Container metrics
Docker – Containerization
AWS EC2 – Cloud deployment
System Architecture
Application
     │
Metrics (/metrics endpoint)
     │
Prometheus
     │
Grafana Dashboards
     │
Visualization

Logs pipeline:

Docker Logs
     │
Promtail
     │
Loki
     │
Grafana
Features
Infrastructure monitoring
Container monitoring
Application metrics monitoring
Log monitoring
Real-time dashboards
Cloud deployment on AWS
Dockerized monitoring stack
Project Structure
cloud-monitoring
│
├── docker-compose.yml
├── prometheus.yml
├── promtail-config.yml
├── alert.rules.yml
├── alertmanager.yml
│
├── dashboards/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
Setup Instructions
Clone Repository
git clone https://github.com/username/cloud-monitoring-system.git
cd cloud-monitoring-system
Start Monitoring Stack
docker-compose up -d
Access Dashboards

Grafana:

http://localhost:3000

Prometheus:

http://localhost:9090
Cloud Deployment

The monitoring stack is deployed on AWS EC2 using Docker containers.

Access Grafana:

http://<server-ip>:3000
Dashboard Metrics

The dashboards monitor:

CPU usage
Memory usage
Container metrics
Request rate
Request latency
Application requests
Future Improvements
Alerting system using Prometheus Alertmanager
Multi-node monitoring
Kubernetes monitoring
CI/CD pipeline integration
Author

Aayush Dadlani
B.Tech CSE Project – Cloud Monitoring System

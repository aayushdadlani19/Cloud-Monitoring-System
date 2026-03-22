# Cloud-Monitoring-System
Cloud Monitoring System using Prometheus and Grafana



1. Project Overview

This project implements a cloud-based monitoring and observability platform using Prometheus and Grafana.
The system collects metrics from infrastructure, containers, and applications and visualizes them through interactive dashboards.
The monitoring stack is containerized using Docker and deployed on AWS EC2 for real-time monitoring of cloud environments.
This project demonstrates how DevOps teams monitor systems in production environments.

2. Objectives

Monitor infrastructure resources such as CPU, memory, and disk usage
Monitor container performance and resource utilization
Collect application metrics using Prometheus endpoints
Visualize monitoring data using Grafana dashboards
Implement centralized logging using Loki and Promtail
Deploy monitoring system on cloud infrastructure

3. Technologies Used

Prometheus – Metrics monitoring and data collection
Grafana – Visualization dashboards
Loki – Log aggregation system
Promtail – Log collection agent
Node Exporter – System metrics exporter
cAdvisor – Container resource monitoring
Docker – Containerization platform
AWS EC2 – Cloud deployment environment

4. System Architecture

Application
│
Metrics Endpoint (/metrics)
│
Prometheus (Metric Collection)
│
Grafana (Visualization Layer)
│
Monitoring Dashboards
Log Monitoring Pipeline
Docker Containers
│
Promtail
│
Loki
│
Grafana

5. Features

Real-time infrastructure monitoring
Container performance monitoring
Application metrics monitoring
Log aggregation and monitoring
Interactive Grafana dashboards
Docker-based monitoring stack
Cloud deployment on AWS

6. Project Structure

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
│
└── README.md

7. Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/cloud-monitoring-system.git
cd cloud-monitoring-system

Step 2: Start Monitoring Stack

docker-compose up -d
This command starts the monitoring services including Prometheus, Grafana, Loki, Promtail, Node Exporter, and cAdvisor.

8. Access Monitoring Dashboards
Grafana Dashboard

http://localhost:3000
Default Login

Username: admin
Password: admin

Prometheus Dashboard

http://localhost:9090

9. Cloud Deployment

The monitoring system is deployed on AWS EC2 using Docker containers.

Grafana Access

http://SERVER-IP:3000

Prometheus Access

http://SERVER-IP:9090

10. Dashboard Metrics

The monitoring dashboards visualize several important metrics including:

CPU utilization
Memory utilization
Container CPU usage
Container memory usage
Application request rate
Request latency
Total requests

These metrics help detect system performance issues and monitor system health.

11. Screenshots
Add screenshots of monitoring dashboards here.
Example folder:

screenshots/
grafana-dashboard.png
prometheus-targets.png
container-metrics.png
12. Future Improvements
Prometheus Alertmanager integration for alert notifications
Multi-server monitoring
Kubernetes monitoring integration
CI/CD pipeline automation
Long-term metrics storage
13. Author
Aayush Dadlani
B.Tech Computer Science Engineering
Cloud Monitoring System Project
14. License
This project is developed for educational and learning purposes.

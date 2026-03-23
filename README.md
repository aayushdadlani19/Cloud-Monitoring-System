# 🚀 Cloud Monitoring & Observability Platform

### Prometheus • Grafana • Loki • Promtail • cAdvisor • Docker • AWS EC2

A **cloud-native monitoring and observability platform** designed to collect, aggregate, and visualize **infrastructure, container, and application metrics** in real time.

This project implements a **production-inspired monitoring stack** using **Prometheus for metrics, Grafana for visualization, and the Grafana Loki stack for centralized logging**.
The system is containerized using **Docker** and deployed on **AWS EC2**, demonstrating a scalable observability architecture commonly used in modern **DevOps and cloud environments**.

---

# 📌 Project Overview

Modern cloud systems require comprehensive observability to ensure reliability, performance optimization, and efficient troubleshooting.

This project builds a **complete monitoring pipeline** that collects:

* Infrastructure metrics
* Container performance metrics
* System resource utilization
* Centralized application logs

The monitoring stack enables **real-time infrastructure insights and log analysis through unified Grafana dashboards**.

---

# 🏗️ Architecture

```
                AWS EC2 Cloud Instance
                        │
                        ▼
              ┌────────────────────┐
              │      Docker        │
              │ Monitoring Stack   │
              └─────────┬──────────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
  Node Exporter      cAdvisor        Promtail
 (Host Metrics)   (Container Metrics) (Log Collector)
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                  Prometheus
            (Metrics Collection)
                        │
                        ▼
                     Loki
                (Log Aggregation)
                        │
                        ▼
                     Grafana
          (Dashboards & Observability)
```

---

# ⚙️ Tech Stack

| Category               | Tools         |
| ---------------------- | ------------- |
| Monitoring             | Prometheus    |
| Visualization          | Grafana       |
| Logging                | Grafana Loki  |
| Log Shipping           | Promtail      |
| Infrastructure Metrics | Node Exporter |
| Container Metrics      | cAdvisor      |
| Containerization       | Docker        |
| Cloud Platform         | AWS EC2       |
| Programming            | Python        |
| Configuration          | YAML          |

---

# ✨ Key Features

* Cloud infrastructure monitoring
* Container performance monitoring
* Centralized log aggregation
* Real-time system observability
* Interactive Grafana dashboards
* Dockerized monitoring stack
* Scalable cloud deployment on AWS
* Unified metrics and log visualization

---

# 📊 Metrics & Logs Collected

The monitoring system tracks:

### Infrastructure Metrics

* CPU utilization
* Memory consumption
* Disk usage
* Network traffic
* System load

### Container Metrics

* Container CPU usage
* Container memory usage
* Container resource consumption

### Log Monitoring

* Application logs
* System logs
* Container logs

All metrics and logs are **visualized in Grafana dashboards for easy analysis and troubleshooting.**

---

# 🐳 Dockerized Monitoring Stack

The entire observability stack runs using Docker containers including:

* Prometheus
* Grafana
* Loki
* Promtail
* Node Exporter
* cAdvisor

This approach enables **portable, scalable, and production-like deployment.**

---

# ☁️ Cloud Deployment (AWS EC2)

The monitoring platform is deployed on an **AWS EC2 instance**, simulating a real-world cloud infrastructure monitoring environment.

### Deployment Flow

1. Launch AWS EC2 instance
2. Install Docker
3. Deploy monitoring containers
4. Configure Prometheus scraping targets
5. Connect Grafana dashboards
6. Monitor infrastructure and logs in real time

---

# 📂 Project Structure

```
cloud-monitoring-observability
│
├── prometheus
│   └── prometheus.yml
│
├── grafana
│   └── dashboards
│
├── loki
│   └── loki-config.yml
│
├── promtail
│   └── promtail-config.yml
│
├── docker-compose.yml
│
├── screenshots
│   ├── grafana-dashboard.png
│   ├── metrics-dashboard.png
│   └── logs-dashboard.png
│
└── README.md
```

---

# 📈 Real World Applications

* Cloud infrastructure monitoring
* DevOps observability platforms
* Microservices monitoring
* Container performance analysis
* Centralized log management
* Production incident troubleshooting

---

# 🔮 Future Improvements

* Kubernetes monitoring integration
* Prometheus Alertmanager for alerts
* Distributed cluster monitoring
* CI/CD pipeline integration
* Multi-cloud observability setup

---

# 👨‍💻 Author

**Aayush Dadlani**

B.Tech Computer Science Engineering

Interested in:

* Cloud Computing
* DevOps Engineering
* Infrastructure Monitoring
* Distributed Systems

---

# ⭐ Support

If you found this project useful, please **give it a star ⭐ on GitHub**.

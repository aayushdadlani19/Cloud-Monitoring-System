# 🚀 Cloud Monitoring System using Prometheus & Grafana

A production-style **cloud infrastructure monitoring system** built using **Prometheus and Grafana** to collect, store, and visualize system metrics in real time.

This project demonstrates how modern DevOps teams monitor cloud services to ensure **high availability, performance optimization, and proactive incident detection**.

---

# 📌 Project Overview

Modern cloud systems require continuous monitoring to detect failures, resource bottlenecks, and performance degradation.

This project implements a **metrics-based monitoring pipeline** where Prometheus continuously scrapes system metrics and Grafana visualizes them using interactive dashboards.

The system monitors:

- CPU Usage
- Memory Utilization
- Disk Usage
- Network Traffic
- System Performance Metrics

---

# 🏗️ Architecture

```
+--------------------+
|   Target System    |
|   (Node Exporter)  |
+---------+----------+
          |
          v
+--------------------+
|    Prometheus      |
| Metric Collection  |
|  & Storage (TSDB)  |
+---------+----------+
          |
          v
+--------------------+
|      Grafana       |
| Data Visualization |
|   Dashboards       |
+--------------------+
```

---

# ⚙️ Tech Stack

| Category | Technology |
|--------|-------------|
| Monitoring | Prometheus |
| Visualization | Grafana |
| Metrics Exporter | Node Exporter |
| Configuration | YAML |
| OS Environment | Linux / WSL |
| Version Control | Git & GitHub |

---

# ✨ Key Features

- Real-time infrastructure monitoring
- Time-series metric collection
- Interactive Grafana dashboards
- System performance visualization
- Production-style monitoring architecture
- Lightweight and scalable monitoring setup

---

# 📊 Metrics Monitored

This monitoring system tracks important infrastructure metrics such as:

- CPU Utilization
- Memory Consumption
- Disk Usage
- Network Activity
- System Load
- Uptime Monitoring

---

# 🛠️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/cloud-monitoring-system.git
cd cloud-monitoring-system
```

---

## 2️⃣ Install Prometheus

Download Prometheus from the official website:

https://prometheus.io/download/

Extract the folder and run:

```bash
./prometheus --config.file=prometheus.yml
```

Prometheus will start on:

```
http://localhost:9090
```

---

## 3️⃣ Install Node Exporter

Download Node Exporter from:

https://prometheus.io/download/

Run the exporter:

```bash
./node_exporter
```

Node Exporter runs on:

```
http://localhost:9100
```

---

## 4️⃣ Install Grafana

Download Grafana from:

https://grafana.com/grafana/download

Start Grafana service.

Open:

```
http://localhost:3000
```

Default credentials:

```
Username: admin
Password: admin
```

---

## 5️⃣ Connect Grafana to Prometheus

1. Open Grafana
2. Go to **Settings → Data Sources**
3. Select **Prometheus**
4. Add URL:

```
http://localhost:9090
```

5. Click **Save & Test**

---

# 📸 Dashboard Preview

Add screenshots of your Grafana dashboards here.

Example:

```
screenshots/cpu-monitoring.png
screenshots/memory-monitoring.png
screenshots/system-dashboard.png
```

Example markdown:

```markdown
![CPU Monitoring](screenshots/cpu-monitoring.png)
![Memory Monitoring](screenshots/memory-monitoring.png)
```

---

# 📂 Project Structure

```
cloud-monitoring-system
│
├── prometheus.yml
├── dashboards
│   └── grafana-dashboard.json
│
├── screenshots
│   ├── cpu-monitor.png
│   ├── memory-monitor.png
│   └── system-dashboard.png
│
└── README.md
```

---

# 📈 Future Improvements

- Alerting system using **Alertmanager**
- Kubernetes monitoring integration
- Container monitoring with **cAdvisor**
- Distributed microservice monitoring
- Cloud deployment monitoring (AWS / GCP / Azure)

---

# 🚀 Real World Use Cases

- Cloud infrastructure monitoring
- DevOps observability systems
- Performance monitoring
- Production system debugging
- Resource usage analysis

---

# 👨‍💻 Author

**Aayush Dadlani**

B.Tech CSE Cloud Computing And Automation 

Interested in:

- Cloud Computing
- DevOps
- System Monitoring
- Distributed Systems

---


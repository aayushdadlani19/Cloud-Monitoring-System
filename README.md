**🚀 Cloud Monitoring System using Prometheus & Grafana**

A production-style cloud infrastructure monitoring system built using Prometheus and Grafana to collect, store, and visualize system metrics in real time. The project demonstrates how modern DevOps teams monitor cloud services to ensure high availability, performance optimization, and proactive incident detection.
This project implements a metrics-based monitoring pipeline where Prometheus continuously scrapes system metrics and Grafana transforms them into interactive dashboards for real-time observability.


**📌 Project Overview**

Modern cloud systems require continuous monitoring to detect failures, resource bottlenecks, and performance degradation. This project simulates a real-world monitoring setup used in production environments.

The system collects infrastructure metrics such as:

•	CPU utilization 

•	Memory usage 

•	Disk I/O 

•	Network activity 

•	System uptime 


These metrics are processed and visualized through Grafana dashboards to provide clear insights into system health and performance trends.



**🏗️ Architecture**




<img width="361" height="244" alt="Screenshot 2026-03-23 144310" src="https://github.com/user-attachments/assets/393b575a-e46c-4cec-b04a-bf2dcd4116e5" />


**Workflow**


•	Node Exporter exposes system metrics.

•	Prometheus scrapes metrics at defined intervals.

•	Metrics are stored in the Prometheus time-series database.

•	Grafana queries Prometheus to visualize metrics in dashboards.


<img width="819" height="471" alt="image" src="https://github.com/user-attachments/assets/fe59ea6b-c1ce-44ca-9ee8-97bafd81b613" />


<img width="536" height="311" alt="Screenshot 2026-03-23 150706" src="https://github.com/user-attachments/assets/6f481d23-a612-4047-b392-87d7a5ddef67" />



<img width="496" height="258" alt="image" src="https://github.com/user-attachments/assets/944b86a6-bc91-45a3-b9ea-61810b2cecc1" />


**🛠️ Setup Instructions**

<img width="270" height="50" alt="image" src="https://github.com/user-attachments/assets/b57ca5d4-60cb-4149-9ba0-940206b8dc69" />   



<img width="679" height="64" alt="image" src="https://github.com/user-attachments/assets/b1d6a688-ef49-4664-a896-95d6c94af9fa" />


<img width="397" height="90" alt="image" src="https://github.com/user-attachments/assets/da7ae4dc-a6ca-48d0-88c9-665395d72522" />








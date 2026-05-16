# System Health Monitor

A real-time Linux server monitoring tool built with Python and Flask that monitors system health and sends automated alerts.

## What is this?
A lightweight server monitoring tool that tracks CPU, RAM, and Disk usage in real-time. When any metric exceeds the defined threshold, it automatically sends an email alert. A live web dashboard shows current system stats updated every 5 seconds.

## Features
- Real-time CPU, RAM, and Disk monitoring every 5 seconds
- Automated email alerts via SMTP when thresholds exceeded
  - CPU > 80%
  - RAM > 80%
  - Disk > 90%
- Live web dashboard powered by Flask REST API
- Logging to file (health.log) for history and debugging
- Systemd service for auto-start on system reboot
- Cron job to clean logs daily at midnight

## Tech Stack
- **Language:** Python
- **Libraries:** psutil, Flask, smtplib, python-dotenv
- **Linux:** /proc filesystem, Systemd, Cron
- **Cloud:** AWS EC2 (Free Tier)
- **Monitoring:** Custom alerting logic

## Architecture
Browser → Flask /metrics API → psutil → Linux /proc → CPU/RAM/Disk data

## How to Run

1. Clone the repository
   git clone https://github.com/foramrafaliya/system-health-monitor.git
   cd system-health-monitor

2. Install dependencies
   pip3 install psutil flask python-dotenv --break-system-packages

3. Create .env file
   EMAIL=your_email@gmail.com
   PASSWORD=your_gmail_app_password

4. Run the monitor
   python3 monitor.py

5. Run the dashboard
   python3 app.py

6. Open browser
   http://127.0.0.1:5000

## Deployment (AWS EC2)

1. Launch EC2 instance (Ubuntu, t2.micro - Free Tier)
2. SSH into instance
   ssh -i key.pem ubuntu@EC2_PUBLIC_IP

3. Clone repository
   git clone https://github.com/foramrafaliya/system-health-monitor.git

4. Install dependencies
   pip3 install psutil flask python-dotenv --break-system-packages

5. Create .env file with credentials

6. Setup systemd service for auto-start

7. Open port 5000 in EC2 Security Group

8. Access dashboard
   http://EC2_PUBLIC_IP:5000

## Project Motivation
Built this project to understand how monitoring tools like Prometheus and Grafana work internally. Already used Grafana in RetailOps project to monitor 13 microservices — wanted to implement the core monitoring logic from scratch using Python and Linux /proc filesystem.

## Screenshots
<img width="673" height="437" alt="image" src="https://github.com/user-attachments/assets/d4782d1e-a769-4405-8f1c-38e38088996b" />



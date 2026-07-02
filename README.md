
# 🌍 Flask Weather Application Deployment

## 📌 Project Overview

This project is a Flask-based weather application deployed on an AWS EC2 Ubuntu 24 instance.

The application allows users to enter a UK postcode and retrieve live weather information. It uses external APIs to convert postcodes into coordinates and fetch weather data.

### APIs Used:
- Postcodes.io API → converts postcode to latitude/longitude
- OpenWeather API → retrieves live weather data

### Technologies Used:
- Python (Flask)
- Gunicorn (WSGI server)
- Nginx (Reverse Proxy)
- AWS EC2 (Ubuntu 24)
- Git & GitHub

---

# 1. EC2 Instance Setup

## Instance Configuration
- Cloud Provider: AWS
- Instance Type: t3.micro
- Operating System: Ubuntu 24.04
- Key Pair: SSH key (.pem file)

## Security Group Rules

| Type  | Port | Source        | Purpose |
|------|------|---------------|---------|
| SSH  | 22   | My IP         | Remote access to EC2 |
| HTTP | 80   | 0.0.0.0/0     | Public access to web app |

---

# 2. Connect to EC2

```bash
ssh -i "Suhaib 610 Key.pem" ubuntu@<EC2_PUBLIC_IP>

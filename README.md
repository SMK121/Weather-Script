# 🌍 Deployment of Flask Weather Application

## Project Overview

This project deploys a Flask weather application to an AWS EC2 Ubuntu 24 instance.

The application allows users to enter a UK postcode and receive live weather information for that location.

It works by:
- Converting a postcode into latitude and longitude using the Postcodes.io API
- Using those coordinates to retrieve live weather data from the OpenWeather API
- Displaying results through a Flask web interface and API endpoint

### Technologies Used:
- Python (Flask)
- Gunicorn (WSGI production server)
- Nginx (reverse proxy)
- AWS EC2 (Ubuntu 24.04)
- Git & GitHub
- External APIs (Postcodes.io + OpenWeather)

The final application is accessed via the EC2 public IPv4 address in a web browser.

---

# ☁️ 1. Launch EC2 Instance

## Instance Details

- Cloud provider: AWS
- Instance type: t3.micro
- Operating system: Ubuntu 24.04
- Access method: SSH key authentication (.pem file)
- Web server: Nginx
- Application framework: Flask

## Security Group Rules

The following inbound rules were configured:

| Type  | Port | Source    | Purpose |
|------|------|-----------|---------|
| SSH  | 22   | My IP     | Secure remote access to EC2 |
| HTTP | 80   | 0.0.0.0/0 | Public access to the web application |

---

# 🔌 2. Connect to EC2 Instance

The EC2 instance is accessed using SSH from the local machine:

```bash

#!/bin/bash

# Update server
sudo apt update -y

# Install required packages
sudo apt install python3-pip python3-venv nginx git -y

# Clone project from GitHub
git clone https://github.com/SMK121/Weather-Script.git

# Enter project folder
cd Weather-Script

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install flask requests gunicorn

# Start app using gunicorn
gunicorn -w 4 -b 127.0.0.1:8000 my_weather_api:app
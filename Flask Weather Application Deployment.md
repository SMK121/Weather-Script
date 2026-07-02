# 🌍 Flask Weather Application Deployment

## Project Overview

Project Overview

This project demonstrates how a Python Flask weather application can be deployed to an AWS EC2 virtual machine running Ubuntu and made accessible over the internet.

The application provides a simple web interface where a user enters a UK postcode. It first sends the postcode to the Postcodes.io API to obtain the corresponding latitude and longitude coordinates. These coordinates are then passed to the OpenWeather API, which returns the current weather conditions for that location. Flask processes the requests and displays the results back to the user in the browser.

To make the application suitable for production, Gunicorn is used as the WSGI application server while Nginx acts as a reverse proxy, forwarding incoming HTTP requests to the Flask application.

### Technologies Used

* Python
* Flask
* Gunicorn
* Nginx
* AWS EC2 Ubuntu 
* Git & GitHub
* Postcodes.io API
* OpenWeather API


## 📦 Project File Structure

The project contains the following files and folders:

```text
Flask_Weather_api.py    - Contains the main weather API logic and helper functions.
my_weather_api.py       - Starts the Flask application and defines the web routes.
utils.py                - Stores reusable helper functions used throughout the project.
templates/              - Contains the HTML templates used by the Flask application.
weather_api_key.txt     - Stores the OpenWeather API key used to authenticate API requests.

```
  

The completed application is publicly accessible using the EC2 public IPv4 address.

---

# 1. EC2 Instance


## Instance Details

An AWS EC2 virtual machine was launched to host the Flask application.

Setting	Value
Cloud Provider	AWS
Instance Type	t3.micro
Operating System	Ubuntu Server
Authentication	SSH Key Pair (.pem)

## Security Group Configuration

The following inbound rules were configured:

| Type | Port | Source | Purpose |
|------|------|--------|---------|
| SSH | 22 | My IP | Allows secure SSH access to the server |
| HTTP | 80 | 0.0.0.0/0 | Allows public users to access the deployed application |

---

# 2. Connect to the EC2 Instance

After launching the instance, connect using SSH.

```bash
ssh -i "Suhaib 610 Key.pem" ubuntu@<EC2_PUBLIC_IP>
```

**Command explanation**

* `ssh` establishes a secure remote connection.
* `-i` specifies the private key used for authentication.
* `ubuntu` is the default user for Ubuntu EC2 instances.

---

# 3. Update the Server

Before installing software, update the package lists.

```bash
sudo apt update -y
```

This ensures the latest package information is available.

---

# 4. Install Required Software

Install the required system packages.

```bash
sudo apt install python3-pip nginx git -y
```

### Package Purpose

| Package       | Purpose                           |
| ------------- | --------------------------------- |
| `python3-pip` | Installs Python packages          |
| `nginx`       | Acts as a reverse proxy           |
| `git`         | Downloads the project from GitHub |

---

# 📤 SCP Deployment (File Transfer to EC2)

I used SCP (Secure Copy Protocol) to transfer my Flask project from my local machine to the AWS EC2 server.

---

## 🧾 Command Used

## 🧠 What this command does

scp Securely transfers files from local machine to a remote server EC2  
-i "Suhaib 610 Key.pem" Uses my AWS SSH key for authentication  
-r Recursively copies the entire project folder including subfolders like templates  
"C: Users Suhaib ... Flask Weather api" My local Flask project directory  
ubuntu@108.131.7.199 My EC2 instance Ubuntu user plus public IP address  
:~ Copies files into the home directory /home/ubuntu/ on the server  

---

## 📦 Result

After running this command, my project was successfully copied to:

/home/ubuntu/Flask Weather api/

### This included:
- Flask backend code  
- HTML templates  
- API logic files  
- Utility scripts
  
---



# 5. Download the Project

Clone the GitHub repository onto the EC2 instance.

```bash
git clone https://github.com/SMK121/Weather-Script.git
```

Move into the Flask project directory.

```bash
cd "Weather-Script/Flask Weather api"
```

Check that all files are present.

```bash
ls
```


# 6. Install Python Dependencies

Install the Python libraries required by the application.

```bash
pip3 install flask requests gunicorn
```

### Python Packages

| Package  | Purpose                                 |
| -------- | --------------------------------------- |
| Flask    | Runs the web application                |
| Requests | Makes API requests to external services |
| Gunicorn | Runs Flask in a production environment  |

---

# 7. Run the Flask Application

Instead of using Flask's built-in development server, the application is started with Gunicorn.

```bash
gunicorn -w 4 -b 127.0.0.1:8000 my_weather_api:app
```

### Command Breakdown

* `gunicorn` starts the application.
* `-w 4` creates four worker processes.
* `127.0.0.1:8000` runs the application locally on port 8000.
* `my_weather_api:app` tells Gunicorn which Flask application to load.

To verify the application is running, open a second SSH session and run:

```bash
curl http://127.0.0.1:8000
```

If successful, the HTML for the weather page is returned.

---

# 8. Configure Nginx as a Reverse Proxy

Rather than allowing users to access Gunicorn directly, Nginx forwards incoming web requests to the Flask application.

Create a new configuration file.

```bash
sudo nano /etc/nginx/sites-available/weather_app
```

Add the following configuration:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable the site.

```bash
sudo ln -s /etc/nginx/sites-available/weather_app /etc/nginx/sites-enabled/
```

Restart Nginx.

```bash
sudo systemctl restart nginx
```

Once configured, users can access the application through port 80 without specifying the Gunicorn port.

---

# 9. Test the Application

Open a web browser and navigate to:

```
http://<EC2_PUBLIC_IP>
```

Enter a valid UK postcode and submit the form.

The application will:

1. Send the postcode to the Postcodes.io API.
2. Retrieve the latitude and longitude.
3. Send those coordinates to the OpenWeather API.
4. Display the current weather conditions.

---

# 10. Application Workflow

```
User enters postcode
          │
          ▼
Postcodes.io API
          │
          ▼
Latitude & Longitude
          │
          ▼
OpenWeather API
          │
          ▼
Weather Information
          │
          ▼
Displayed in Flask Web Application
```

---

# 11. Screenshots


* EC2 instance running
<img width="1435" height="334" alt="image" src="https://github.com/user-attachments/assets/ab3550e5-cda6-4ac7-a4e0-5555ebb788c8" />

---
  
* GitHub repository cloned
<img width="1439" height="297" alt="image" src="https://github.com/user-attachments/assets/02307c90-612b-4bdd-81ba-4380fc68ccb5" />

---

* Gunicorn running
<img width="1393" height="250" alt="image" src="https://github.com/user-attachments/assets/ae478f14-77a5-4402-97d9-117d23ceb4c4" />

---
  
* Nginx configuration
<img width="925" height="119" alt="image" src="https://github.com/user-attachments/assets/2c5246ed-56c1-4e65-a0ab-43a7e1b8dab1" />

---
 
* Weather search results / Frontend
<img width="1901" height="1017" alt="image" src="https://github.com/user-attachments/assets/4d36eef3-5856-45e0-8cd4-204ca7bd6af8" />


---

# 12. Reflection

Through this project I gained practical experience with:

* Deploying a Flask application on AWS EC2.
* Using Linux commands to configure a server.
* Installing application dependencies.
* Running Flask with Gunicorn instead of the development server.
* Configuring Nginx as a reverse proxy.
* Integrating multiple external APIs.
* Deploying a complete web application that is publicly accessible.

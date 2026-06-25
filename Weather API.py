from pprint import pprint
import requests

# Weather API endpoint
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# Location coordinates
latitude = 51.5933
longitude = 0.20000

# Open file containing API key
with open("weather_api_key") as file:
    api_key = file.readline().strip()

# Send GET request to weather API
response = requests.get(
    WEATHER_ENDPOINT +
    f"?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
)

# Print status code
print(response.status_code)

# If request was successful
if response.status_code == 200:

    # Convert JSON response into Python dictionary
    weather = response.json()

    # Print weather data in readable format
    pprint(weather)

    
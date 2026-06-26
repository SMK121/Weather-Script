import requests  # library used to send HTTP requests to external APIs

from utils import get_weather_icon


# ----------------------------
# API ENDPOINTS
# ----------------------------

# Postcodes API endpoint (converts postcode → latitude & longitude)
POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"

# OpenWeather API endpoint (fetches weather data using lat/lon)
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# API key used to authenticate requests to OpenWeather
API_KEY = "5c41ce44c396ff07e8f2a087d2a809b8"


# ----------------------------
# POSTCODE → LAT / LON
# ----------------------------
def get_coordinates(postcode):

    # Try block prevents program crashing if API request fails
    try:
        # Send request to Postcodes API
        response = requests.get(POSTCODE_ENDPOINT + postcode)

        # Convert API response into Python dictionary
        data = response.json()

        # Check if API returned success status
        if data["status"] != 200 or not data["result"]:
            return None, None

        # Extract result section from response
        result = data["result"]

        # Return latitude and longitude
        return result["latitude"], result["longitude"]

    except:
        # Return None values if anything goes wrong
        return None, None


# ----------------------------
# LAT / LON → WEATHER DATA
# ----------------------------
def get_weather(lat, lon, api_key):

    # Try block prevents crashes if API request fails
    try:
        # Send request to OpenWeather API with parameters
        response = requests.get(
            WEATHER_ENDPOINT,
            params={
                "lat": lat,
                "lon": lon,
                "appid": api_key,
                "units": "metric"
            }
        )

        # Check if request was successful
        if response.status_code != 200:
            print("Weather API error:", response.text)
            return None

        # Convert response into Python dictionary
        data = response.json()

        # Extract only required weather details
        return {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "icon": get_weather_icon(data["weather"][0]["description"])
        }

    except:
        # Return None if any error occurs
        return None
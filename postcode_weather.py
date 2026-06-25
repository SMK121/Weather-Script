import sys
import requests

# API endpoints used in this project
POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"


# ----------------------------
# STEP 1: Get coordinates from postcode
# ----------------------------
def get_coordinates(postcode):
    # Send request to Postcodes API
    response = requests.get(POSTCODE_ENDPOINT + postcode)

    if response.status_code == 200:
        # Convert response to Python dictionary
        data = response.json()

        # Extract latitude and longitude
        latitude = data["result"]["latitude"]
        longitude = data["result"]["longitude"]

        return latitude, longitude
    else:
        print("Error: Invalid postcode or API issue")
        return None, None


# ----------------------------
# STEP 2: Get weather data using coordinates
# ----------------------------
def get_weather(lat, lon, api_key):
    # Send request to OpenWeather API
    response = requests.get(
        f"{WEATHER_ENDPOINT}?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    )

    if response.status_code == 200:
        # Convert response to Python dictionary
        return response.json()
    else:
        print("Error: Could not fetch weather data")
        return None


# ----------------------------
# STEP 3: Display clean weather output
# ----------------------------
def display_weather(postcode, weather):
    print(f"\nWeather for {postcode}")
    print("------------------------")

    # Extract and display key weather details
    print("Description:", weather["weather"][0]["description"])
    print("Temperature:", round(weather["main"]["temp"]), "°C")
    print("Feels like:", round(weather["main"]["feels_like"]), "°C")
    print("Humidity:", weather["main"]["humidity"], "%")


# ----------------------------
# MAIN PROGRAM (controls flow)
# ----------------------------
def main():

    # Get postcode from command line arguments (e.g. RM1 1AA)
    postcode = "".join(sys.argv[1:]).replace(" ", "")

    # Read API key from file (keeps it secure and not hardcoded)
    with open("weather_api_key") as file:
        api_key = file.readline().strip()

    # STEP 1: Get coordinates from postcode
    lat, lon = get_coordinates(postcode)

    if lat is None:
        return  # stop program if postcode is invalid

    # STEP 2: Get weather data from OpenWeather API
    weather = get_weather(lat, lon, api_key)

    if weather is None:
        return  # stop program if API fails

    # STEP 3: Display final weather output
    display_weather(postcode, weather)


# Run the program
main()
from flask import Flask, jsonify, request, render_template
import Flask_Weather_api  # imports your logic file (postcode → coordinates + weather functions)

# Create Flask application instance
app = Flask(__name__)

# OpenWeather API key used to authenticate weather requests
API_KEY = "5c41ce44c396ff07e8f2a087d2a809b8"


# ----------------------------
# HOME ROUTE (health check)
# ----------------------------
@app.route("/")
def home():
    # Show frontend page instead of JSON
    return render_template("index.html")


# ----------------------------
# WEATHER ROUTE (GET + POST supported)
# ----------------------------
@app.route("/weather-api", methods=["GET", "POST"])
def weather_api():

    # =========================================================
    # GET REQUEST
    # Used for single postcode via browser:
    # Example: /weather-api?postcode=EC1A1BB
    # =========================================================
    if request.method == "GET":

        # Get postcode from query string (?postcode=...)
        postcode = request.args.get("postcode")

        # Validate input
        if not postcode:
            return jsonify({"error": "postcode required"}), 400

        # Clean postcode (remove spaces + standard format)
        postcode = postcode.replace(" ", "").upper()

        # Convert postcode into latitude and longitude
        lat, lon = Flask_Weather_api.get_coordinates(postcode)

        # Handle invalid postcode response
        if lat is None:
            return jsonify({"error": "invalid postcode"}), 400

        # Get weather data using coordinates
        weather = Flask_Weather_api.get_weather(lat, lon, API_KEY)

        return render_template(
            "index.html",  # This tells Flask to load the HTML page from the templates folder
            postcode=postcode,  # Sends the cleaned postcode to the HTML page so it can be displayed
            weather=weather  # Sends the weather dictionary (temp, humidity, etc.) to the HTML page
        )


    # =========================================================
    # POST REQUEST
    # Used for multiple postcodes in one request
    # Example JSON body:
    # ["EC1A1BB", "SW1A1AA"]
    # =========================================================
    if request.method == "POST":

        # Get list of postcodes from request body (JSON array)
        postcodes = request.json

        # Store all results here
        results = []

        # Loop through each postcode in the list
        for postcode in postcodes:

            # Clean postcode format
            postcode = postcode.replace(" ", "").upper()

            # Convert postcode → coordinates
            lat, lon = Flask_Weather_api.get_coordinates(postcode)

            # If postcode is invalid, store error and continue loop
            if lat is None:
                results.append({
                    "postcode": postcode,
                    "error": "invalid postcode"
                })
                continue

            # Get weather data for coordinates
            weather = Flask_Weather_api.get_weather(lat, lon, API_KEY)

            # Store full result (postcode + location + weather)
            results.append({
                "postcode": postcode,
                "location": {
                    "latitude": lat,
                    "longitude": lon
                },
                "weather": weather
            })

        # Return list of all results
        return jsonify(results)


# ----------------------------
# RUN FLASK SERVER
# ----------------------------
if __name__ == "__main__":
    # Start development server with debug mode enabled
    app.run(debug=True)
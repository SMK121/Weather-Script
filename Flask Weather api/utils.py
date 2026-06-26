

# utils.py

def get_weather_icon(description):
    description = description.lower()

    if "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "clear" in description:
        return "☀️"
    elif "snow" in description:
        return "❄️"
    elif "storm" in description:
        return "⛈️"
    else:
        return "🌡️"
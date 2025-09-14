import requests

#  Weather Forecast App - CS50P Final Project
# Author: PHR Manikantha

API_KEY = "3fe92d0b64e88dd46ef37ca56292e931"  # Your API Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def kelvin_to_celsius(temp_k):
    """Convert Kelvin to Celsius (rounded to 2 decimals)."""
    return round(temp_k - 273.15, 2)


def format_weather(data):
    """Format weather JSON into a dictionary with key details."""
    return {
        "location": f"{data['name']}, {data['sys']['country']}",
        "condition": data["weather"][0]["description"].title(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }


def get_weather(city):
    """Fetch weather data for a given city and return formatted dict, or None if error."""
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print(f" Error: {data.get('message', 'Unknown error').title()}\n")
            return None

        return format_weather(data)

    except requests.exceptions.ConnectionError:
        print(" Network error! Please check your internet connection.\n")
        return None
    except Exception as e:
        print(" Unexpected error:", e)
        return None


def display_weather(info):
    """Pretty-print the weather dictionary."""
    if not info:
        return
    print("\n=== Weather Report ===")
    print(f" Location     : {info['location']}")
    print(f" Condition    : {info['condition']}")
    print(f" Temperature  : {info['temperature']}C")
    print(f" Humidity     : {info['humidity']}%")
    print(f" Wind Speed   : {info['wind_speed']} m/s\n")


def main():
    print("=== Weather Forecast App ===")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.strip().lower() == "exit":
            print(" Goodbye!")
            break
        elif not city.strip():
            print(" Please enter a valid city name.\n")
            continue

        info = get_weather(city)
        display_weather(info)


if __name__ == "__main__":
    main()

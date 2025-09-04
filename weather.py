import requests

#  Weather Forecast App - CS50P Final Project
# Author: PHR Manikantha

API_KEY = "3fe92d0b64e88dd46ef37ca56292e931"  #  Your API Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # Parameters for API request
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        # Send request to OpenWeather API
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Handle errors from API
        if data.get("cod") != 200:
            print(f" Error: {data.get('message', 'Unknown error').title()}\n")
            return

        # Display weather details
        print("\n===  Weather Report ===")
        print(f" Location     : {data['name']}, {data['sys']['country']}")
        print(f" Condition    : {data['weather'][0]['description'].title()}")
        print(f" Temperature  : {data['main']['temp']}C")
        print(f" Humidity     : {data['main']['humidity']}%")
        print(f" Wind Speed   : {data['wind']['speed']} m/s\n")

    except requests.exceptions.ConnectionError:
        print(" Network error! Please check your internet connection.\n")
    except Exception as e:
        print(" Unexpected error:", e)

def main():
    print("===  Weather Forecast App ===")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.strip().lower() == "exit":
            print(" Goodbye!")
            break
        elif not city.strip():
            print(" Please enter a valid city name.\n")
            continue
        get_weather(city)

if __name__ == "__main__":
    main()

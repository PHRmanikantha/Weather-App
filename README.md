
🌦️ Weather Forecast App
Video Demo: [Your Video Link Here]
Description:
For my CS50P Final Project, I wanted to create something useful, practical, and fun to code. After thinking about different ideas, I decided on a Weather Forecast App. Weather is something everyone checks almost daily, and I thought it would be interesting to connect Python with real-world live data. By using the OpenWeather API, I was able to fetch real-time weather details for any city in the world.

The app runs in the command line and is very simple to use. You just type in the name of a city, and it shows you the temperature, humidity, wind speed, and weather condition in that location. If the city name is invalid, the app handles it without crashing and instead shows a clear error message. I focused on error handling because I wanted the project to feel reliable, not just a quick demo.

✨ Features
✅ Real-time weather information from OpenWeather API

✅ Displays condition, temperature, humidity, and wind speed

✅ Graceful handling of invalid inputs or network errors

✅ Simple and beginner-friendly interface

✅ Code divided into functions for clarity and testing

🛠️ Technologies Used
Python 3 🐍

Requests Library 🌐

OpenWeather API ⛅

Pytest 🧪 for automated testing

🚀 How to Run
1. Clone or Download the Project
bash
Copy code
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app
2. Install Requirements
bash
Copy code
pip install -r requirements.txt
3. Run the Program
bash
Copy code
python project.py
4. Run Tests
bash
Copy code
pytest -q
📂 Files in the Project
project.py → Contains the main program logic. It includes the main() function and helper functions:

get_weather() → fetches and processes data from the API.

format_weather() → organizes raw JSON into a neat dictionary.

display_weather() → prints the weather in a readable way.

kelvin_to_celsius() → converts Kelvin to Celsius.

test_project.py → Automated tests using pytest. It tests conversion, formatting, error handling, and even printed output.

requirements.txt → Contains external dependencies (only requests).

README.md → Documentation for the project (this file).

🧩 Design Choices and Challenges
At first, I thought about building a graphical version using Tkinter. But I realized that a command-line interface would keep the project clean and easier to focus on Python logic rather than UI design. I also split the code into multiple functions so it would be easier to test. This design made debugging much simpler.

Testing was a bit tricky because I didn’t want the tests to rely on the live API. To solve this, I used sample data and mocked error responses. That way, the tests run reliably even without internet. This was a good learning experience for me about how to test programs that depend on external services.

🚀 Future Improvements
If I had more time, I’d like to:

Add command-line arguments with argparse so users can run python project.py -c London.

Add colored output with colorama for a nicer look.

Save the last searched city to a file, so the app remembers your previous search.

Allow export of results to JSON or CSV.

📌 Conclusion
This project was a fun way to combine Python fundamentals with something real-world. It uses functions, error handling, APIs, and testing — all skills I learned during CS50P. I’m happy with how it turned out because it feels like a small but complete application. I believe it meets all the requirements for the final project, and I’m proud to submit it as the final step of my CS50P journey


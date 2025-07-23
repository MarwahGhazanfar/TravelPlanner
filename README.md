# TravelPlanner ✈️🗺️

**TravelPlanner** is a modular and extensible real-time travel itinerary planner designed to help users make informed decisions while traveling. It currently integrates weather forecasting using the OpenWeatherMap API, providing live updates for any city. This project can be easily extended to include maps, currency converters, hotel listings, local events, and much more.

---

## Features 🚀

- 🌤️ Live weather updates for any city using OpenWeatherMap API 
- 🖥️ Clean and readable terminal output using PrettyTable 
- 🔐 Environment variables support using python-dotenv 
- 🧩 Designed to be extended with additional travel utilities 
- 🎓 Beginner-friendly, modular code with simple logic 

---

## Current Capabilities ✅

This version includes:

- Real-time weather forecast for user-input cities 
- User-friendly interface with clear instructions 
- Display of temperature, weather condition, humidity, and wind speed 
- Structured output for better readability 

> **Note:** The weather API is implemented as a starting point. The architecture supports adding more APIs such as maps, hotel search, route planning, or budget estimation.

---

## Sample Output 🎯

Welcome to Marwah's Travel Itinerary Planner

Enter the name of the city you want to plan travel for: Paris

Fetching live weather forecast for Paris...

+------------------+-----------------------------+
| City             | Paris                       |
| Weather          | Clouds                      |
| Temperature (°C) | 22.3                        |
| Humidity (%)     | 68                          |
| Wind Speed (m/s) | 5.1                         |
+------------------+-----------------------------+

Technologies Used 🛠️

Python 3.11
Requests (for API calls)
PrettyTable (for terminal output formatting)
python-dotenv (for environment variable management)

Folder Structure 📁

TravelPlanner/
│
├── .env                  # Contains API keys (not uploaded to GitHub)
├── travelplanner.py      # Main script
├── README.md             # Project documentation
├── Makefile              # Helper commands

How It Works ⚙️

The script prompts the user to input a city.
It fetches the current weather data using the OpenWeatherMap API.
It displays the results in a structured table format.

The structure is kept modular to allow easy addition of new services like:
Route optimization
Currency exchange rates
Hotel and flight search
Local event suggestions

Customization and Extension 💡
You can easily add:

🌍 Google Maps or Mapbox integration

🏨 Hotel API (e.g., Booking.com or Expedia)

✈️ Flight information

💸 Budget calculators

📅 Day-wise itinerary planner

📍 Places to visit using TripAdvisor API or similar

This project was built with enhancement in mind. Feel free to fork it and extend it for your own use case.

Contribution 🤝
If you’re a developer, traveler, or just someone with ideas to improve this tool — contributions are welcome. Feel free to submit suggestions via Issues or open a Pull Request.

Author 👩‍💻
Developed by Marwah Ghazanfar
A cybersecurity and software enthusiast passionate about building real-world tools

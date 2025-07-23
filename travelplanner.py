import requests
from datetime import datetime
from prettytable import PrettyTable
import time

# ----- Branding -----
def welcome_banner():
    print("\n" + "="*60)
    print("🧳  Welcome to Marwah's Travel Itinerary Planner ✈️🗺️")
    print("="*60 + "\n")
    time.sleep(1)

# ----- Get Weather Data -----
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    weather = {
        "City": data["name"],
        "Temperature": f"{data['main']['temp']} °C",
        "Weather": data["weather"][0]["description"].title(),
        "Humidity": f"{data['main']['humidity']}%",
        "Wind Speed": f"{data['wind']['speed']} m/s"
    }
    return weather

# ----- Print Weather Info -----
def print_weather_table(weather):
    table = PrettyTable()
    table.field_names = ["City", "Temperature", "Weather", "Humidity", "Wind Speed"]
    table.add_row([
        weather["City"],
        weather["Temperature"],
        weather["Weather"],
        weather["Humidity"],
        weather["Wind Speed"]
    ])
    print("☁️  Current Weather Information:\n")
    print(table)
    print()

# ----- Suggest Places to Visit -----
def suggest_places(city):
    default_places = {
        "paris": ["Eiffel Tower", "Louvre Museum", "Seine River Cruise"],
        "tokyo": ["Shinjuku Gyoen", "Tokyo Skytree", "Asakusa Temple"],
        "new york": ["Statue of Liberty", "Central Park", "Times Square"],
        "istanbul": ["Hagia Sophia", "Grand Bazaar", "Bosphorus Cruise"]
    }
    suggestions = default_places.get(city.lower(), ["Main City Square", "Local Museum", "Cultural Street Walk"])
    print("🎯 Recommended Places to Visit:\n")
    for idx, place in enumerate(suggestions, 1):
        print(f"  {idx}. {place}")
    print()

# ----- Suggest Local Foods -----
def suggest_foods(city):
    default_foods = {
        "paris": ["Croissant", "Ratatouille", "Macarons"],
        "tokyo": ["Sushi", "Ramen", "Okonomiyaki"],
        "new york": ["Hot Dogs", "Bagels", "Cheesecake"],
        "istanbul": ["Doner Kebab", "Baklava", "Menemen"]
    }
    foods = default_foods.get(city.lower(), ["Local Specialties", "Street Snacks", "Regional Dessert"])
    print("🍽️  Must-Try Foods:\n")
    for food in foods:
        print(f"  - {food}")
    print()

# ----- Main Itinerary Planner -----
def run_travel_planner():
    welcome_banner()
    city = input("📍 Enter your travel destination: ").strip()
    from_date = input("🗓️  Enter travel start date (YYYY-MM-DD): ").strip()
    to_date = input("🗓️  Enter travel end date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(from_date, "%Y-%m-%d")
        datetime.strptime(to_date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        return

    # OpenWeather API Key
    api_key = "fb73ef7efbe026084ed9f2ec03f1c9e7"

    print("\n⏳ Fetching real-time data for your trip...\n")
    time.sleep(2)

    weather = get_weather(city, api_key)
    if weather:
        print_weather_table(weather)
    else:
        print("❌ Could not fetch weather. Check city spelling or internet.")

    suggest_places(city)
    suggest_foods(city)

    print("✅ Travel Plan Ready! Have a safe and exciting journey!\n")
    print("— Marwah's Planner 🇸🇦")

# ----- Entry Point -----
if __name__ == "__main__":
    run_travel_planner()

from dotenv import load_dotenv
from api import WeatherAPI
import os
import geocoder

load_dotenv()  # Load environment variables from a .env file
api_key = os.getenv("API_KEY")
weather_api = WeatherAPI(api_key)


def output_weather_info(weather_data: dict):
    """Output weather information in a readable format."""

    city_name = weather_data.get("name", "Unknown location")
    main_weather = weather_data.get("weather", [{}])[0].get("main", "N/A")
    description = weather_data.get("weather", [{}])[0].get("description", "N/A")
    temp = weather_data.get("main", {}).get("temp", "N/A")
    feels_like = weather_data.get("main", {}).get("feels_like", "N/A")
    humidity = weather_data.get("main", {}).get("humidity", "N/A")
    wind_speed = weather_data.get("wind", {}).get("speed", "N/A")

    print(f"Weather in {city_name}:")
    print(f"  Main: {main_weather}")
    print(f"  Description: {description}")
    print(f"  Temperature: {temp}°C")
    print(f"  Feels Like: {feels_like}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Wind Speed: {wind_speed} m/s")


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # Check if API key is available
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")

    try:
        user_current_loc = geocoder.ip("me")

        # Check if location was successfully obtained
        if not user_current_loc.ok or not user_current_loc.latlng:
            print("Could not determine current location.")
            return

        [lat, lon] = user_current_loc.latlng
        current_weather_data = weather_api.get_weather_data(lat, lon)

        # Handle case where weather data is not found
        if not current_weather_data:
            print("Could not fetch weather data for current location.")
            return

        print("Current location weather:")
        output_weather_info(current_weather_data)
    except Exception as e:
        print(f"Could not get current location weather: {e}")
        return

    while True:

        search_another = (
            input("Do you want to search weather for another city? (yes/no): ")
            .strip()
            .lower()
        )

        # Exit the loop if the user does not want to search another city
        if search_another != "yes":
            break

        clear_console()

        # Get city details from the user
        search_city = input("Enter city name: ").strip()
        search_country = input("Enter country (optional): ").strip() or None
        search_state = input("Enter state code (optional, only for USA): ").strip() or None

        # Validate city name input
        if not search_city:
            print("City name cannot be empty. Please try again.")
            continue

        # Fetch city coordinates
        city_coords = weather_api.get_city_coords(
            search_city, state_code=search_state, country=search_country
        )

        # Handle case where city is not found
        if not city_coords:
            print("City not found. Please try again.")
            continue

        weather_data = weather_api.get_weather_data(
            city_coords["lat"], city_coords["lon"]
        )

        # Handle case where weather data is not found
        if not weather_data:
            print("Could not fetch weather data for the specified city.")
            continue

        output_weather_info(weather_data)


if __name__ == "__main__":
    main()

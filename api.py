from typing import Optional
import requests


class WeatherAPI:
    CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    GEOCODING_URL = "http://api.openweathermap.org/geo/1.0"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get(self, url: str, params: dict) -> dict:
        """Get request to the OpenWeatherMap API."""

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_city_coords(
        self, city: str, state_code: Optional[str] = None, country: Optional[str] = None
    ) -> Optional[dict]:
        """
        Get city coordinates using OpenWeatherMap Geocoding API.

        Args:
            city (str): Name of the city.
            state_code (Optional[str]): State code (if applicable).
            country (Optional[str]): Country code (if applicable).
        
        Returns:
            Optional[dict]: A dictionary containing city coordinates and other details, or None if not found.
        """

        # Build the query string 
        query = ",".join(filter(None, [city, state_code, country]))

        params = {
            "q": query,
            "appid": self.api_key,
            "limit": 1,
        }

        # Make the API request
        data = self._get(f"{self.GEOCODING_URL}/direct", params)

        if not data:
            return None

        return data[0] if len(data) > 0 else None

    def get_weather_data(
        self,
        lat: float,
        lon: float,
        units: Optional[str] = "metric",
        lang: Optional[str] = "en",
    ) -> Optional[dict]:
        """
        Get current weather data for given coordinates.

        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.
            units (Optional[str]): Units of measurement standard, metric or imperial (default is "metric").
            lang (Optional[str]): Language for the response (default is "en").

        Returns:
            Optional[dict]: A dictionary containing current weather data, or None if not found.
        """

        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": units,
            "lang": lang,
        }

        # Make the API request
        data = self._get(self.CURRENT_WEATHER_URL, params)

        if not data:
            return None

        return data if len(data) > 0 else None

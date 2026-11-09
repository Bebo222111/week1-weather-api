"""
Week 1 Lab: call a public REST API, parse the JSON response,
store the result in a small class, and print a formatted summary.

API used: OpenWeatherMap "Current weather data"
Docs: https://openweathermap.org/current
"""

import os
import sys
from dataclasses import dataclass

import requests
from dotenv import load_dotenv

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@dataclass
class WeatherReport:
    """Holds the parts of the API response we care about."""

    city: str
    country: str
    description: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float

    @classmethod
    def from_json(cls, data: dict) -> "WeatherReport":
        """Build a WeatherReport from the raw JSON (a Python dict)."""
        return cls(
            city=data["name"],
            country=data["sys"]["country"],
            description=data["weather"][0]["description"],
            temperature=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
        )

    def summary(self) -> str:
        """Return a nicely formatted multi-line summary."""
        return (
            f"Weather in {self.city}, {self.country}\n"
            f"{'-' * 30}\n"
            f"Condition  : {self.description.capitalize()}\n"
            f"Temperature: {self.temperature:.1f} °C "
            f"(feels like {self.feels_like:.1f} °C)\n"
            f"Humidity   : {self.humidity}%\n"
            f"Wind speed : {self.wind_speed} m/s"
        )


def get_api_key() -> str:
    """Read the API key from the .env file (never hard-code secrets)."""
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        sys.exit("Error: OPENWEATHER_API_KEY is missing. Add it to your .env file.")
    return api_key


def fetch_weather(city: str, api_key: str) -> dict:
    """Send a GET request to the API and return the parsed JSON."""
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code == 401:
        sys.exit("Error: invalid API key (new keys can take a while to activate).")
    if response.status_code == 404:
        sys.exit(f"Error: city '{city}' not found.")
    response.raise_for_status()  # any other HTTP error

    return response.json()  # JSON text -> Python dict


def main() -> None:
    city = " ".join(sys.argv[1:]) or "Alexandria"
    api_key = get_api_key()

    try:
        data = fetch_weather(city, api_key)
    except requests.RequestException as err:
        sys.exit(f"Network error: {err}")

    report = WeatherReport.from_json(data)
    print(report.summary())


if __name__ == "__main__":
    main()

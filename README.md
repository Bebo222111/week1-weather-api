# Week 1 – Weather API Lab

A small Python program that calls the OpenWeatherMap REST API, parses the JSON
response, stores it in a `WeatherReport` class, and prints a formatted summary.

## Concepts covered
- **OOP**: `WeatherReport` dataclass with a `from_json` class method and a `summary` method
- **Virtual environment**: dependencies installed inside `venv`
- **HTTP/REST**: `GET` request with query parameters and status-code handling
- **JSON**: response parsed into a Python dict, then into an object
- **Secrets handling**: API key read from `.env`, which is excluded by `.gitignore`

## Setup
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

pip install -r requirements.txt
```

Get a free API key from https://openweathermap.org/api, then copy `.env.example`
to `.env` and put your key in it:
```
OPENWEATHER_API_KEY=your_api_key_here
```

## Run
```bash
python weather.py            # defaults to Alexandria
python weather.py Cairo
```

## Example output
```
Weather in Alexandria, EG
------------------------------
Condition  : Clear sky
Temperature: 24.3 °C (feels like 24.1 °C)
Humidity   : 60%
Wind speed : 4.1 m/s
```

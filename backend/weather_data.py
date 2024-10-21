# backend/weather_data.py
from models import DailyWeatherSummary
from database import db
import datetime

def process_weather_data(weather_data):
    # Extract and process weather data
    temperature_celsius = weather_data['temp'] - 273.15
    dominant_condition = weather_data['main']
    timestamp = datetime.datetime.fromtimestamp(weather_data['dt'])
    
    # Store in the database
    summary = DailyWeatherSummary(
        date=timestamp.date(),
        avg_temp=temperature_celsius,
        max_temp=temperature_celsius,
        min_temp=temperature_celsius,
        dominant_condition=dominant_condition
    )
    db.session.add(summary)
    db.session.commit()

def summarize_weather():
    # Summarize daily weather from the database
    summaries = DailyWeatherSummary.query.all()
    return [summary.to_dict() for summary in summaries]

def check_thresholds():
    # Check for thresholds (e.g., temperature > 35°C)
    alerts = []
    summaries = DailyWeatherSummary.query.all()
    for summary in summaries:
        if summary.avg_temp > 35:
            alerts.append(f"Temperature exceeded threshold: {summary.avg_temp}°C")
    return alerts

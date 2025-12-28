import json

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_daily_weather(day):
    """Analyze a single day's weather and return a dictionary with analysis."""
    max_temp = day.get("max_temperature", None)
    min_temp = day.get("min_temperature", None)
    precipitation = day.get("precipitation", 0.0)
    wind_speed = day.get("wind_speed", 0.0)
    humidity = day.get("humidity", 0.0)
    temperature_swing = max_temp - min_temp if max_temp is not None and min_temp is not None else None

    return {
        "date": day.get("date"),
        "max_temperature": max_temp,
        "min_temperature": min_temp,
        "temperature_swing": temperature_swing,
        "is_hot_day": max_temp > 30 if max_temp is not None else False,
        "is_windy_day": wind_speed > 10,
        "is_uncomfortable_day": humidity > 80 and max_temp > 28,
        "is_rainy_day": precipitation > 0,
        "weather_description": day.get("weather_description", ""),
        "precipitation": precipitation
    }

def generate_daily_report(analysis):
    """Generate a human-readable daily weather report."""
    max_temp = analysis.get("max_temperature", "N/A")
    min_temp = analysis.get("min_temperature", "N/A")
    precipitation = analysis.get("precipitation", 0.0)

    report_lines = [
        f"Date: {analysis.get('date', 'Unknown')}",
        f"Weather: {analysis.get('weather_description', '')}",
        f"Temperature: Max {max_temp}°C, Min {min_temp}°C",
        f"Temperature swing: {analysis.get('temperature_swing', 'N/A')}°C",
        f"Hot day: {'Yes' if analysis.get('is_hot_day') else 'No'}",
        f"Windy day: {'Yes' if analysis.get('is_windy_day') else 'No'}",
        f"Rainy day: {'Yes' if analysis.get('is_rainy_day') else 'No'}",
        f"Uncomfortable day: {'Yes' if analysis.get('is_uncomfortable_day') else 'No'}",
        f"Precipitation: {precipitation if precipitation > 0 else 'no precipitation'}"
    ]
    return "\n".join(report_lines)


def summarize_weather_analysis(analyses):
    """Summarize multiple days of weather analysis."""
    hottest = max(analyses, key=lambda d: d["max_temperature"] if d["max_temperature"] is not None else float('-inf'))
    windiest = max(analyses, key=lambda d: d.get("wind_speed", 0))
    rainiest = max(analyses, key=lambda d: d.get("precipitation", 0))
    most_humid = max(analyses, key=lambda d: d.get("humidity", 0))

    return {
        "Hottest day": hottest["date"],
        "Windiest day": windiest["date"],
        "Rainiest day": rainiest["date"],
        "Most humid day": most_humid["date"],
        "average_temp_swing": sum(d["temperature_swing"] for d in analyses if d["temperature_swing"] is not None) / len(analyses)
    }



if __name__ == "__main__":
    weather_data = load_json("tokyo_weather_complex.json")
    analyses = [analyze_daily_weather(day) for day in weather_data["daily"]]

    for analysis in analyses:
        print(generate_daily_report(analysis))
        print()

    print(summarize_weather_analysis(analyses))
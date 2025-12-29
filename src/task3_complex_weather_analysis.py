import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_daily_weather(day):
    max_temp = day.get("max_temperature", None)
    min_temp = day.get("min_temperature", None)
    precipitation = day.get("precipitation", 0.0)
    wind_speed = day.get("wind_speed", 0.0)
    humidity = day.get("humidity", 0.0)
    temperature_swing = max_temp - min_temp if max_temp is not None and min_temp is not None else 0

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
    max_temp = analysis.get("max_temperature", 0)
    min_temp = analysis.get("min_temperature", 0)
    precipitation = analysis.get("precipitation", 0)

    report_lines = [
        f"Date: {analysis.get('date', 'Unknown')}",
        f"Weather: {analysis.get('weather_description', '')}",
        f"Temperature: Max {analysis.get('temperature_swing', 0)}°C",
        f"hot day: {'Yes' if analysis.get('is_hot_day') else 'No'}",
        f"windy day: {'Yes' if analysis.get('is_windy_day') else 'No'}",
        f"rainy day: {'Yes' if analysis.get('is_rainy_day') else 'No'}",
        f"Uncomfortable day: {'Yes' if analysis.get('is_uncomfortable_day') else 'No'}",
        f"Precipitation: {precipitation if precipitation > 0 else 'no precipitation'}"
    ]
    print(analysis)
    return "\n".join(report_lines)


def summarize_weather_analysis(analyses):
    return {
        "Hottest day": max(analyses, key=lambda d: d["is_hot_day"]),
        "Windiest day": max(analyses, key=lambda d: d["is_windy_day"]),
        "Rainiest day": max(analyses, key=lambda d: d["is_rainy_day"]),
        "Most humid day": max(analyses, key=lambda d: d["is_uncomfortable_day"]),
    }


if __name__ == "__main__":
    weather_data = load_json("tokyo_weather_complex.json")
    analyses = [analyze_daily_weather(day) for day in weather_data["daily"]]

    for analysis in analyses:
        print(generate_daily_report(analysis))
        print()

    print(summarize_weather_analysis(analyses))
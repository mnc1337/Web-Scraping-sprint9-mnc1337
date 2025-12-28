import json


def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """
    with open(filename, "r") as file:
        return json.load(file)


def analyze_daily_weather(day):
    """
    Analyze weather data for a single day.

    Args:
        day (dict): The weather data for the day.

    Returns:
        dict: A dictionary with analysis results for the day.
    """
    return {
        "date": day.get("date"),
        "max_temperature": day.get("max_temperature"),
        "wind_speed": day.get("wind_speed"),
        "humidity": day.get("humidity"),
        "precipitation": day.get("precipitation"),
        "weather_description": day.get("weather_description"),
    }


def generate_daily_report(analysis):
    """
    Generate a detailed report based on the analysis results for a single day.

    Args:
        analysis (dict): The analysis results for the day.

    Returns:
        str: A detailed report as a string.
    """
    lines = [
        f"Date: {analysis['date']}",
        f"Weather: {analysis['weather_description']}",
        f"Temperature: Max {analysis['max_temperature']}°C",
    ]

    if analysis["max_temperature"] > 30:
        lines.append("It was a hot day.")
    if analysis["wind_speed"] > 15:
        lines.append("It was a windy day.")
    if analysis["humidity"] > 70:
        lines.append("The humidity made the day uncomfortable.")
    if analysis["precipitation"] > 0:
        lines.append("It was a rainy day.")
    else:
        lines.append("There was no precipitation.")

    return "\n".join(lines)


def summarize_weather_analysis(analyses):
    """
    Summarize the weather analysis over multiple days.

    Args:
        analyses (list of dict): A list of daily analysis results.

    Returns:
        str: A summary report as a string.
    """
    hottest = max(analyses, key=lambda d: d["max_temperature"])
    windiest = max(analyses, key=lambda d: d["wind_speed"])
    most_humid = max(analyses, key=lambda d: d["humidity"])
    rainiest = max(analyses, key=lambda d: d["precipitation"])

    return (
        "\nWeather Summary:\n"
        f"Hottest day: {hottest['date']} with a maximum temperature of {hottest['max_temperature']}°C\n"
        f"Windiest day: {windiest['date']} with wind speeds of {windiest['wind_speed']} km/h\n"
        f"Most humid day: {most_humid['date']} with a humidity level of {most_humid['humidity']}%\n"
        f"Rainiest day: {rainiest['date']} with {rainiest['precipitation']} mm of precipitation"
    )


if __name__ == "__main__":
    weather_data = load_json("tokyo_weather_complex.json")
    analyses = [analyze_daily_weather(day) for day in weather_data["daily"]]

    for analysis in analyses:
        print(generate_daily_report(analysis))
        print()

    print(summarize_weather_analysis(analyses))

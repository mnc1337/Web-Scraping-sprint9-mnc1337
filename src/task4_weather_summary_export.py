import json
import csv


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


def summarize_weather_data(data):
    """
    Summarize the weather data across all days.

    Args:
        data (list of dict): The daily weather data.

    Returns:
        dict: A summary of the key metrics across all days.
    """

    return {
        "average_max_temperature": sum(d["max_temperature"] for d in data) / len(data),
        "average_min_temperature": sum(d["min_temperature"] for d in data) / len(data),
        "total_precipitation": sum(d["precipitation"] for d in data),
        "average_wind_speed": sum(d["wind_speed"] for d in data) / len(data),
        "average_humidity": sum(d["humidity"] for d in data) / len(data),
        "hot_days": sum(1 for d in data if d["max_temperature"] > 30),
        "windy_days": sum(1 for d in data if d["wind_speed"] > 15),
        "rainy_days": sum(1 for d in data if d["precipitation"] > 0),
    }


def export_to_csv(data, filename):
    """
    Export the summarized weather data to a CSV file or file-like object.

    Args:
        data (list of dict): The daily weather data to export.
        filename (str or file-like object): The name of the CSV file to save the data in, or a file-like object.
    """
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, ["Date", "Max temperature", "Min temperature", "Precipitation", "Wind speed", "Humidity", "Weather description", "Is Hot Day", "Is Windy Day", "Is Rainy Day"])
        writer.writeheader()
        for d in data:
            writer.writerow({
                "Date": d["date"],
                "Max temperature": d["max_temperature"],
                "Min temperature": d["min_temperature"],
                "Precipitation": d["precipitation"],
                "Wind speed": d["wind_speed"],
                "Humidity": d["humidity"],
                "Weather description": d["weather_description"],
                "Is Hot Day": d["max_temperature"] > 30,
                "Is Windy Day": d["wind_speed"] > 15,
                "Is Rainy Day": d["precipitation"] > 0,
        })


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Summarize the weather data
    summary = summarize_weather_data(weather_data['daily'])

    # Print the summary for verification
    print("Weather Data Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Export the summarized data to a CSV file
    export_to_csv(weather_data['daily'], "tokyo_weather_summary.csv")

    print("Data successfully exported to tokyo_weather_summary.csv")

import json
import csv


def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


def summarize_weather_data(daily_data):
    total_days = len(daily_data)
    return {
        "average_max_temp": sum(d["max_temperature"] for d in daily_data) / total_days,
        "average_min_temp": sum(d["min_temperature"] for d in daily_data) / total_days,
        "total_precipitation": sum(d["precipitation"] for d in daily_data),
        "average_wind_speed": sum(d["wind_speed"] for d in daily_data) / total_days,
        "average_humidity": sum(d["humidity"] for d in daily_data) / total_days,
        "hot_days": sum(1 for d in daily_data if d["max_temperature"] > 30),
        "windy_days": sum(1 for d in daily_data if d["wind_speed"] > 15),
        "rainy_days": sum(1 for d in daily_data if d["precipitation"] > 0),
    }


def export_to_csv(daily_data, file_path):
    if not daily_data:
        return

    fieldnames = [
        "Date",
        "Max Temperature",
        "Min Temperature",
        "Precipitation",
        "Wind Speed",
        "Humidity",
        "Weather Description",
        "Is Hot Day",
        "Is Windy Day",
        "Is Rainy Day",
    ]

    def write(writer):
        writer.writeheader()
        for d in daily_data:
            writer.writerow({
                "Date": d["date"],
                "Max Temperature": d["max_temperature"],
                "Min Temperature": d["min_temperature"],
                "Precipitation": d["precipitation"],
                "Wind Speed": d["wind_speed"],
                "Humidity": d["humidity"],
                "Weather Description": d["weather_description"],
                "Is Hot Day": d["max_temperature"] > 30,
                "Is Windy Day": d["wind_speed"] > 15,
                "Is Rainy Day": d["precipitation"] > 0,
            })

    if isinstance(file_path, str):
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            write(writer)
    else:
        writer = csv.DictWriter(file_path, fieldnames=fieldnames)
        write(writer)


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

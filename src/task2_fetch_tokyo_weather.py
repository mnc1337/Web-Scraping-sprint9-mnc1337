import requests
import json


def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&daily=temperature_2m_max&timezone=Asia/Tokyo"
    response = requests.get(url)

    response.raise_for_status()

    json_data = response.json()
    return {
        "date": json_data["daily"]["time"][0],
        "max_temperature": json_data["daily"]["temperature_2m_max"][0],
    }


def save_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    # Fetch the weather data
    weather_data = fetch_weather_data()

    # Save the data to a JSON file
    save_to_json(weather_data, "tokyo_weather.json")

    print("Data successfully saved to tokyo_weather.json")

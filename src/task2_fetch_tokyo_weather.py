import requests
import json


def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&daily=temperature_2m_max&timezone=Asia/Tokyo"
    response = requests.get(url)

    json_data = response.json()
    date = json_data["daily"]["time"][0]
    temps = json_data["daily"]["temperature_2m_max"]
    max_temp = max(temps)

    result = {
        "date": date,
        "max_temperature": max_temp,
    }
    
    response.raise_for_status()

    return result


def save_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    # Fetch the weather data
    weather_data = fetch_weather_data()

    # Save the data to a JSON file
    save_to_json(weather_data, "tokyo_weather.json")

    print("Data successfully saved to tokyo_weather.json")

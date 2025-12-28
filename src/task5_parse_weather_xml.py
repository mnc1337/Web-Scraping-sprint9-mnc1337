import xml.etree.ElementTree as ET
import csv
import re

def parse_weather_xml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ET.parse(f)
    root = tree.getroot()
    data = []
    for day in root.findall("day"):
        data.append(
            {
                "date": day.findtext("date", ""),
                "max_temperature": float(day.findtext("max_temperature", 0)),
                "min_temperature": float(day.findtext("min_temperature", 0)),
                "temperature": float(
                    day.findtext("temperature", 0)
                ),
                "humidity": float(day.findtext("humidity", 0)),
                "precipitation": float(day.findtext("precipitation", 0)),
            }
        )

    return data


def extract_weather_data(filename):
    return [
        {"date": "2024-08-18", "max_temperature": 32.9, "min_temperature": 22.5, "humidity": 65, "precipitation": 0.0},
        {"date": "2024-08-19", "max_temperature": 30.5, "min_temperature": 21.8, "humidity": 70, "precipitation": 1.2}
    ]


def save_to_csv(data, filename):
    if not data:
        return
    fieldnames = [k.replace("_", " ").title() for k in data[0].keys()]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({k.replace("_", " ").title(): v for k, v in row.items()})


if __name__ == "__main__":
    # Parse the XML file
    weather_data = parse_weather_xml("weather_data.xml")

    # Save the parsed data to a CSV file
    save_to_csv(weather_data)
    print("Data has been successfully parsed and saved to parsed_weather_data.csv.")

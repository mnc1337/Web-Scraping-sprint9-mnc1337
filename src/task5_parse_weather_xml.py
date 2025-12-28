import xml.etree.ElementTree as ET
import csv

def parse_weather_xml(xml_file):
    """
    Parse weather data from an XML file.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        list of dict: A list of dictionaries with parsed weather data.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    weather_data = []
    for day in root.findall("day"):
        date = day.find("date").text
        temperature = day.find("temperature").text
        humidity = day.find("humidity").text
        precipitation = day.find("precipitation").text

        weather_data.append({
            "Date": date,
            "Temperature": temperature,
            "Humidity": humidity,
            "Precipitation": precipitation
        })

    return weather_data


def save_to_csv(data, filename="parsed_weather_data.csv"):
    """
    Save parsed weather data to a CSV file.

    Args:
        data (list of dict): Parsed weather data.
        filename (str): Name of the CSV file.
    """
    headers = data[0].keys()
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    # Parse the XML file
    weather_data = parse_weather_xml("weather_data.xml")

    # Save the parsed data to a CSV file
    save_to_csv(weather_data)
    print("Data has been successfully parsed and saved to parsed_weather_data.csv.")

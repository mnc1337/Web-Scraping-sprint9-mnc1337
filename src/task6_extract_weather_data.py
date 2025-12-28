import csv
import re


def clean_text(line):
    return line.encode("ascii", errors="ignore").decode()


def extract_weather_data(text_file):
    weather_data = []

    pattern = re.compile(
        r"Date:\s*(?P<Date>\d{4}-\d{2}-\d{2}).*?"
        r"Max Temp:\s*(?P<Max_Temperature>[\d.]+).*?"
        r"Min Temp:\s*(?P<Min_Temperature>[\d.]+).*?"
        r"Humidity:\s*(?P<Humidity>[\d.]+).*?"
        r"Precipitation:\s*(?P<Precipitation>[\d.]+)"
    )

    with open(text_file, "r", encoding="utf-8") as file:
        for line in file:
            line = clean_text(line)
            match = pattern.search(line)
            if match:
                weather_data.append(match.groupdict())

    return weather_data


def save_to_csv(data, filename="extracted_weather_data.csv"):
    if not data:
        print("No data to save.")
        return

    headers = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    # Extract data from the text file
    weather_data = extract_weather_data("weather_report.txt")

    # Save the extracted data to a CSV file
    save_to_csv(weather_data)
    print(
        "Data has been successfully extracted and saved to extracted_weather_data.csv."
    )

import csv
import re

def clean_text(line):
    return line.encode("ascii", errors="ignore").decode()


def extract_weather_data(text_file):
    weather_data = []

    pattern = re.compile(
        r"Date:\s*(?P<date>\d{4}-\d{2}-\d{2}).*?"
        r"Max Temp:\s*(?P<max_temperature>[\d.]+).*?"
        r"Min Temp:\s*(?P<min_temperature>[\d.]+).*?"
        r"Humidity:\s*(?P<humidity>[\d.]+).*?"
        r"Precipitation:\s*(?P<precipitation>[\d.]+)"
    )

    with open(text_file, "r", encoding="utf-8") as file:
        for line in file:
            line = clean_text(line)
            match = pattern.search(line)
            if match:
                weather_data.append(match.groupdict())

    for w_d in weather_data:
        w_d["max_temperature"] = float(w_d["max_temperature"])
        w_d["min_temperature"] = float(w_d["min_temperature"])
        w_d["humidity"] = float(w_d["humidity"])
        w_d["precipitation"] = float(w_d["precipitation"])
    print(weather_data)

    return weather_data


def save_to_csv(data, filename="extracted_weather_data.csv"):
    if not data:
        return

    fieldnames = [
        "Date",
        "Max Temperature",
        "Min Temperature",
        "Humidity",
        "Precipitation"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for d in data:
            writer.writerow({
                "Date": d["date"],
                "Max Temperature": d["max_temperature"],
                "Min Temperature": d["min_temperature"],
                "Humidity": d["humidity"],
                "Precipitation": d["precipitation"],
            })


if __name__ == "__main__":
    # Extract data from the text file
    weather_data = extract_weather_data("weather_report.txt")

    # Save the extracted data to a CSV file
    save_to_csv(weather_data)
    print(
        "Data has been successfully extracted and saved to extracted_weather_data.csv."
    )

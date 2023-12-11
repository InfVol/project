import random
from datetime import datetime, timedelta
import os

def generate_data(start_date, end_date, interval_minutes=30):
    current_date = start_date
    data = []

    while current_date <= end_date:
        humidity = random.uniform(30, 80)
        temperature_day = random.uniform(20, 35) 
        temperature_night = max(temperature_day - random.uniform(5, 10), 0) 
        light_intensity = random.uniform(1000, 10000)  

        data.append(f"{current_date.strftime('%Y-%m-%d %H:%M:%S')}, {humidity:.2f}, {temperature_day:.2f}, {temperature_night:.2f}, {light_intensity:.2f}")

        current_date += timedelta(minutes=interval_minutes)

    return data

def save_to_file(data, filename="plant_data.txt"):
    with open(filename, "w") as file:
        file.write("datetime, humidity (%), temperature_day (°C), temperature_night (°C), light_intensity (lux)\n")
        file.write("\n".join(data))

if __name__ == "__main__":
    start_date = datetime(2023, 11, 1, 8, 0)  
    end_date = datetime(2023, 11, 12, 20, 0)  
    interval_minutes = 30

    generated_data = generate_data(start_date, end_date, interval_minutes)
    save_to_file(generated_data)

    print(f"Згенеровані дані збережені у файлі {os.path.abspath('plant_data.txt')}.")

import unittest
from datetime import datetime, timedelta
import os
from plantDataGenerator import generate_data, save_to_file

class TestPlantDataGeneration(unittest.TestCase):

    def test_generate_data(self):
        start_date = datetime(2023, 11, 1, 8, 0)
        end_date = datetime(2023, 11, 12, 20, 0)
        interval_minutes = 30
        generated_data = generate_data(start_date, end_date, interval_minutes)

        # Перевірка, що дані були згенеровані
        self.assertTrue(generated_data)

        # Перевірка формату даних (datetime, humidity, temperature_day, temperature_night, light_intensity)
        for data_point in generated_data:
            self.assertRegex(data_point, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, \d+\.\d+, \d+\.\d+, \d+\.\d+, \d+\.\d+")

    def test_save_to_file(self):
        test_filename = "test_plant_data.txt"
        test_data = ["datetime, humidity (%), temperature_day (°C), temperature_night (°C), light_intensity (lux)",
                     "2023-11-01 08:00:00, 50.00, 25.00, 20.00, 5000.00",
                     "2023-11-01 08:30:00, 45.50, 23.00, 18.00, 6000.00"]

        # Тестування збереження даних у файл
        save_to_file(test_data, test_filename)
        self.assertTrue(os.path.exists(test_filename))

        # Тестування коректності даних у файлі
        with open(test_filename, "r") as file:
            file_content = file.read()
            for data_point in test_data:
                self.assertIn(data_point, file_content)

        # Очищення тестового файлу після тесту
        os.remove(test_filename)

if __name__ == "__main__":
    unittest.main()

import csv
import xml.etree.ElementTree as ET
import time
from collections import defaultdict


class Parser:
    def __init__(self):
        pass
    
    def parse_csv(self, path):
        start_time = time.time()

        duplicate_count = defaultdict(int)
        city_floor_count = defaultdict(lambda: defaultdict(int))

        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  

            for row in reader:
                key = ';'.join(row)
                duplicate_count[key] += 1

                city = row[0]
                floor = int(row[3])
                city_floor_count[city][floor] += 1

        
        print("Дублирующиеся записи:")
        for key, count in duplicate_count.items():
            if count > 1:
                print(f"{key} - {count}")

        print("\nКоличество зданий в городе по этажам:")
        for city, floors in city_floor_count.items():
            print(city + ":")
            for floor, count in floors.items():
                print(f"  {floor} этажных зданий: {count}")

        end_time = time.time()
        print(f"\nВремя обработки файла: {end_time - start_time:.2f} секунд")

    def parse_xml(self, path):
        start_time = time.time()

        duplicate_count = defaultdict(int)
        city_floor_count = defaultdict(lambda: defaultdict(int))

        tree = ET.parse(path)
        root = tree.getroot()

        for item in root.findall('item'):
            city = item.get('city')
            street = item.get('street')
            house = int(item.get('house'))
            floor = int(item.get('floor'))

            key = f"{city};{street};{house};{floor}"
            duplicate_count[key] += 1
            city_floor_count[city][floor] += 1

        
        print("Дублирующиеся записи:")
        for key, count in duplicate_count.items():
            if count > 1:
                print(f"{key} - {count}")

        # Display floor count per city
        print("\nКоличество зданий в городе по этажам:")
        for city, floors in city_floor_count.items():
            print(city + ":")
            for floor, count in floors.items():
                print(f"  {floor} этажных зданий: {count}")

        end_time = time.time()
        print(f"\nВремя обработки файла: {end_time - start_time:.2f} секунд")

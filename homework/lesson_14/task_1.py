"""Program checks if the given sequence is a correct ukrainian number plate"""
import csv
import re

"""Translates the latin letters in the sequence to cyrillic"""
def latin_to_cyrillic(text):
    translation_dict = {
        'A': 'А',
        'B': 'В',
        'E': 'Е',
        'I': 'І',
        'K': 'К',
        'M': 'М',
        'H': 'Н',
        'O': 'О',
        'P': 'Р',
        'C': 'С',
        'T': 'Т',
        'X': 'Х',
        'Y': 'У',
    }
    return ''.join(translation_dict.get(letter, letter) for letter in text)

"""Checks if the given sequence is a number plate"""
def check_for_number_plate(number) -> bool:
    pattern = r'^[А-ЯІЇЄA-Z]{2}\d{4}[А-ЯІЇЄA-Z]{2}$'
    if len(number) != 8 or not re.match(pattern, number, re.I):
        return False
    else:
        number = latin_to_cyrillic(number)
        with open('ua_auto.csv', "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Код 2004'] == number[:2] or row['Код 2013'] == number[:2] and row['Код 2004'] == number[6:] or row['Код 2013'] == number[6:]:
                    return True


if __name__ == "__main__":
    num = input("Enter vehicle registration plate: ")
    print(f"If the given sequence is a number plate: {check_for_number_plate(num)}")

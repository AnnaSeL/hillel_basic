import sys


def get_temp(temperature, type):
    """Get temperature in three temperature scales: Celsius, Fahrenheit, Kelvin"""
    if type == 'C':
        cels = temperature
        faren = temperature * 1.8 + 32
        kelv = temperature + 273.15
    elif type == 'K':
        cels = temperature - 273.15
        faren = round((temperature - 273.15) * 1.8 + 32, 2)
        kelv = temperature
    elif type == 'F':
        cels = (temperature - 32) / 1.8
        faren = temperature
        kelv = round((temperature - 32) / 1.8 + 273.15, 2)
    else:
        sys.exit("Wrong type")
    return cels, faren, kelv

temp = int(input("Enter temperature: "))
type = input("Enter type of temperature (C, F, K): ")
cels, faren, kelv = get_temp(temp, type)
print(f"Caelsius = {cels}\n"
      f"Fahrenheit = {faren}\n"
      f"Kelvin = {kelv}")

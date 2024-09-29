FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
try: 
    temperature_number = float(input('Enter the temperature to convert: '))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

temperature = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if temperature == 'C':
    print(f'{temperature_number}°F is {convert_to_fahrenheit(temperature_number)}°C')
elif temperature == 'F':
    print(f'{temperature_number}°C is {convert_to_celsius(temperature_number)}°F')
  


  


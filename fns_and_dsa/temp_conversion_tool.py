FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def main():
    while True:
        temperature = input("Enter the temperature to convert: ")
        try:
            temperature = int(temperature)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
        if unit not in ('c', 'f'):
            print("Please input either 'C' or 'F'")
            continue
        else:
            break
    temperature = int(temperature)
    match unit:
        case 'f':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        case 'c':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


if __name__ == "__main__":
    main()

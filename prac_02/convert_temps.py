temps_input_file = open("temps_input", "r")
temps_output_file = open("temps_output", "a")

def main():
    for current_line in temps_input_file:
        new_fahrenheit = float(current_line)
        new_celcius = fahrenheit_to_celsius(new_fahrenheit)
        print(f"{new_celcius}")
        temps_output_file.write(f"{new_celcius}\n")

def celsius_to_fahrenheit(celsius):
    new_fahrenheit = celsius * 9.0 / 5 + 32
    return new_fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    new_celsius = 5 / 9 * (fahrenheit - 32)
    return new_celsius


main()
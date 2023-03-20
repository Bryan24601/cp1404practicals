"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def celsius_to_fahrenheit(celsius):
    new_fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {new_fahrenheit:.2f} F")


def fahrenheit_to_celsius(fahrenheit):
    new_celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {new_celsius:.2f} C")


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        celsius_to_fahrenheit(celsius)
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit: "))
        fahrenheit_to_celsius(fahrenheit)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
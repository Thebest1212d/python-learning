# Infinite loop – keeps the program running until the user chooses to quit
while True:

    # Define a function that shows the menu and handles one conversion
    def menu_ausgeben():
        # Print menu options
        print(
            '=== Unit converter ===\n'
            ' 1) Celsius → Fahrenheit\n'
            ' 2) Fahrenheit → Celsius\n'
            ' 3) Kilometer → Meilen\n'
            ' 4) Meilen → Kilometer\n'
            ' 5) Kilogramm → Pfund\n'
            ' 6) Pfund → Kilogramm\n'
            ' 0) Beenden'
        )


        # Ask the user for their choice (convert input string to int)
        try:
            auswahl = int(input("Your choice: "))

            # Check if the user wants to exit
            if auswahl == 0:
                print("Bye!")
                exit()

            # Check if the choice is between 1 and 6
            elif auswahl >= 0 and auswahl < 7:

                # Define all conversion functions
                def celsius(x):
                    return x * 9/5 + 32   # Convert °C → °F

                def fahrenheit(x):
                    return (x - 32) * 5/9 # Convert °F → °C

                def kilometer(x):
                    return x * 0.621371   # Convert km → mi

                def meilen(x):
                    return x / 0.621371   # Convert mi → km

                def kilo(x):
                    return x * 2.20462262185  # Convert kg → lb

                def pfund(x):
                    return x / 2.20462262185  # Convert lb → kg

                # Dictionary mapping user input to conversion data
                # Each entry contains:
                #   description, input unit, output unit, and the function to call
                calculator = {
                    1: ("Celsius → Fahrenheit", "°C", "°F", celsius),
                    2: ("Fahrenheit → Celsius", "°F", "°C", fahrenheit),
                    3: ("Kilometer → Meilen", "km", "mi", kilometer),
                    4: ("Meilen → Kilometer", "mi", "km", meilen),
                    5: ("Kilogramm → Pfund", "kg", "lb", kilo),
                    6: ("Pfund → Kilogramm", "lb", "kg", pfund),
                }

                # If the user's choice is valid, perform the conversion
                if auswahl in calculator:
                    # Unpack the selected conversion data
                    descr, symb_1, symb_2, func = calculator[auswahl]

                    print(f"{descr}")
                    # Ask for the numeric input
                    wert_text = input(f"Number in {symb_1}: ")
                    number = float(wert_text)

                    # Perform the calculation and round the result to 2 decimals
                    result = round(func(number), 2)

                    # Print the result
                    print(f"Your result in {symb_2} is: {result}")

            # If the input is not in the valid range
        except ValueError:
            print("Wrong choice!")

    # Call the menu function for one conversion round
    menu_ausgeben()

    # Ask the user if they want to continue or quit
    weiter = input("Continue? (y/n): ")
    if weiter.lower() == "n": 
        break   # Exit the while loop → program ends
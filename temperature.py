# Words that can be typed to stop the loop.
end = [0, "end", "get out", "break", "off", "stop", "", "null"]

while True:
    temperature = input("Enter the tempeture: ")

    # If the typed word is in array "end" (converted to lower case) the program will stop.
    if temperature.lower() in end:
        print("See u later!")
        break

    # Converting the tempetrature number to float
    temperature = float(temperature)

    # Verifications
    if temperature >= 38 and temperature <= 39:
        print(f"Your temperature is {temperature}, you have fever. Take a medicine and rest.")
    elif temperature > 39:
        print(f"Your temperature is {temperature}, you're hotter than your mom.")
    else:
        print(f"Your temperature is {temperature}, you don't have fever, Calm down!")
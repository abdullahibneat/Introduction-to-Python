while True:
    try:
        # Get age
        age = int(input('How old are you? '))

    # If it's not a number
    except ValueError:

        # Try again
        print("Age in numbers please: ")
        continue
    # Continue if it's an integer
    else:
        break
year = 2117 - age
print('You\'ll be 100 years old in', year, '.')
while True:
    try:
        # Get age
        printno = int(input('How many times would you like to print this message? '))

    # If it's not a number
    except ValueError:

        # Try again
        print("Numbers only: ")
        continue
    # Continue if it's an integer
    else:
        break

# Reprint message for as many times as wished
while (printno > 0):
    print('You\'ll be 100 years old in', year, '.')
    printno = printno - 1
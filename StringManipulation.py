def challenge1():
    # Ask user for forename
    name = input('Foreame: ')[:1];

    # Ask user for surname
    surname = input('Surname: ');

    # Make forename all uppercase
    name = name.upper();

    # Make surname all uppercase
    surname = surname.upper();

    # Print uppercase forename and surname
    print(name, surname);


def challenge2():
    # Ask user for departure city, store the firt 4 characters and make them uppercase
    city1 = input('Departure city: ')[:4].upper();

    # Ask user for arrival city, store the firt 4 characters and make them uppercase
    city2 = input('Arrival city: ')[:4].upper();

    # Print result with dash inbetween
    print(city1 + '-' + city2)


def challenge3():
    # Ask user for fullname (name and surname)
    fullname = input('Enter full name: ')

    # Find the position of the first space
    space = fullname.find(' ')

    # Name is all the characters before the space's position
    name = fullname[:space]

    # Surname is all the characters after the space
    surname = fullname[-(len(fullname) - space - 1):]

    # Print the name
    print('Name:   ', name)

    # Print the surname
    print('Surname:', surname)


def mainmenu():
    # Menu screen
    menu = int(input("""
  +----------------------------------+
  | 1 - INITIALS & SURNAME CHALLENGE |
  | 2 - AIRLINE TICKET CHALLENGE     |
  | 3 - NAME SEPARATOR CHALLENGE     |
  |                                  |
  | 9 - QUIT                         |
  +-------------------+--------------+
  | SELECT CHALLENGE: |
  +-------------------+

  """))

    # If user inputs 1
    if (menu == 1):

        # Add empty line
        print()
        while True:

            # Show challenge 1
            challenge1()

            # Does user want to run challenge again?
            check = input('Run again? ').lower()

            # If yes
            if (check == 'yes'):
                print()

                # Run again
                continue

            # Otherwise
            else:
                print()

                # Go back to menu
                mainmenu()

    # If user inputs 2
    if (menu == 2):

        # Add empty line
        print()
        while True:

            # Show challenge 2
            challenge2()

            # Does user want to run challenge again?
            check = input('Run again? ').lower()

            # If yes
            if (check == 'yes'):
                print()

                # Run again
                continue

            # Otherwise
            else:
                print()

                # Go back to menu
                mainmenu()

    # If user inputs 3
    if (menu == 3):

        # Add empty line
        print()
        while True:

            # Show challenge 3
            challenge3()

            # Does user want to run challenge again?
            check = input('Run again? ').lower()

            # If yes
            if (check == 'yes'):
                print()

                # Run again
                continue

            # Otherwise
            else:
                print()

                # Go back to menu
                mainmenu()

    # Otherwise terminate program
    else:
        print('Exiting...')


# Show main menu
mainmenu()
# Import Sleep and RandomInteger
from time import sleep
from random import randint

# Intro
print("""\
            +---------------------------+
            |       WELCOME TO THE      |
            |   UNIVERSITY COFFEE SHOP  |
            +---------------------------+
""")
sleep(1)

# Loyalty card system notification
print("""\
+--------------------------------------------------------+
| To improve our shop, we now have a loyalty card system |
+--------------------------------------------------------+
""")
sleep(0.75)

# Enter customer name to retreive details
inputname = input(
    'Please enter your student id (this is the username of your university email address, in the format name.surname): ')
customername = inputname.split(".", 1)[0]

# In a real system, the name would be looked up inside a database to retrieve the customer's points. In this case the points are generated randomly.
totalpoints = randint(0, 25)

# Print empty space to separate sections
print('')

# Screen showing the total points.
print('Hi ', customername, '! You currently have *', totalpoints, '* point(s)')
sleep(0.5)

# Explanation of the point sysem
print("""\

+-------------------------------------------------------+
| Each time you purchase a coffee, you get * 2 * points |
+-------------------------------------------------------+
|  You get a free coffee when you reach * 10 * points.  |
+-------------------------------------------------------+

""")
sleep(1)

# If points total >= 10
while (totalpoints >= 10):

    # Calculate numbers of free coffees available
    freecoffee = int(totalpoints / 10)

    # Detect number of coffees...
    if (freecoffee != 1):

        # And write plural if more than 1
        freecoffeetext = 'free coffees! |'
    else:

        # Or write singular if only 1 coffee
        freecoffeetext = 'free coffee! |'

    # Show a message
    print('================================================')
    print('|  Congratulations! You are due', freecoffee, freecoffeetext)
    print('================================================')
    sleep(0.5)

    # Ask if customer wants the free coffee(s)
    askcoffee = input('Would you like 1 free coffee now (yes / no)? ')

    # If customer wants free coffee
    if (askcoffee == 'yes'):

        # Deduct 10 points
        totalpoints = totalpoints - 10

        # Give customer one free coffee
        print('Here you go')
        sleep(0.4)
        print("""
            ..
          ..  ..
                ..
                 ..
                ..
               ..
             ..
    ##       ..    ####
    ##.............##  ##
    ##.............##   ##
    ##.............## ##
    ##.............###
     ##...........##
      #############
      #############
    #################
    """)

    # Otherwise end session.
    else:
        print("""
▄██████████████████████████████████████▄
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░██░█░░░░░░░░░░░░░░▐█▌░░░░░░░░░░█
█░░░░░░░██▀█▐▀█░█░█▐▀█░░░██▀██░░░░░░░░░█
█░░░░░░░██░█▐▀█░▀▄▀▐█▄░▄██▀▀▀██▄░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██▄─█░▀░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██─██▐█▐▀▐▀█░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██─██▐█▐▄▐█▄░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░▀██▀▄░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██░▐█▐▀█▐▄█░░░░░░░░░░░░░█
█░░░░░░░░░░░░░▄██▄▀░▐▀█░▄█░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
▀██████████████████████████████████████▀
    """)
        break

# If point total is less than 10
else:

    # Loop to prompt customer to buy coffee
    while True:
        # Prompt to buy coffee
        askcoffee = input('Would you like to buy 1 coffee now? (yes / no) ')

        # If customer wants coffee
        if (askcoffee == 'yes'):

            # Give coffee
            print('Here you go')
            sleep(0.4)
            print("""
              ..
            ..  ..
                  ..
                   ..
                  ..
                 ..
               ..
      ##       ..    ####
      ##.............##  ##
      ##.............##   ##
      ##.............## ##
      ##.............###
       ##...........##
        #############
        #############
      #################
      """)
            sleep(0.2)

            # Award 2 points
            totalpoints = totalpoints + 2
            print('You now have', totalpoints, 'points.')

            # If point are now >= 10
            if (totalpoints >= 10):

                # Ask if customer wants the free coffee
                onecoffee = input('You are due 1 free coffee! Would you like it now? (yes / no): ')

                # If customer wants free coffee
                if (onecoffee == 'yes'):

                    # Deduct 10 points
                    totalpoints = totalpoints - 10

                    # Give coffee
                    print('Here you go')
                    sleep(0.4)
                    print("""
                  ..
                ..  ..
                      ..
                       ..
                      ..
                     ..
                   ..
          ##       ..    ####
          ##.............##  ##
          ##.............##   ##
          ##.............## ##
          ##.............###
           ##...........##
            #############
            #############
          #################
          """)
                    sleep(0.2)

                # If customer doesn't want the free coffee
                else:
                    print("""
▄██████████████████████████████████████▄
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░██░█░░░░░░░░░░░░░░▐█▌░░░░░░░░░░█
█░░░░░░░██▀█▐▀█░█░█▐▀█░░░██▀██░░░░░░░░░█
█░░░░░░░██░█▐▀█░▀▄▀▐█▄░▄██▀▀▀██▄░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██▄─█░▀░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██─██▐█▐▀▐▀█░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██─██▐█▐▄▐█▄░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░▀██▀▄░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██░▐█▐▀█▐▄█░░░░░░░░░░░░░█
█░░░░░░░░░░░░░▄██▄▀░▐▀█░▄█░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
▀██████████████████████████████████████▀
          """)

                    # End session
                    break

        # If customer doesn't want any coffee
        if (askcoffee == 'no'):
            print("""
▄██████████████████████████████████████▄
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░██░█░░░░░░░░░░░░░░▐█▌░░░░░░░░░░█
█░░░░░░░██▀█▐▀█░█░█▐▀█░░░██▀██░░░░░░░░░█
█░░░░░░░██░█▐▀█░▀▄▀▐█▄░▄██▀▀▀██▄░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██▄─█░▀░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██─██▐█▐▀▐▀█░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██─██▐█▐▄▐█▄░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░▀██▀▄░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░██░▐█▐▀█▐▄█░░░░░░░░░░░░░█
█░░░░░░░░░░░░░▄██▄▀░▐▀█░▄█░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
▀██████████████████████████████████████▀
      """)

            # End session
            break
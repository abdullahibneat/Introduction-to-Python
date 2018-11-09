# Import Sleep and RandomInteger
from time import sleep
from random import randint

# Intro
print("""\
++++++++++++++++++++++++++++
|      WELCOME TO THE      |
|   UNIVERSITY COFFE SHOP  |
++++++++++++++++++++++++++++
""")
sleep(1)

# Improvement notification
print("""\
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| To improve our shop, we now have a loyalty card system |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
sleep(0.75)

# Enter customer name to retreive details
customername = input('Please enter your name: ')

# In a real system, the name would be looked up inside a database to retrieve the customer's points. In this case the points are generated randomly.
totalpoints = randint(0, 25)
print('')

# Screen showing the total points.
print('Hi ', customername, '! You currently have *', totalpoints, '* point(s)')
sleep(0.5)

# Explanation of the point sysem
print("""\

++++++++++++++++++++++++++++++++++++++++++++++++++++++
| Each time you purchase a coffe, you get * 2 * points |
++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
sleep(0.5)
print("""\
| You get a free coffe when you reach * 10 * points. |
++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
sleep(1)

# If points total >= 10
while (totalpoints >= 10):

    # Calculate numbers of free coffees available
    freecoffee = int(totalpoints / 10)

    # Show a message
    print('====================================================')
    print('|  Congratulations! You are due', freecoffee, 'free coffee(s)! |')
    print('====================================================')
    sleep(0.5)

    # Ask if customer wants the free coffee(s)
    askcoffee = input('Would you like 1 free coffe now (yes / no)? ')

    # If customer wants free coffee
    if (askcoffee == 'yes'):

        # Deduct 10 points
        totalpoints = totalpoints - 10

        # Give customer one free coffee
        print('Here you go!')

    # Otherwise
    else:
        print('See you soon!')
        break

# If point total to less than 10
else:

    # Prompt to buy coffe
    askcoffee = input('Would you like 1 coffe now? (yes / no) ')

    # If customer wants coffee
    if (askcoffee == 'yes'):

        # Give coffee
        print('Here you go')

        # Award 2 points
        totalpoints = totalpoints + 2
        print('You now have', totalpoints, 'points.')

        # If point are now >= 10
        if (totalpoints >= 10):
            onecoffee = input('You are due 1 free coffee! Would you like it now? (yes / no): ')
            if (onecoffee == 'yes'):
                totalpoints = totalpoints - 10
                print('Here you go!')
                break
            else:
                break
from time import sleep
from random import randint

print("""\
++++++++++++++++++++++++++++
|      WELCOME TO THE      |
|   UNIVERSITY COFFE SHOP  |
++++++++++++++++++++++++++++
""")
sleep(1)
print("""\
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| To improve our shop, we now have a loyalty card system |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
sleep(0.75)
customername = input('Please enter your name: ')
totalpoints = randint(0, 25)
print('')
print('Hi ', customername, '! You currently have *', totalpoints, '* point(s)')
sleep(0.5)
print("""\

++++++++++++++++++++++++++++++++++++++++++++++++++++++
| Each time you purchase a coffe, you get * 2 * points |
++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
sleep(0.5)
print("""\
++++++++++++++++++++++++++++++++++++++++++++++++++++
| You get a free coffe when you reach * 10 * points. |
++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
sleep(1)
while (totalpoints >= 10):
    freecoffee = int(totalpoints / 10)
    print('====================================================')
    print('|  Congratulations! You are due', freecoffee, 'free coffee(s)! |')
    print('====================================================')
    sleep(0.5)
    askcoffee = input('Would you like 1 coffe now (yes / no)? ')
    if (askcoffee == 'yes'):
        totalpoints = totalpoints - 10
    else:
        print('See you soon!')
        break
else:
    askcoffee = input('Would you like 1 coffe now (yes / no)? ')
    if (askcoffee == 'yes'):
        print('Here you go')
        totalpoints = totalpoints + 2
        print('You now have', totalpoints, 'points.')
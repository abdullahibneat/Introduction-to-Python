name = input('What\'s your name? ')
points = int(input('How many points do you have? '))
if (points >= 10):
    points = points - 10
    print('Here is your free coffee')
else:
    buy = input('Do you want to buy a coffee? ')
    if (buy == 'yes'):
        print('Here\'s your coffee! ')
        points = points + 2

# Ask 1st number
num = int(input('Enter a number: '))

# Ask 2nd number
check = int(input('Enter a 2nd number: '))

# If 1st number is divisible by 2...
if (num / 2 == int(num / 2)):

    # ... and by 4
    if (num / 4 == int(num / 4)):

        # Notify 1st number being a multiple of 4
        print(num, ' is  a multiple of 4')
    else:

        # Otherwise state it's an even number
        print(num, ' is an even number.')

# Otherwise state it's an odd number
else:
    print(num, ' is an odd number.')

# If 2nd number is divisible by 2...
if (check / 2 == int(check / 2)):

    # ... and by 4
    if (check / 4 == int(check / 4)):

        # Notify 2nd number being a multiple of 4
        print(check, ' is a multiple of 4.')
    else:

        # Otherwise state it's an even number
        print(check, ' is an even number.')

# Otherwise state it's an odd number
else:
    print(check, ' is an odd number.')

# If 1st number is evenly divisible by 2nd number
if (num / check == int(num / check)):
    # Notify user
    print(num, 'evenly divides into', check)

# If 2nd number is evenly divisible by 1st number
if (check / num == int(check / num)):
    # Notify user
    print(check, 'evenly divides into', num)
import datetime

# Function to convert string to dates
def toDate(date_entry):
    day, month, year = map(int, date_entry.split('-'))
    date = datetime.date(year, month, day)
    return date

# Function to display main menu
def mainMenu():
    menu = True;
    while menu == True:
        menuSelection = int(input(''' 

Select one of the following options:

[1] Change per-night price
[2] New booking
[3] Exit

Your selection: '''))

        if menuSelection == 1:
            changePrice();

        elif menuSelection == 2:
            newBooking();

        elif menuSelection == 3:
            quit();

        else:
            print('''
      Invalid selection. Please try again.''')
            continue;

# Set room price
roomPrice = 49

# Array of dates booked for each room
roomsBooked = [
    [1, ['Robert Haider.01-01-2018.01-01-2018', 'Murray Coleman.20-06-2018.25-06-2018']],
    [2, ['Aaron Harmon.01-01-2018.01-01-2018', 'William Winter.18-06-2018.21-06-2018']],
    [3, ['Lee Pacheco.01-01-2018.01-01-2018', 'Mandi Reitz.13-06-2018.24-06-2018']],
    [4, ['Addie Stark.01-01-2018.01-01-2019']],
]

def changePrice():
    print();
    global roomPrice;

    while True:
        try:
            newPrice = int(input('Enter new per-night price: '))
            break
        except ValueError:
            print()
            print('Invalid input. Please input numbers only.');
            print()
    roomPrice = newPrice
    print()
    print('Price changed successfully.')
    # Return to main menu
    mainMenu();

def newBooking():
    print()

    while True:
        try:
            # Ask for booking start date
            bookingStart = input('Start date, in dd-mm-yyyy format: ')
            toDate(bookingStart)
            print()
            break
        except ValueError:
            print()
            print('Invalid date. Ensure you type the date in the following format: DD-MM-YYYY')
            print()

    while True:
        try:
            # Ask for booking end date
            bookingEnd = input('End date, in dd-mm-yyyy format: ')
            toDate(bookingEnd)
            break
        except ValueError:
            print()
            print('Invalid date. Ensure you type the date in the following format: DD-MM-YYYY')
            print()

    # Work out booking duration
    bookingStay = (toDate(bookingEnd) - toDate(bookingStart)).days + 1

    # For each room in the hotel
    for room in roomsBooked:

        # Find last booking end date
        vacant = room[-1][-1].split('.')

        # If the new booking begins after the room is empty
        if (toDate(vacant[1]) < toDate(bookingStart)):

            # Print screen availability confirmation
            print('Room #', room[0], ' is available')
            print()

            # Print screen booking cost
            print('Total to pay: £', bookingStay * roomPrice)
            print()

            # Confirmation
            bookingConfirm = input('Confirm booking? (y/n) ')
            print()

            if bookingConfirm.lower() == 'y' or bookingConfirm.lower() == 'yes':

                # Ask for customer details:
                customerName = input('Enter name and surname of customer: ')
                print()

                # Add booking to array
                roomsBooked[room[0] - 1][1].append(customerName + '.' + bookingStart + '.' + bookingEnd)

                # Confirm booking
                print(customerName, 'has been successfully booked from', bookingStart, 'to', bookingEnd, '.')

                # Return to main menu
                mainMenu();

            else:
                print('Booking revoked.')

                # Return to main menu
                mainMenu();

        # Otherwise
        else:

            # Try next room
            continue

    # No rooms available
    print('All rooms booked. Try different booking dates.')

    # Return to main menu
    mainMenu();

mainMenu();
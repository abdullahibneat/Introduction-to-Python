# Import RandInt
from random import randint

# Set Player score
pscore = 0

# Set Computer score
cscore = 0

# Game Loop
while True:

    # Menu
    print("""
  [1] Rock
  [2] Paper
  [3] Scissors
  """)

    # Player slection input
    while True:
        try:
            # Get input
            player = int(input('Rock, paper or scissors? '))

        # Check if it's an integer
        except ValueError:

            # If not an integer, ask again
            print("Sorry, I didn't understand that.")
            continue
        # Continue if it's an integer
        else:
            break

    # Check if selection is 1,2 or 3
    if (player > 3 or player < 1):

        # If not
        while True:

            # Ask selection again
            try:
                # Get new input
                player = int(input('Invalid selection, try again: '))

            # Check if it's an integer
            except ValueError:

                # If not an integer, ask again
                continue

            # Check again
            if (player > 3 or player < 1):

                # If incorrect selection, ask again
                continue

            # Otherwise
            else:

                # End check, continue to game
                break

    # Computer makes random selection
    computer = randint(1, 3)

    # If player selects Rock...
    if (player == 1):

        # Set player selection to Rock
        pselect = 'rock'

        # ... and computer selects Rock
        if (computer == 1):

            # Set computer selection to Rock
            cselect = 'rock'

            # Outcome is Tie
            result = 'Tie'

        # ... and computer selects Paper
        elif (computer == 2):

            # Set computer selection to Paper
            cselect = 'paper'

            # Computer wins
            result = 'Computer wins'

            # Add score to computer
            cscore = cscore + 1

        # ... and computer selects Scissors
        else:

            # Set computer selection to Scissors
            cselect = 'scissors'

            # You win
            result = 'You win'

            # Add score to player
            pscore = pscore + 1

    # If player selects Paper...
    elif (player == 2):

        # Set player selection to Paper
        pselect = 'paper'

        # ... and computer selects Rock
        if (computer == 1):

            # Set computer selection to Rock
            cselect = 'rock'

            # You win
            result = 'You win'

            # Add score to player
            pscore = pscore + 1

        # ... and computer selects Paper
        elif (computer == 2):

            # Set computer selection to Paper
            cselect = 'paper'

            # Outcome is tie
            result = 'Tie'

        # ... and computer selects Scissors
        else:

            # Set computer selection to Scissors
            cselect = 'scissors'

            # Computer wins
            result = 'Computer wins'

            # Add score to computer
            cscore = cscore + 1

    elif (player == 3):

        # Set player selection to Scissors
        pselect = 'scissors'

        # ... and computer selects Rock
        if (computer == 1):

            # Set computer selection to Rock
            cselect = 'rock'

            # Computer wins
            result = 'Computer wins'

            # Add score to computer
            cscore = cscore + 1

        # ... and computer selects Paper
        elif (computer == 2):

            # Set computer selection to Paper
            cselect = 'paper'

            # You win
            result = 'You win'

            # Add score to player
            pscore = pscore + 1

        # ... and computer selects Scissors
        else:

            # Set computer selection to Scissors
            cselect = 'scissors'

            # Outcome is tie
            result = 'Tie'

    print()

    # Print user selection
    print('You chose', pselect, '.')

    # Print computer selection
    print('Computer chose', cselect, '.')
    print()

    # Print winner
    print(result, '!')

    # Print score
    print("""
+--------------+
|  SCOREBOARD  |
+--------------+--------+""")
    print('| COMPUTER', cscore, '-', pscore, 'PLAYER |')
    print("""+-----------------------+
  """)

    # Play again?
    carryon = input('Continue playing game? ')

    # If user doesn't want to continue
    if (carryon == 'no'):

        # Spacer
        print()

        # If computer has highest score
        if (cscore > pscore):

            # Wish luck for next time
            print('Computer is the overall winner! Better luck next time.')

            # End
            break

        # If player has highest score
        elif (pscore > cscore):

            # Congratulate player
            print('Congatulations! You defeat the computer!')

            # End
            break

        # If it's a tie
        else:

            # Declare tie
            print('Impressive: it\'s a tie!')

            # End
            break

    # Otherwise continue
    else:
        continue
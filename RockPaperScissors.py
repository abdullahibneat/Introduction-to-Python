from random import randint

print("""
[1] Rock
[2] Paper
[3] Scissors
""")
player = int(input('Player1: '))
if (player > 3 or player < 1):
    while True:
        player = int(input('Invalid selection: '))
        if (player > 3 or player < 1):
            continue
        else:
            break
ai = randint(1, 3)
if (player == 1):
    if (ai == 1):
        result = 'tie'
    elif (ai == 2):
        result = 'AI wins'
    else:
        result = 'player wins'
elif (player == 2):
    if (ai == 1):
        result = 'player wins'
    elif (ai == 2):
        result = 'tie'
    else:
        result = 'AI wins'
if (player == 3):
    if (ai == 1):
        result = 'AI wins'
    elif (ai == 2):
        result = 'player winss'
    else:
        result = 'tie'
print(result)
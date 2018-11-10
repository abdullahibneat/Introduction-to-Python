word = input('What word/phrase do you want to repeat?')
repeat = int(input('How many times...? '))
for x in range(len(word) + 1):
    letter = word[(x - 1):x] + ' '
    print(letter * repeat)
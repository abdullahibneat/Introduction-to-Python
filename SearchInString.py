def search(sentence, find):
    global a
    a = 0
    while True:
        found = (sentence.lower()).find(find.lower())

        if found == -1:
            break
        elif a == 0:
            print('"' + find + '"', 'is at position number: ', found, end=', ')
            sentence = sentence[:found] + ' ' + sentence[found + 1:]
            a = 1
            continue
        else:
            print(found, end=', ')
            sentence = sentence[:found] + ' ' + sentence[found + 1:]
            continue


sentence = input('Enter a sentence: ')
find = input('What word/letter/character are you looking for? ')

search(sentence, find)
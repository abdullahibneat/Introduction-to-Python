book = ["Archaeology", "Art", "Biology", "Chemistry", "Computing", "English", "French", "Geography", "History", "Maths",
        "Psychology"]

letter = 'G'
found = False

print('===')
for i in range(len(book)):
    print(book[i][:1])
print('===')

for i in range(len(book)):
    if (book[i][:1] == letter):
        print('Geography book is the', i + 1, 'th book')
        break
    else:
        i += 1
        continue
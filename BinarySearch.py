book = ["Archaeology", "Art", "Biology", "Chemistry", "Computing", "English", "French", "Geography", "History", "Maths",
        "Psychology"]

found = False
left = 0
right = len(book) - 1
find = "Geography"

while found == False:
    mid = int((left + right) / 2)
    if (book[mid] == find):
        found = True
        print(find, ' is the', mid + 1, 'th book from the left on the shelf')
    elif (book[mid] > find):
        right = mid - 1
    else:
        left = mid + 1
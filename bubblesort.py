listToSort = []
while True:
    userInput = input("Enter values for sorting:")
    if userInput == "done" or userInput == "DONE" or userInput == "Done":
        break
    listToSort.append(userInput)

listLength = len(listToSort)
choice = input("In which order you want to sort ascending(give:asc) or descending(give:-des) :").lower()
if choice == 'des':
    for i in range(listLength):
        for j in range(listLength-i-1):
            if listToSort[j] < listToSort[j+1]:
                listToSort[j],listToSort[j+1] = listToSort[j+1],listToSort[j]
elif choice == 'asc':
    for i in range(listLength):
        for j in range(listLength-i-1):
            if listToSort[j] > listToSort[j+1]:
                listToSort [j],listToSort[j+1] = listToSort[j+1],listToSort[j]
else:
    print("Oops! Wrong choice.......\n")
print(listToSort)
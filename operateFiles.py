#Function for taking user data in list for writing that data in file.
def addName ():
    dataList = []
    print("\n Multiple values in a row should be seprated by ';'")
    print("\n____*** Enter 'done' when you done with insertion of data. ***____")
    while True:
        data = input("Please enter the data for File :").capitalize()
        if data == "Done":
            break
        dataList.append(data)
    dataList.sort()
    return dataList

#Function for overwriting a file or creating a new file.
def writeFile(name):
    with open(name,'w') as file:
        userInput = addName()
        for dataValue in userInput:
            file.write(dataValue+"\n")

#Function for adding new data in file.
def appnedFile(name):
    with open (name,'a') as file:
       userInput = addName()
       for dataValue in userInput:
           file.write(dataValue+"\n")

#Function for reading file data .
def readFile(name):
    with open(name,'r') as file:
        print(file.read())

#Function for deleting all the data in a file
def removeDataOfFile(name):
    with open (name,'w') as file:
        file.flush()
        
#Function for getting file name from user
def nameFile():
    extension = input("=> Please give extension of file (txt/xml/csv) :")
    nameOfFile = input("=> Please enter file name (new or existing one) (Don't specify extension) :")
    fileName = nameOfFile + '.'+extension
    return fileName

print("\n\n\t****** Perform operations on files *******")
# Loop for repetation of opertion on files using different function.
while True:

    print("\n**Please select an operation :-> ")
    print("=> 1. For reading a file.")
    print("=> 2. For adding content in file.")
    print("=> 3. For overwriting a file. ")
    print("=> 4. For creating a new file. ")
    print("=> 5. For deleting data from a file!!")
    print("=> 6. For exit !!")

    selectMode = int(input("||->Enter your choice (1/2/3/4/5/6) :"))

    if selectMode == 1:        
        readFile(nameFile())
    elif selectMode == 2:
        appnedFile(nameFile())
    elif selectMode == 3 or selectMode == 4:
        writeFile(nameFile())
    elif selectMode == 5:
        removeDataOfFile(nameFile())
    elif selectMode == 6:
        print("\n**-> Hope you performed all operations on your file. Bye Bye!\n")
        break
    else:
        print("!! Oops! Please make correct choice.........\n\n")


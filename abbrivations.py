"""This program takes abbrivations as input from user (Make sure abbrivation only contain letters) and
 Give the meaning of that abbrivation in output"""
control = None #Intialize a variable to create a break point for While Loop.
while control!="e":
    userInput = input("Enter the name: ") #Take abbrivation as input.
    n = len(userInput) # Store abbrivation length .
    try:
        with open("abbrivation.txt","r") as file:   #Open abbrivation.txt text file in read mode.
            for line in file.readlines():   # Read every line of file.
                if userInput.upper() == line[:n]: # Compare the abbrivations from text file data.
                    print(line) #Print the meaning of Abbrivation 
    except:
        print("Number and symbols( . , @ / ) is not valid")
    else:
        print("Hope you get right one!")
    control = input("For continue directly press 'Enter Key' OR Want To Exit please enter 'e' : ").lower()
# This program extract character and numbers from a string and store characters and addition of all numbers
userChoice =input("Want to enter a string(Yes/NO):").capitalize()
if userChoice == 'Yes':
    userString = input("Enter a string with formed of mixed numbers and characters (ex:-dwq234jj43jl): ")
else:
    userString = 'ABC123DEF456'
def answer(string):
    alphabets = ""
    result = 0
    for char in string:
        if char.isdigit():
            result+=int(char)
        else:
            alphabets+=char
    return(alphabets,result)
print(answer(userString))
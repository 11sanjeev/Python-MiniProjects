# Import random library to generate random numbers
import random
highestRange = input("||=> Please enter highest range of number in which you want to choose number :")
# Check user input is valid number or not If valid then convert that number into integer datatype from string datatype
if highestRange.isdigit():
    highestRange = int(highestRange)
else:
    print("||=> Please enter a positive number !")
    quit()
#generate a random number in given range and store that in varible randNum
randNum = random.randint(0,highestRange)
print("******* You have 10 chances to complete this game . Have great play time. *******")
# Initialize to variable for counting user guess and user score
guesses = 0
score = 20
while True:
    guesses+=1
    userGuess = input("||=> Make a choice between 0 to {0:d} :".format(highestRange))
    if userGuess.isdigit():
        userGuess = int(userGuess)
        if userGuess > highestRange:
            score = 0
            print("||=> Please choose number in your given range!")
            break
        elif userGuess == randNum:
            print("||=> Yooo ! you choose the correct number .**>>")
            break
        elif userGuess > randNum:
            print("||=> You are above the number! Please enter lower number.")
        else :
            print("||=> You are below the number! Please enter higher number.")
        score -=2
        if score == 0:
            break
    else:
        score = 0
        print("||=> Please enter a valid choice !")
        break

if score == 0:
    print("!!=> Oops! you are out of the game!")
    print("!!=> You choose invalid number Or you completed your chances !")
    print("!!=> And your score is %d "%score)
    print("!!=> Make better choice next time.")
else:
    print("||=> You guess right number in {0:d}".format(guesses)+" guesses")
    print("||=> Your score is %d "%score)
    print("||=> ****Well played.****")
#1. To draw shape untile you give length 0 
import turtle
# Creat variable for storing values 
length = 1
turnAngle = 0
print("Please enter length 0 if want to exit.\nHave a great line drawing ")
# Loop started for line drawing 
while length != 0:
    # take input how much length of line you want
    length = float(input("Enter line length :"))
    if length == 0:
        break
    # Take input of what color of line you want
    color = input("Enter the colour of line :").lower()
    # Take input as how many sides drawing contain
    side = int (input("How many sides you want (In integer numbers) :"))
    # select closed shape or opened shape
    shapeType = input("want a closed shape (yes/no):").lower()
    if shapeType == "yes":
        turnAngle = 360/side
    else:
        turnAngle = float(input("Give angle on which you want turn your line :"))

    turnSide = input("In which side you want to turn your line (right/left):").lower()
    # Declare variable to checking condition for entering in loop 
    counter = 0
    while counter < side:
        turtle.color(color) # Apply color on line
        turtle.forward(length) # Deaw a line forward
        if turnSide == "right":
            turtle.right(turnAngle) # Turn line on given angle
        elif turnSide == "left":
            turtle.left(turnAngle) # Turn line on given angle
            
        # Increase counter by one to make loop finite    
        counter+=1



#2. Draw shape inside a shape 
# import turtle
# side = int(input("Enter side of object:"))
# for steps in range(side):
#     turtle.forward(100)
#     turtle.right(360/side)
#     for steps in range (side):
#         turtle.forward(50)
#         turtle.right(360/side)
# turtle.Screen().exitonclick()
#Import sys library for listing error type if error occured.
import sys
#Function that calculate LCM of given input and print that.
def lcmValue(value1,value2):
    if value1 > value2:
        for multiplier in range (1,value1):
            lcm =  value1*multiplier
            if lcm % value2 == 0:
                print("\n=>* LCM is %d*"%lcm)
                break
    elif value1 < value2:
        for multiplier in range (1,value2):
            lcm =  value2*multiplier
            if lcm % value1 == 0:
                print("\n=>* LCM is %d*"%lcm)
                break
    else:
        print("\n=>*LCM is %d*"%value1)
#Function for calculating HCF of given input and print the HCF.
def hcfValue(value1,value2):
    hcf = 1
    if value1 > value2:
        for divisible in range(2,value1+1):
            if(value1%divisible==0 and value2%divisible==0):
                hcf = divisible
    elif value1 < value2:
        for divisible in range(2,value2+1):
            if(value1%divisible==0 and value2%divisible==0):
                hcf = divisible
    print("\n=>* HCF is %d*"%hcf)
#Take user input for performing desired operation and call function according to user choice.
while True:
    num1 = int(input("\nEnter first digit :"))
    num2 = int(input("Enter second digit :"))
    print("\n****-> Select your option *****")
    print("=> 1. To calculate LCM ")
    print("=> 2. To calculate HCF ")
    print("=> 3. To exit")
    try:
        userChoice = int(input("**=> Choose one (1/2/3) :"))
        if userChoice == 1:
            lcmValue(num1,num2)
        elif userChoice == 2:
            hcfValue(num1,num2)
        elif userChoice == 3:
            print("\nHope you get your desired answer. Bye Bye!\n")
            break
        else:
            print("!!!! Make choice from given options......\n")
    except:
        print("\n!! Oops! Error Occured! and error is: "+ str(sys.exc_info()[0]))
        print("Enter valid input!!\n")
"""Can use string like - repeat repeat this string string with with multiple multiple word word repetition repetition precisely precisely"""
import sys
# Python Program to Count words in a String using Dictionary
def freq(string):
    #A list variable is declared and initialized to an empty list.
    words = []
    #Break the string into list of words
    words = string.split() # or string.lower().split()
    #Declare a dictionary
    Dict = {}
    #Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key) 
    #Print the dictionary
    print("Found *** -> The repeation of words is:",Dict)
def letterCount(string,word):
    words_list = []
    words_list = string.split()
    Dict_string = {}
    for key in words_list:
        #Compare with user specified word and string in words_list 
        if key == word:
            Dict_string[key] = words_list.count(key)
    print("Found *** -> Total repeatation of",word,"is =",Dict_string)

    
#Take string from user . Call function and pass string in it
user_Input = input("=> Enter a string in which you want to count words:")
user_choice = input("=> Want to count for complete String (Enter-'c') or for a specific word (Enter-'w') :").lower()
if user_choice == 'c':
    freq(user_Input)
elif user_choice == 'w':
    specific_word = input("Enter the word for which you want to count :")
    letterCount(user_Input,specific_word)
else:
    print("***!!! Choose wrong option!")
    
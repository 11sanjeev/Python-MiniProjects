# Creating file name variable for storing file name
fileName = 'Null.txt'
# For choosing new one or existing one and extension type 
typeOfFile = input("Want to create a new file or want to add values in existing file \
 please select (new/add)").lower()
chooseExtension = input("Want to choose file extension (yes/no) :").lower()
if chooseExtension == "yes":
    fileExtension = input("Enter file extension (ex:-txt/csv/xml) :")
else:
    fileExtension = 'txt'
#Loop create a new txt file if want to create a new one and choose file opening mode as write or append
if typeOfFile == 'new':
    Name = input("Enter new file name in which want to store name (Don't specify any extension) :")
    fileName = Name+'.'+str(fileExtension)
    openMode = 'w'
else :
    Name = input("Enter existing file name in which you want to store name (Don't specify any extension) :")
    fileName = Name+str(fileExtension)
    openMode = 'a'
# Open file in write mode if new one or in append mode if existing one
file = open(fileName,openMode)
guest = []
# Taking guest name input as list
print("Please make it comma(,) separated If want to give multiple values with one name.")
print("Please enter 'Done' for exiting input mode When you done with all name or values.")
while True:
    name = input("Person name please:").capitalize()
    if name == 'Done':
        break
    guest.append(name)
#Sorting guest name 
guest.sort()
# Add guest name one by onein file
for guests in guest:
    file.write(guests + "\n")
# file closed
file.close()
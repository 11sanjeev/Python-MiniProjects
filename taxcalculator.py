tax = 0
country = input("From which country you are :").lower()
orderAmmount = float(input("Enter your order total amount :"))
if country == 'canada':
    province = input ("Enter from which province :")
    if province == "alberta":
        tax = orderAmmount*0.05/100
        orderAmmount = orderAmmount+tax
        print("You have to pay${0:f}".format(orderAmmount))
    elif province =="ontario"or province == "new brunswick" or province=='nova soctia':
        tax = orderAmmount*13/100
        orderAmmount = orderAmmount+tax
        print("You have to pay${0:f}".format(orderAmmount))
    else:
        tax = orderAmmount*0.11/100
        orderAmmount = orderAmmount+tax
        print("You have to pay${0:f}".format(orderAmmount))
else : 
    print("Your total ammount is ${0:f}".format(orderAmmount))
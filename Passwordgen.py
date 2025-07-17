import random 
import string

# Make function Input to take Input from user and return some value
def Input():
    length = int(input("Enter length of your desired password :"))
    letter = string.ascii_letters
    digit = string.digits
    symbol = string.punctuation
    SumOfAll = letter + digit + symbol
    return length,SumOfAll

# Make a function called passwordgenerator to create password
def passwordgenerator():
    length,SumOfAll = Input()
    list = []
    for i in SumOfAll:
        list.append(i)
    password=""
    for i in range(length):
        password=password+random.choice(SumOfAll)
    print(password)
    user_Input = input("Do you want to create more password(Select yes and no): ")
    if(user_Input.lower() == "yes"):
        passwordgenerator()
    else:
        print("Thank you")

passwordgenerator()
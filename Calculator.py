# Make a function named calc which is used to solve some mathematical operation.
def calc(opt,num1,num2):
    if(opt  == "+"):
        return num1+num2
    elif(opt == "-"):
        return num1-num2
    elif(opt == "*"):
        return num1*num2
    elif(opt == "/"):
        return num1/num2
    elif(opt == "%"):
        return num1%num2
    else:
        return -1
    
def  Input():
    # Take input two number from the user.
    num1 = int(input("Enter the 1st no.: "))
    num2 = int(input("Enter the 2nd no.: "))

    # Take input operator from the user.
    print("You can use these operators:\n+ = (to add)\n- = (to subtract)\n* = (to multiply)\n/ = (to divide)\n% = (to find reminder)")
    operator = input("Enter the operator: ")

    # Here we call the function calc and try to get the answer.
    result = calc(operator,num1,num2)
    if(result == -1):
        print("You entered wrong operator.")
    else:
        print("Answer of",num1,operator,num2,"is:",result)
    
    #Take user input to use calculator or not.
    #If yes,then used recurrsion to call calc and other thing
    user_input = input("Do you want a calculator for more calculations(Select yes and no): ")
    if(user_input.lower() == "yes"):
        Input()
    else:
        print("Thank you")

Input()
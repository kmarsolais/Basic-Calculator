finishedExecuting = False
num1Valid = False
num2Valid = False
userChoiceValid = False
counterOperand = 0
chances = 3
enoughChances = True
operandChosen = False
print("Hi, Welcome To Kevin's Magical Calculator")
while not finishedExecuting:

    if counterOperand > 0:
        while enoughChances:
            print("That is not a valid operand, please enter 'x', '+', '-' or '/' You have "+str(chances)+" chance(s) "
                                                                                                          "left.")
            operand = input("What operation would you like to perform? (x,+,-,/)")
            if operand in ('x', '+', '-', '/'):
                operandChosen=True
                break
            chances = chances-1
            if chances == 0:
                print("Sorry, you have exhausted all your chances, please run the program again if you wish to "
                      "perform other calculations, the program will now terminate.")
                exit(0)
    userChoiceValid = False
    if not operandChosen:
        operand = input("What operation would you like to perform? (x,+,-,/)")
    if operand not in ('x', '+', '-', '/'):
        counterOperand = counterOperand + 1
        continue
    else:
        finishedExecuting = True

    while not num1Valid:
        try:
            num1 = input("Please enter a valid number")
            check_num1 = isinstance(int(num1), int)
            num1Valid = check_num1
        except ValueError:
            print("That is not a valid number, please try again")

    while not num2Valid:
        try:
            num2 = input("Please enter a valid number")
            check_num2 = isinstance(int(num2), int)
            num2Valid = check_num2
        except ValueError:
            print("That is not a valid number, please try again")

    if operand == "x":
        print(float(num1) * float(num2))
    elif operand == "+":
        print(float(num1) + float(num2))
    elif operand == "-":
        print(float(num1) - float(num2))
    elif operand == "/":
        print(float(num1) / float(num2))

    while not userChoiceValid:

        userChoice = input("Would you like to perform another calculation? (y/n)")
        if userChoice not in ('y','n'):
            input("Please enter 'y' or 'n'")
        if userChoice == 'y':
            finishedExecuting = False
            num1Valid = False
            num2Valid = False
            userChoiceValid = True
            counterOperand = 0
            chances = 3
            enoughChances = True
            operandChosen = False
        if userChoice == 'n':
            print("Thank you for using Kevin's magical calculator")
            exit(0)








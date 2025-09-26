from art import logo
print(logo)

#addition
def addition(n1, n2):
    return n1 + n2

add = addition

#subtraction
def subtraction(n1, n2):
    return n1 - n2

subtract = subtraction

#multiplication
def multiplication(n1, n2):
    return n1 * n2

multiply = multiplication

def division(n1, n2):
    return n1 / n2

divide = division

calculator_operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

#set state
first_run = True
continue_working = True

while continue_working:
    if first_run:
        n1 = float(input("Type the first number: \n "))
        first_run = False
        #Operator
        for symbol in calculator_operation:
          print(symbol)

        operator = input("Pick an operator to perform: \n ")

    while operator not in calculator_operation:
        print('Invalid operation, choose "+", "-", "*" or "/" ')
        operator = input("Type the mathematical operator: \n ")

    n2 = float(input("Type the second number: \n "))
    # Apply operation
    result = calculator_operation[operator](n1, n2)
    print(f" {n1} {operator} {n2} = {result}")

    # Ask if user wants to continue working with previous result
    previous_result = input(f"Want to continue next operation using the previous result {result}? "
                            "Type 'y' or 'n : \n").lower()

    if previous_result == "y":
        n1 = result #update n1 for next calculation
        operator = input("Type the mathematical operator: \n ")
    else: #previous_result == "no":
        another_operation = input("what to perform another operation. Type 'y' to start or 'n' to stop \n").lower()
        if another_operation == "y":
            first_run = True
            #continue
        else:
            continue_working = False



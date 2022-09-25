#Calculator


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1):
    # n2 = n1
    return n1*n1


operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": power}


def calculator():

    n1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol == "**":
          calculation_function = operations[operation_symbol]
          answer = calculation_function(n1)
          print(f"{n1} {operation_symbol} {n1} = {answer}")
        else:  
          n2 = int(input("Whats the next number?: "))
          calculation_function = operations[operation_symbol]
          answer = calculation_function(n1, n2)
          print(f"{n1} {operation_symbol} {n2} = {answer}")
  
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ) == "Y" or "y" or "Yes" or "yes":
            n1 = answer
        else:
            should_continue = False
            calculator()


calculator()

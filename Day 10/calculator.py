#Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

operations = {
  "+": add, #symbol: Key
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": power
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
if operations[operation_symbol] != power: 
    num2 = int(input("What's the second number?: ")) 
else:
    calculation_function = operations[operation_symbol]
    num2 = num1
  

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
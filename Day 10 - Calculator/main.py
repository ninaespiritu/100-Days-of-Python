from art import logo
print(logo)

# Functions for Operations
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# Dictonary for Operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# Calculator Function
def calculator():
  num1 = float(input("Enter the first number: "))
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Choose an operation (+ - * /): ")
    num2 = float(input("Enter next number: "))
    function = operations[operation_symbol]
    answer = function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    should_continue_input = input(f'\nType "y" to continue calculating with {answer}, or type "n" to start a new calculation: ')
    
    if should_continue_input == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
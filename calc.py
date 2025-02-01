def add(num1, num2):
  """Adds two numbers together and returns the result."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts one number from another and returns the result."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers together and returns the result."""
  return num1 * num2

def divide(num1, num2):
  """Divides one number by another and returns the result. Handles division by zero error."""
  if num2 == 0:
    return "Error: Cannot divide by zero"
  else:
    return num1 / num2

while True:
  # Get user input for operation
  print("Enter operation (+, -, *, /): ")
  operator = input()

  # Get user input for numbers
  print("Enter first number: ")
  num1 = float(input())
  print("Enter second number: ")
  num2 = float(input())

  # Perform calculation based on operator
  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator")
    continue

  # Print the result
  print(f"{num1} {operator} {num2} = {result}")

  # Ask user if they want to continue
  print("Do you want to continue? (y/n): ")
  choice = input()
  if choice != 'y':
    break

print("Thank you for using the calculator!")

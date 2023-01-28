from configparser import SectionProxy


first=input("Enter the first number:")
operator=input("Enter operator(+,-,*,/,%)")
second=input("Enter the second number:\n")

first=int(first)
second=int(second)

if operator == "+":
    print("Addition of two numbers:",first + second)
    
elif operator == "-":
    print("Subtraction of two numbers:",first - second)
    
elif operator == "*":
    print("Multiplication of two numbers:",first * second)
    
elif operator == "/":
    print("Division of two numbers:",first / second)
    
elif operator == "%":
    print("Reminder of two numbers:",first % second)
    
else:
    print("Invalid operator")
    

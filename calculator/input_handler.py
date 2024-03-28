from decimal import Decimal

def get_user_input():
    a = Decimal(input("Enter the first number: "))
    b = Decimal(input("Enter the second number: "))
    return a, b
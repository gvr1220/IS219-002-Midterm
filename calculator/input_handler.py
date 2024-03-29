import logging
from decimal import Decimal, InvalidOperation

logging.basicConfig(level=logging.INFO)
loggers = logging.getLogger("root")

def get_user_input():
    while True:
        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
            return a, b
        except InvalidOperation:
            print("Invalid input! Please enter a valid number.")
            loggers.warning("Invalid input detected")
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice != 'yes':
                return None, None  # Returning None values to indicate the user wants to return to the main page

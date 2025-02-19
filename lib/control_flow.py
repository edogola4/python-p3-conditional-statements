#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    """
    Returns "Access granted" if the username is "admin" or "ADMIN"
    and the password is "12345". Otherwise, returns "Access denined".
    """
    if ( username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
    """
    Returns a weather message based on the given temperatures.
    - Below 40: "It's brisk out there!"
    - Between 40 and 65 (inclusive): "It's a little chilly out there!"
    - Above 85: "It's too dang hot out there!"
    - Otherwise: "It's perfect out there!"

    """
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass

def fizzbuzz(num):
    # your code here
    """
    For multiple of 3, return "Fizz"
    For multiple of 5, return "Buzz"
    For multiple of both 3 and 5, return "FizzBuzz"
    Otherwise, returns the number itself
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else: 
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    """
    Takes an operator (one of "+", "-", "*", or "/") and two numbers.
    Returns the result of applying the operation to the numbers
    If the operation not valid, prints "Invalid operation!" and returns None
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else: 
        print("Invalid operation!")
        return None
    pass

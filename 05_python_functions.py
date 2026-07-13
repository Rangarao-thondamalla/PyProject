# ============================================================
# 5. Python Functions
# ============================================================

# -------------------------------
# 5.1 Python Functions (Concept)
# -------------------------------
# A function is a block of reusable code that performs a specific task.
# Why use functions?
# 1. Avoid code repetition.
# 2. Break large programs into smaller, manageable pieces.
# 3. Make code reusable and readable.
# 4. Can return results or perform actions.

# Syntax:
# def function_name(parameters):
#     """docstring (optional)"""
#     body of the function
#     return value (optional)
# function definitions must be executed before they can be called.
# after function definition, you can call the function by using its name followed by parentheses.
# without callinga function, it will not execute.

# Example 1: Simple Function
# def greet():
#     print("Hello, welcome to Python Functions!")
#   # Output: Hello, welcome to Python Functions!
# greet()

# Example 2: Function with Parameters
# def add(a, b):
#     return a + b
# print(add(5, 3))  # Output: 8
# print(add(10, 10)) # Output: 20
# print(add(1, 2)) # Output: 3

# def eligible_to_vote(salary, age, name):
#     print("This is name: ", name)
#     print("This is salary: ", salary)
#     print("This is age: ", age)
#     if age>=18:
#         print("You are eligible to vote.")
#     elif age<18 and age>0:
#         print("You are not eligible to vote.")  
#     else:
#         print("Invalid age entered.")                      

# # age = int(input("Enter your age: "))
# age = 15
# f_name = "John"
# salary = 120000
# eligible_to_vote(salary, age, f_name)

# Example 3: Function with Default Parameters
# def introduce(name="User"):
#     print("Hello,", name)
# introduce()              # Output: Hello, User
# introduce("Alice")       # Output: Hello, Alice

# Example 4: Function Returning Multiple Values
# def math_operations(a, b):
#     return a+b, a-b, a*b, a/b
# print(math_operations(10, 2))  # Output: (12, 8, 20, 5.0)

# Example 5: Docstring Example

# write a function that calculate the square and take input from user and return the square of the number.
# def calculate_square(num):
#     """This function takes a number as input and returns its square."""
#     return num ** 2

# print(calculate_square(5))  # Output: 25

# # instead of hardcoding the value, we can take input from user and return the square of the number.
# def calculate_square_from_input():
#     """This function takes a number as input from the user and returns its square."""
#     num = float(input("Enter a number: "))
#     return num ** 2

# print(calculate_square_from_input())  # Output: (depends on user input)


# -----------------------------------
# 5.2 Python Built-in Functions
# -----------------------------------
# Python provides many built-in functions to perform common tasks.
# These are pre-defined and can be used directly.
# Categories: Numeric, Type conversion, Iteration, String, etc.

# Example 1: Numeric Functions
# print(abs(-10))   # Output: 10
# print(pow(2, 3))  # Output: 8
# print(round(3.141, 2))
# print(min(10, 20, 30))
# print(sum(1, 2))

# Example 2: Type Conversion Functions
# print(int(3.7))    # Output: 3
# print(float("5"))  # Output: 5.0

# Example 3: Iteration Functions
# numbers = [1, 2, 3, 4, 1]
# print(len(numbers))       # Output: 4
# print(sum(numbers))       # Output: 10
# print(max(numbers))       # Output: 4
# print(min(numbers))       # Output: 1

# Example 4: String Functions
# print(chr(65))  # Output: 'A'
# print(ord("A")) # Output: 65

# Example 5: Miscellaneous Functions
# print(type(5))        # Output: <class 'int'>
# print(type("abc"))
# print(type(3.14))
# print(isinstance(5, int))  # Output: True
# value = 10
# print(id(value))
# help(sum)



# -----------------------------------
# 5.3 Python Lambda Functions
# -----------------------------------
# A lambda function is a small anonymous function defined with 'lambda' keyword.
# Syntax: lambda arguments: expression
# Key points:
# 1. Can have multiple arguments but only one expression.
# 2. Expression is automatically returned.
# 3. Useful for short, simple functions.

# Example 1: Simple Lambda
# square = lambda x, y: x * y
# sum = lambda x, y: x + y
# print(type(square))
# print(square(5, 10))  
# print(sum(5, 10)) 

# numbers = [1,2,3,4,5,6]
# print(numbers)
# event_numbers = list(filter(lambda n: n % 2 == 0, numbers))
# print(event_numbers)

# def is_even(n):
#     return n % 2 == 0

# numbers = [1,2,3,4,5,6]
# event_numbers = list(filter(is_even, numbers))
# print(event_numbers)

# squares = list(map(lambda x: x+x, nums))
# print(squares)  # Output: [1, 4, 9, 16, 25, 36]


# Example 2: Lambda with Two Arguments
# add = lambda a, b: a + b
# print(add(10, 20))  # Output: 30

# Example 3: Using Lambda in Sorting
# data = [(1, "apple"), (3, "banana"), (2, "cherry")]
# print(type(data))
# data.sort(key=lambda x: x[0])
# print(data)  # Output: [(1, 'apple'), (2, 'cherry'), (3, 'banana')]

# Example 4: Lambda with filter()
# nums = [1, 2, 3, 4, 5, 6, 0]
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)  # Output: [2, 4, 6]

# # Example 5: Lambda with map()
# squares = list(map(lambda x: x+x, nums))
# print(squares)  # Output: [1, 4, 9, 16, 25, 36]



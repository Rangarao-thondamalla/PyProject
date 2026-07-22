# ================================================================================
# 7. Python OOPs
# ================================================================================

# OOP is a programming paradigm based on the concept of "objects"
# Objects contain data (attributes) and code (methods)
# Four main pillars of OOP: Encapsulation, Inheritance, Polymorphism, Abstraction

# KEY BENEFITS OF OOP:
# 1. Modularity: Code organized into logical units
# 2. Reusability: Classes can be reused across programs
# 3. Maintainability: Easy to modify and extend
# 4. Scalability: Easy to manage complex systems
# 5. Data Hiding: Protect internal implementation

# --------------------------------------------------------------------------------
# Python OOPs Concepts
# --------------------------------------------------------------------------------

# CORE OOP CONCEPTS IN PYTHON:

# 1. CLASS: Blueprint/template for creating objects
#    - Defines attributes and methods common to all objects of that type
#    - Serves as a factory for creating instances

# 2. OBJECT: Instance of a class with actual data
#    - Has state (attributes), behavior (methods), and identity
#    - Represents real-world entities in code

# 3. ATTRIBUTE: Variable bound to an object or class
#    - Instance variables: Unique to each object
#    - Class variables: Shared across all instances

# 4. METHOD: Function defined within a class
#    - Operates on object data
#    - Can access and modify object state

# 5. CONSTRUCTOR: Special method __init__() for object initialization
#    - Called automatically when object is created
#    - Sets initial state of the object

# 6. SE
# LF: Reference to current instance of the class
#    - First parameter of instance methods
#    - Used to access variables and methods


# ................................................................................
# Example: Basic Class and Object Creation - Car Manufacturing
# ................................................................................

# class userAccount:
#     def __init__(self, name, account_no, address):
#         self.name = name
#         self.account_no = account_no
#         self.address = address

#     def displayUser(self):
#         return f"Name is: {self.name}, account number is: {self.account_no}, address is: {self.address}"

# john = userAccount("John", 1200988112233, "XYZ")
# print(john.displayUser())
# pradeep = userAccount("Pradeep", 12345, "ABC")
# print(pradeep.displayUser())


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         return f"{self.brand} {self.model}"

# my_car = Car("Toyota", "Corolla")
# print(my_car.display_info())

# Expected Output:
# Toyota Corolla

# --------------------------------------------------------------------------------
# Python Classes and Objects
# --------------------------------------------------------------------------------

# CLASSES AND OBJECTS DETAILED EXPLANATION:

# CLASS COMPONENTS:
# 1. Class Name: Identifier following naming conventions
# 2. Class Variables: Variables shared by all instances
# 3. Instance Variables: Variables unique to each instance
# 4. Methods: Functions defining object behavior
# 5. Constructor: __init__ method for initialization

# OBJECT CHARACTERISTICS:
# 1. Identity: Unique object identifier (memory address)
# 2. State: Represented by object's attributes
# 3. Behavior: Defined by object's methods

# INSTANCE VS CLASS VARIABLES:
# - Instance variables: Different for each object
# - Class variables: Same for all objects of the class
# - Class variables are defined outside any method
# - Instance variables are defined inside __init__ or methods

# ................................................................................
# Example: Student Class with Multiple Objects - University Management
# ................................................................................
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
    
#     def get_details(self):
#         return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# student1 = Student("Alice", 20, "A")
# student2 = Student("Bob", 22, "B")
# student3 = Student("Charlie", 19, "A+")

# print(student1.get_details())
# print(student2.get_details())
# print(student3.get_details())

# Expected Output:
# Name: Alice, Age: 20, Grade: A
# Name: Bob, Age: 22, Grade: B
# Name: Charlie, Age: 19, Grade: A+


# ................................................................................
# Example: Class with Instance and Class Variables - Corporate System
# ................................................................................
# class Employee:
#     company = "Tech Corp"  # Class variable - shared across all instances
    
#     def __init__(self, name, salary):
#         self.name = name      # Instance variable - unique to each object
#         self.salary = salary   # Instance variable - unique to each object
    
#     def display_info(self):
#         return f"{self.name} works at {Employee.company} and earns ${self.salary}"
 
# emp1 = Employee("John", 50000)
# emp2 = Employee("Sarah", 60000)

# print(emp1.display_info())
# print(emp2.display_info())
# print(f"Company: {Employee.company}")

# Expected Output:
# John works at Tech Corp and earns $50000
# Sarah works at Tech Corp and earns $60000
# Company: Tech Corp

# ................................................................................
# Example: Class with Multiple Methods - Calculator Application
# ................................................................................

# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def add(self, a, b):
#         self.result = a + b
#         return self.result
    
#     def multiply(self, a, b):
#         self.result = a * b
#         return self.result
    
#     def get_previous_result(self):
#         return self.result

# calc = Calculator()
# print(calc.multiply(4, 7))

# print(calc.add(5, 3))
# print(calc.add(1, 2))
# print(calc.add(4, 2))
# print(f"Previous result: {calc.get_previous_result()}")

# Expected Output:
# 8
# 28
# Previous result: 28

# ................................................................................
# Example: Method Chaining in Classes - String Builder Pattern
# ................................................................................
# class StringBuilder:
#     def __init__(self):
#         self.string = ""
#     # string = ""
#     def add_text(self, text):
#         self.string += text
#         return self  # Return self to enable chaining
#     # string = "Hello"
#     def add_space(self):
#         self.string += " "
#         return self  # Return self to enable chaining
#     # string = "Hello "
#     # string = "Hello World"
#     def build(self):
#         return self.string

# builder = StringBuilder()
# result = builder.add_text("Hello").add_space().add_text("World").build()
# print(result)

# Expected Output:
# Hello World

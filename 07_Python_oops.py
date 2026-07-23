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

# --------------------------------------------------------------------------------
# Python Constructors
# --------------------------------------------------------------------------------

# CONSTRUCTORS COMPREHENSIVE THEORY:

# WHAT IS A CONSTRUCTOR?
# - Special method named __init__
# - Automatically called when object is created
# - Used to initialize object's state
# - Can take parameters for object initialization

# TYPES OF CONSTRUCTORS:
# 1. Default Constructor: No parameters, sets default values
# 2. Parameterized Constructor: Takes parameters for initialization
# 3. Constructor with Default Values: Parameters with default values

# CONSTRUCTOR CHARACTERISTICS:
# - Always named __init__
# - First parameter is always 'self'
# - Can call other methods from constructor
# - Can perform validation during object creation
# - Doesn't return any value explicitly


# ................................................................................
# Example: Default Constructor - Basic Object Initialization
# ................................................................................
# class DefaultDemo:
#     def __init__(self):
#         self.value = 100
#         self.message = "Default object created"
    
#     def display(self):
#         return f"Value: {self.value}, Message: {self.message}"

# obj = DefaultDemo()
# print(obj.display())

# Expected Output:
# Value: 100, Message: Default object created

# ................................................................................
# Example: Parameterized Constructor - Person Profile System
# ................................................................................
# class Person:
#     def __init__(self, name, age=15, city="unknown"):
#         self.name = name
#         self.age = age
#         self.city = city
    
#     def introduce(self):
#         return f"I'm {self.name}, {self.age} years old from {self.city}"

# person1 = Person("Mike", 25, "New York")
# person2 = Person("Emma", 30, "London")
# person3 = Person("John")

# print(person1.introduce())
# print(person2.introduce())
# print(person3.introduce())

# Expected Output:
# I'm Mike, 25 years old from New York
# I'm Emma, 30 years old from London

# ................................................................................
# Example: Constructor with Default Parameters - Library Management
# ................................................................................
# class Book:
#     def __init__(self, title, author="Unknown", pages=0):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def get_info(self):
#         return f"'{self.title}' by {self.author}, {self.pages} pages"

# book1 = Book("Python Programming")
# book2 = Book("Data Science", "Jane Smith")
# book3 = Book("Algorithms", "Robert Brown", 350)

# print(book1.get_info())
# print(book2.get_info())
# print(book3.get_info())

# Expected Output:
# 'Python Programming' by Unknown, 0 pages
# 'Data Science' by Jane Smith, 0 pages
# 'Algorithms' by Robert Brown, 350 pages

# ................................................................................
# Example: Constructor Calling Other Methods - Bank Account Setup
# ................................................................................
# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.holder = account_holder
#         self.balance = initial_balance
#         self.account_number = self.generate_account_number()
#         self.display_welcome_message()
    
#     def generate_account_number(self):
#         import random
#         return f"ACC{random.randint(1000, 9999)}" 
    
#     def display_welcome_message(self):
#         print(f"Welcome {self.holder}! Account {self.account_number} created with balance: ${self.balance}")

# account1 = BankAccount("Tom")
# account2 = BankAccount("Jerry", 1000)

# Expected Output:
# Welcome Tom! Account ACC[random] created with balance: $0
# Welcome Jerry! Account ACC[random] created with balance: $1000


# --------------------------------------------------------------------------------
# Python Inheritance
# --------------------------------------------------------------------------------

# INHERITANCE COMPREHENSIVE THEORY:

# WHAT IS INHERITANCE?
# - Mechanism to create new class from existing class
# - New class (child) inherits attributes and methods from existing class (parent)
# - Promotes code reusability and establishes relationships

# TYPES OF INHERITANCE:
# 1. Single Inheritance: Child class inherits from one parent
# 2. Multiple Inheritance: Child inherits from multiple parents 
# 3. Multilevel Inheritance: Chain of inheritance (A→B→C) 
# 4. Hierarchical Inheritance: Multiple children from single parent
# 5. Hybrid Inheritance: Combination of multiple types

# KEY TERMS:
# - Parent Class (Base/Super class): Class being inherited from
# - Child Class (Derived/Sub class): Class that inherits
# - Method Overriding: Child class provides specific implementation of parent method
# - super(): Function to call parent class methods

# ................................................................................
# Example: Single Inheritance with Method Overriding - Animal Kingdom
# ................................................................................
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return "Animal makes sound"
    
#     def move(self):
#         return f"{self.name} is moving"

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Call parent constructor
#         self.breed = breed
    
#     def speak(self):  # Method overriding - specific implementation
#         return "Woof!"
    
#     def fetch(self):
#         return f"{self.name} is fetching"

# dog = Dog("Buddy", "Golden Retriever")
# print(dog.speak())
# print(dog.move())
# print(dog.fetch())


# Expected Output:
# Woof!
# Buddy is moving
# Buddy is fetching


# ................................................................................
# Example: Multiple Inheritance - Hybrid Creature System
# ................................................................................
# class Swimmer:
#     def swim(self):
#         return "Swimming in water"

#     def print(self):
#         return "Name in swimmer" 

# class Flyer:
#     def fly(self):
#         return "Flying in sky"

#     def print(self):
#         return "Name in Flyer" 

# class Duck(Swimmer, Flyer):
#     def __init__(self, name):
#         self.name = name
    
#     def quack(self):
#         return "Quack quack!"

# duck = Duck("Donald")
# print(duck.print())
# print(duck.quack())
# print(duck.swim())
# print(duck.fly())

# # Expected Output:
# # Quack quack!
# # Swimming in water
# # Flying in sky

# # ................................................................................
# # Example: Multilevel Inheritance - Vehicle Hierarchy
# # ................................................................................
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
    
#     def start_engine(self):
#         return "Engine started"

# class Car(Vehicle):
#     def __init__(self, brand, doors):
#         super().__init__(brand)
#         self.doors = doors
    
#     def open_trunk(self):
#         return "Trunk opened"

# class SportsCar(Car):
#     def __init__(self, brand, doors, top_speed):
#         super().__init__(brand, doors)
#         self.top_speed = top_speed
    
#     def turbo_boost(self):
#         return "Turbo boost activated!"

# sports_car = SportsCar("Ferrari", 2, 300)
# print(sports_car.start_engine())
# print(sports_car.open_trunk())
# print(sports_car.turbo_boost())
# print(f"Brand: {sports_car.brand}, Doors: {sports_car.doors}, Top Speed: {sports_car.top_speed}km/h")

# # Expected Output:
# # Engine started
# # Trunk opened
# # Turbo boost activated!
# # Brand: Ferrari, Doors: 2, Top Speed: 300km/h

# # ................................................................................
# # Example: Hierarchical Inheritance - Shape Geometry System
# # ................................................................................



# class Shape:
#     def __init__(self, color):
#         self.color = color
    
#     def describe(self):
#         return f"This is a {self.color} shape"

# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius
    
#     def area(self):
#         return 3.14159 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, color, length, width):
#         super().__init__(color)
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width

# circle = Circle("red", 5)
# rectangle = Rectangle("blue", 4, 6)

# print(circle.describe())
# print(f"Circle area: {circle.area()}")
# print(rectangle.describe())
# print(f"Rectangle area: {rectangle.area()}")

# Expected Output:
# This is a red shape
# Circle area: 78.53975
# This is a blue shape
# Rectangle area: 24



# --------------------------------------------------------------------------------
# Abstraction in Python
# --------------------------------------------------------------------------------

# ABSTRACTION COMPREHENSIVE THEORY:

# WHAT IS ABSTRACTION?
# - Hiding complex implementation details and showing only essential features
# - Focus on what object does rather than how it does it
# - Achieved using Abstract Base Classes (ABC) and abstract methods

# ABSTRACT BASE CLASS (ABC):
# - Class that cannot be instantiated directly
# - Contains one or more abstract methods
# - Serves as blueprint for other classes

# ABSTRACT METHOD:
# - Method declared but contains no implementation
# - Must be implemented by concrete (non-abstract) subclasses
# - Defined using @abstractmethod decorator

# KEY POINTS:
# - Import ABC from abc module
# - Use @abstractmethod decorator for abstract methods
# - Concrete classes must implement all abstract methods
# - Prevents instantiation of incomplete classes


# from abc import ABC, abstractmethod
# from abc import ABC, abstractmethod
# class Phone(ABC):

#     def __init__(self, model_name):
#         self.model_name = model_name

#     @abstractmethod
#     def make_call(self, number):
#         pass

#     @abstractmethod
#     def send_message(self, number, message):
#         pass

#     @abstractmethod
#     def connect_internet(self):
#         pass

#     def phone_info(self):
#         print(f"Phone Model: {self.model_name}")

# class ApplePhone(Phone):

#     def make_call(self, number):
#         print(f"Dialing {number} using Apple iPhone's calling system....")    

#     def send_message(self, number, message):
#         print(f"Sending message to {number} using Apple iPhone's messaging system....: {message}")

#     def connect_internet(self):
#         print(f"Connecting to internet....")

# class SamsungPhone(Phone):

#     def make_call(self, number):
#         print(f"Dialing {number} using Samsung's calling system with network 5G....")    

#     def send_message(self, number, message):
#         print(f"Sending message to {number} using Samsung's messaging system....: {message}")

#     def connect_internet(self):
#         print(f"Connecting to internet using 5G gateway....")

# apple = ApplePhone("Iphone 17E")
# apple.phone_info()
# apple.make_call("+91-91726655441122")
# apple.send_message("+91-91726655441122", "Hello I am John!")
# apple.connect_internet()
# print("---------------------------------------------------------------")
# samsung = SamsungPhone("Samsung 351")
# samsung.phone_info()
# samsung.make_call("+91-9155667788")
# samsung.send_message("+91-9155667788", "Hello I am John, from USA!")
# samsung.connect_internet()

# ................................................................................
# Example: Abstract Base Class with Multiple Implementations - Payment System
# ................................................................................
# from abc import ABC, abstractmethod

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass
    
#     @abstractmethod
#     def refund_payment(self, amount):
#         pass
    
#     def get_processor_info(self):  # Concrete method
#         return "This is a payment processor"

# class CreditCardProcessor(PaymentProcessor):
#     def process_payment(self, amount):
#         return f"Processing credit card payment of ${amount}"
    
#     def refund_payment(self, amount):
#         return f"Refunding ${amount} to credit card"

# class PayPalProcessor(PaymentProcessor):
#     def process_payment(self, amount):
#         return f"Processing PayPal payment of ${amount}"
    
#     def refund_payment(self, amount):
#         return f"Refunding ${amount} via PayPal"

# credit_card = CreditCardProcessor()
# paypal = PayPalProcessor()

# print(credit_card.process_payment(100))
# print(credit_card.refund_payment(50))
# print(credit_card.get_processor_info())
# print(paypal.process_payment(200))
# print(paypal.get_processor_info())

# Expected Output:
# Processing credit card payment of $100
# Refunding $50 to credit card
# Processing PayPal payment of $200
# This is a payment processor

# ................................................................................
# Example: Abstract Class with Concrete and Abstract Methods - Database Interface
# ................................................................................
# from abc import ABC, abstractmethod

# class Database(ABC):
#     def __init__(self, database_name):
#         self.database_name = database_name
    
#     @abstractmethod
#     def connect(self):
#         pass
    
#     @abstractmethod
#     def disconnect(self):
#         pass
    
#     def backup_database(self):  # Concrete method with implementation
#         return f"Backing up {self.database_name}"

# class MySQLDatabase(Database):
#     def connect(self):
#         return f"Connected to MySQL database: {self.database_name}"
    
#     def disconnect(self):
#         return f"Disconnected from MySQL database: {self.database_name}"

# class PostgreSQL(Database):
#     def connect(self):
#         return f"Connected to PostgreSQL database using method PSQL: {self.database_name}"
    
#     def disconnect(self):
#         return f"Disconnected from PostgreSQL database: {self.database_name}"        

# mysql_db = MySQLDatabase("Employee_Data")
# print(mysql_db.connect())
# print(mysql_db.backup_database())
# print(mysql_db.disconnect())

# postgresql_db = PostgreSQL("Patient_Data")
# print(postgresql_db.connect())
# print(postgresql_db.backup_database())
# print(postgresql_db.disconnect())

# Expected Output:
# Connected to MySQL database: my_database
# Backing up my_database
# Disconnected from MySQL database: my_database

# ................................................................................
# Example: Abstract Properties - Biological Classification System
# ................................................................................
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @property
#     @abstractmethod
#     def scientific_name(self):
#         pass
    
#     @property
#     @abstractmethod
#     def habitat(self):
#         pass
    
#     def describe(self):
#         return f"{self.scientific_name} lives in {self.habitat}"

# class Lion(Animal):
#     @property
#     def scientific_name(self):
#         return "Panthera leo"
    
#     @property
#     def habitat(self):
#         return "savannah"

# lion = Lion()
# print(lion.describe())
# print(f"Scientific name: {lion.scientific_name}")

# Expected Output:
# Panthera leo lives in savannah
# Scientific name: Panthera leo

# --------------------------------------------------------------------------------
# Access Modifiers in Python
# --------------------------------------------------------------------------------

# ACCESS MODIFIERS COMPREHENSIVE THEORY:
1
# TYPES OF ACCESS MODIFIERS:
# 1. Public: No underscore prefix - accessible from anywhere
# 2. Protected: Single underscore prefix - internal use convention
# 3. Private: Double underscore prefix - name mangling applied

# PUBLIC MEMBERS:
# - Accessible from outside the class
# - No restrictions on access
# - Standard way to expose interface

# PROTECTED MEMBERS:
# - Convention: intended for internal use
# - Accessible within class and subclasses
# - Not enforced by Python interpreter

# PRIVATE MEMBERS:
# - Name mangling: _ClassName__privateMember
# - Not accessible directly from outside
# - Should use public methods to access

# NAME MANGLING:
# - Mechanism to make private members harder to access
# - Changes name to include class name
# - Prevents accidental override in subclasses

# class HospitalManagement:
#     hospital_name = "Appolo"
#     _doctor_name_list = "dr. Sachet Roy"
#     __medicine_name = "Test"

# h1 = HospitalManagement()
# print(f"This is public variable: {h1.hospital_name}")
# print(f"This is protected variable: {h1._doctor_name_list}") 
# When tried to access private variables outside 
# print(f"This is private variable: {h1.__medicine_name}") 

# ................................................................................
# Example: Public, Protected, and Private Members - Access Control Demo
# ................................................................................
# class AccessDemo:
#     def __init__(self):
#         self.public_var = "I am public"           # Public - no restrictions
#         self._protected_var = "I am protected"    # Protected - internal use
#         self.__private_var = "I am private"       # Private - name mangling
    
#     def public_method(self):
#         return "Public method"
    
#     def _protected_method(self):
#         return "Protected method"
    
#     def __private_method(self):
#         return "Private method"
    
#     def access_private_members(self):
#         # Can access private members within class
#         return f"{self.__private_var} - {self.__private_method()}"

# class DerivedClass(AccessDemo):
#     def access_protected(self):
#         # Can access protected members in derived class
#         return f"{self._protected_var} - {self._protected_method()}"

# obj = AccessDemo()
# derived = DerivedClass()

# print(obj.public_var)
# print(obj.public_method())
# print(derived.access_protected())
# print(obj.access_private_members())

# Expected Output:
# I am public
# Public method
# I am protected - Protected method
# I am private - Private method

# ................................................................................
# Example: Name Mangling with Private Members - Security System
# ................................................................................
# class NameManglingDemo:
#     def __init__(self):
#         self.public_value = 10
#         self._protected_value = 20
#         self.__private_value = 30  # Becomes _NameManglingDemo__private_value
    
#     def get_private_value(self):
#         return self.__private_value

# obj = NameManglingDemo()

# print(f"Public: {obj.public_value}")
# print(f"Protected: {obj._protected_value}")
# # print(f"Private via method: {obj.get_private_value()}")

# # Accessing private variable using name mangling (not recommended)
# print(f"Private via name mangling: {obj._NameManglingDemo__private_value}")

# Expected Output:
# Public: 10
# Protected: 20
# Private via method: 30
# Private via name mangling: 30

# --------------------------------------------------------------------------------
# Encapsulation in Python
# --------------------------------------------------------------------------------

# ENCAPSULATION COMPREHENSIVE THEORY:

# WHAT IS ENCAPSULATION?
# - Bundling of data and methods that operate on that data within a single unit
# - Restricting direct access to some of object's components
# - Also known as data hiding

# ACCESS CONTROL IN PYTHON:
# - Public: Accessible from anywhere (no underscore)
# - Protected: Convention for internal use (_single_underscore)
# - Private: Name mangling applied (__double_underscore)

# PRIVATE MEMBERS:
# - Name mangling: _ClassName__privateMember
# - Not truly private but harder to access accidentally
# - Should only be accessed through public methods

# PROPERTIES:
# - Use @property decorator for getter methods
# - Use @attribute.setter for setter methods
# - Provide controlled access to private attributes

# ................................................................................
# Example: Bank Account with Private Attributes - Secure Banking System
# ................................................................................
# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.account_holder = account_holder
#         self.__balance = initial_balance  # Private attribute
#         self.__account_id = self.__generate_account_id()  # Private method call
    
#     def __generate_account_id(self):  # Private method
#         import random
#         return f"BANK{random.randint(10000, 99999)}"
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"Deposited ${amount}. New balance: ${self.__balance}"
#         return "Invalid deposit amount"
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             return f"Withdrew ${amount}. New balance: ${self.__balance}"
#         return "Insufficient funds or invalid amount"
    
#     def get_balance(self):
#         return f"Current balance: ${self.__balance}"
    
#     def get_account_info(self):
#         return f"Account: {self.__account_id}, Holder: {self.account_holder}"

# account = BankAccount("John Doe", 1000)
# print(account.get_account_info())
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.withdraw(2000))
# print(account.get_balance())

# Expected Output:
# Account: BANK[random], Holder: John Doe
# Deposited $500. New balance: $1500
# Withdrew $200. New balance: $1300
# Insufficient funds or invalid amount
# Current balance: $1300

# ................................................................................
# Example: Read-Only Properties with Encapsulation - Personal Information System
# ................................................................................
# class Person:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.__birth_year = birth_year  # Private attribute
    
#     @property
#     def age(self):  # Read-only property - no setter
#         return 2025 - self.__birth_year
    
#     @property
#     def birth_year(self):
#         return self.__birth_year
    
#     @birth_year.setter
#     def birth_year(self, value):
#         if 1900 <= value <= 2025:
#             self.__birth_year = value
#         else:
#             print("Invalid birth year")

# person = Person("Alice", 1990)
# print(f"Name: {person.name}")
# print(f"Age: {person.age}")
# print(f"Birth Year: {person.birth_year}")

# person.birth_year = 1985
# print(f"Updated Age: {person.age}")

# person.birth_year = 1800  # Invalid year

# Expected Output:
# Name: Alice
# Age: 34
# Birth Year: 1990
# Updated Age: 39
# Invalid birth year


# --------------------------------------------------------------------------------
# Method Overloading in Python
# --------------------------------------------------------------------------------

# METHOD OVERLOADING COMPREHENSIVE THEORY:

# WHAT IS METHOD OVERLOADING?
# - Ability to define multiple methods with same name but different parameters
# - Traditional overloading not supported in Python
# - Simulated using various techniques
         
# TECHNIQUES FOR METHOD OVERLOADING:

# 1. Default Parameters:
#    - Parameters with default values
#    - Method can be called with different number of arguments

# 2. Variable Arguments (*args):
#    - Accept any number of positional arguments
#    - Flexible parameter handling   

# 3. Keyword Arguments (**kwargs):
#    - Accept any number of keyword arguments
#    - Named parameter flexibility   

# 4. Type Checking:
#    - Check argument types at runtime
#    - Different behavior based on input types

# ................................................................................
# Example: Method Overloading with Default Parameters - Mathematical Operations
# ................................................................................
# class MathOperations:
#     def add(self, a, b=0, c=0, d=0):
#         return a + b + c + d
    
#     def multiply(self, a, b=1, c=1):
#         return a * b * c

# math = MathOperations()
# print(math.add(5))           # Single argument
# print(math.add(5, 3))        # Two arguments  
# print(math.add(5, 3, 2))     # Three arguments
# print(math.add(5, 3, 2, 1, 6))  # Four arguments
# print(math.multiply(2))      # Single argument
# print(math.multiply(2, 3))   # Two arguments
# print(math.multiply(2, 3, 4)) # Three arguments

# Expected Output:
# 5
# 8
# 10
# 11
# 2
# 6
# 24

# ................................................................................
# Example: Method Overloading with *args and **kwargs - Flexible Data Processing
# ................................................................................
# class FlexibleFunction:
#     def process_data(self, *args, **kwargs):
#         if args and not kwargs:
#             return f"Processing {len(args)} arguments: {args}"
#         elif kwargs and not args:
#             return f"Processing {len(kwargs)} keyword arguments: {kwargs}"
#         elif args and kwargs:
#             return f"Processing {len(args)} args and {len(kwargs)} kwargs"
#         else:
#             return "No arguments provided"

# flex = FlexibleFunction()
# print(flex.process_data(1, 2, 3))
# print(flex.process_data(name="Alice", age=25))
# print(flex.process_data(1, 2, 3, name="Bob", city="NYC"))
# print(flex.process_data())

# Expected Output:
# Processing 3 arguments: (1, 2, 3)
# Processing 2 keyword arguments: {'name': 'Alice', 'age': 25}
# Processing 2 args and 2 kwargs
# No arguments provided

# ................................................................................
# Example: Type-Based Method Overloading - Data Type Converter
# ................................................................................
# class Converter:
#     def convert(self, value):
#         if isinstance(value, int):
#             return f"Integer: {value}"
#         elif isinstance(value, str):
#             return f"String: {value.upper()}"
#         elif isinstance(value, list):
#             return f"List length: {len(value)}"
#         elif isinstance(value, float):
#             return f"Float: {value:.2f}"
#         else:
#             return f"Unknown type: {type(value)}"

# converter = Converter()
# print(converter.convert(42))
# print(converter.convert("hello"))
# print(converter.convert([1, 2, 3, 4]))
# print(converter.convert(3.14159))
# print(converter.convert({"key": "value"}))
# complex = 2+3j
# print(converter.convert(complex))

# Expected Output:
# Integer: 42
# String: HELLO
# List length: 4
# Float: 3.14
# Unknown type: <class 'dict'>

# ================================================================================
# Practice Questions
# ================================================================================

# EASY QUESTIONS:
# 1. Create a class 'Student' with attributes name, age, and grade, and a method to display student info
# 2. Create a 'Rectangle' class with length and width, and methods to calculate area and perimeter
# 3. Implement single inheritance: 'Vehicle' as parent and 'Car' as child class with additional attributes
# 4. Create a class with private attribute and provide getter/setter methods with validation

# MEDIUM QUESTIONS:
# 5. Implement multiple inheritance with 'Swimmer' and 'Flyer' interfaces and 'Duck' class implementing both
# 6. Create an abstract class 'Shape' with abstract methods area() and perimeter(), then implement 'Circle' and 'Rectangle'
# 7. Implement method overloading using *args and **kwargs for a 'Calculator' class that handles different operations

# HARD QUESTIONS:
# 8. Create a banking system with 'Account' abstract class and 'SavingsAccount', 'CurrentAccount' implementations with different interest rates
# 9. Implement a complete student management system using encapsulation with private attributes for student data and course enrollment
# 10. Create a class hierarchy for employees with different types (Manager, Developer, Intern) using multilevel inheritance with specific methods for each role

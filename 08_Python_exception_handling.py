"""
PYTHON EXCEPTION HANDLING 
================================================================================
PURPOSE: Exception handling prevents program crashes by managing runtime errors gracefully.
Without it, programs terminate abruptly. With it, errors are caught and handled properly.

KEY TERMS:
- Exception: Runtime error that disrupts normal program flow
- try: Block containing code that might cause exceptions
- except: Block that handles specific exceptions
- else: Executes only if no exceptions occur  
- finally: Always executes (for cleanup operations)
- raise: Manually trigger exceptions
- Built-in Exceptions: Predefined exception types in Python
"""

# ================================================================================
# 8.1 BASIC EXCEPTION HANDLING
# ================================================================================

# Example 1: Division without exception handling
# print("Example 1: Division without exception handling")
# def divide_unsafe(a, b):
#     return a / b

# try:
#     result = divide_unsafe(10, 0)
#     print(f"Result: {result}")
# except ZeroDivisionError as e:
#     print(f"Program would crash: {e}")

# Expected Output:
# Program would crash: division by zero

# Example 2: Invalid input without exception handling
# print("Example 2: Invalid input without exception handling")
# def convert_unsafe(text):
#     return int(text) 

# try:
#     value = convert_unsafe("abc")
#     print(f"Value: {value}") 
# except ValueError as e:
#     print(f"Program would crash: {e}")

# Expected Output:
# Program would crash: invalid literal for int() with base 10: 'abc'

# Example 3: File operation without exception handling
# print("Example 3: File operation without exception handling")
# def read_unsafe(filename):
#     file = open(filename, 'r')
#     return file.read()

# try:
#     content = read_unsafe("missing.txt")
#     print(f"Content: {content}")
# except FileNotFoundError as e:
#     print(f"Program would crash: {e}")

# Expected Output:
# Program would crash: [Errno 2] No such file or directory: 'missing.txt'

# Example 4: Safe division with exception handling
# print("Example 4: Safe division with exception handling")
# def divide_safe(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# print(f"10 / 0 = {divide_safe(10, 0)}")
# print(f"10 / 2 = {divide_safe(10, 2)}")


# Expected Output:
# 10 / 2 = 5.0
# 10 / 0 = Cannot divide by zero

# Example 5: Safe input conversion
# print("Example 5: Safe input conversion")
# def convert_safe(text):
#     try:
#         value = int(text)
#         return value
#     except ValueError:
#         return "Invalid number format"

# print(f"Convert '123': {convert_safe('123')}")
# print(f"Convert 'abc': {convert_safe('abc')}")

# Expected Output:
# Convert '123': 123
# Convert 'abc': Invalid number format

# Example 6: Safe file reading
# print("Example 6: Safe file reading")
# def read_safe(filename):
#     try:
#         with open(filename, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return "File not found"

# print(f"Read file: {read_safe('missing.txt')}")

# Expected Output:
# Read file: File not found

# Example 7: Using else block
# print("Example 7: Using else block")
# def process_number(input_str):
#     try:
#         number = float(input_str)
#     except ValueError:
#         return "Invalid input"
#     else:
#         return f"Valid number: {number}"

# print(f"Process '45.5': {process_number('45.5')}")
# print(f"Process 'abc': {process_number('abc')}")

# Expected Output:
# Process '45.5': Valid number: 45.5
# Process 'abc': Invalid input

# ================================================================================
# 8.2 MULTIPLE EXCEPTION HANDLING
# ================================================================================

# Example 1: Separate except blocks
# print("Example 1: Separate except blocks")
# def calculate_operations(a, b, operation):
#     try:
#         if operation == 'divide':
#             return a / b
#         elif operation == 'power':
#             return a ** b
#     except ZeroDivisionError as e:
#         return f"Division by zero error: {e}"
#     except TypeError as e:
#         return f"Type error in operation: {e}"

# print(f"Divide 10/0: {calculate_operations(10, 0, 'divide')}")
# print(f"Power 10^'a': {calculate_operations(10, 'a', 'power')}")

# Expected Output:
# Divide 10/0: Division by zero error
# Power 10^'a': Type error in operation

# Example 2: Multiple exceptions in one block
# print("Example 2: Multiple exceptions in one block")
# def process_list_data(data_list, index):
#     try:
#         value = data_list[index]
#         result = 100 / value
#         return result
#     except (IndexError, ZeroDivisionError, TypeError) as e:
#         return f"Data error: {type(e).__name__}"

# print(f"Valid data: {process_list_data([2, 3, 4], 1)}")
# print(f"Index error: {process_list_data([2, 3, 4], 5)}")
# print(f"Zero division: {process_list_data([0, 3, 4], 0)}")

# Expected Output:
# Valid data: 33.333333333333336
# Index error: Data error: IndexError
# Zero division: Data error: ZeroDivisionError

# Example 3: Specific and generic handling
# print("Example 3: Specific and generic handling")
# def comprehensive_calculator(a, b):
#     try:
#         result = a / b
#         return f"Result: {result}"
#     except ZeroDivisionError:
#         return "Specific: Cannot divide by zero"
#     except TypeError:
#         return "Specific: Invalid data types"
#     except Exception as e:
#         return f"Generic error: {e}"

# print(f"10/2: {comprehensive_calculator(10, 2)}")
# print(f"10/0: {comprehensive_calculator(10, 0)}")
# print(f"10/'a': {comprehensive_calculator(10, 'a')}")

# Expected Output:
# 10/2: Result: 5.0
# 10/0: Specific: Cannot divide by zero
# 10/'a': Specific: Invalid data types

# Example 4: Loop with exception handling
# print("Example 4: Loop with exception handling")
# def process_multiple_values(values):
#     results = []
#     for value in values:
#         try:
#             result = 100 / value
#             results.append(f"100/{value} = {result}")
#         except (ZeroDivisionError, TypeError) as e:
#             results.append(f"Error with {value}: {type(e).__name__}")
#     return results

# test_values = [10, 0, 5, "text", 25]
# results = process_multiple_values(test_values)
# for result in results:
#     print(result)

# Expected Output:
# 100/10 = 10.0
# Error with 0: ZeroDivisionError
# 100/5 = 20.0
# Error with text: TypeError
# 100/25 = 4.0

# ================================================================================
# 8.3 RAISING EXCEPTIONS
# ================================================================================

# Example 1: Basic raise
# print("Example 1: Basic raise")
# def validate_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     if age > 150:
#         raise ValueError("Age exceeds reasonable limit")
#     return f"Valid age: {age}"

# try:
#     print(validate_age(25))
#     print(validate_age(-5))
# except ValueError as e:
#     print(f"Age validation failed: {e}")

# Expected Output:
# Valid age: 25
# Age validation failed: Age cannot be negative

# Example 2: Custom exception
# print("Example 2: Custom exception")
# class TemperatureError(Exception):
#     pass

# def check_temperature(temp):
#     if temp < -50:
#         raise TemperatureError("Temperature too low")
#     if temp > 60:
#         raise TemperatureError("Temperature too high")
#     return f"Temperature OK: {temp}°C"

# try:
#     print(check_temperature(25))
#     print(check_temperature(100))
# except TemperatureError as e:
#     print(f"Temperature check failed: {e}")

# Expected Output:
# Temperature OK: 25°C
# Temperature check failed: Temperature too high

# Example 3: Raising with custom message
# print("Example 3: Raising with custom message")
# def process_salary(salary):
#     if salary < 0:
#         raise ValueError(f"Invalid salary: {salary}. Must be positive.")
#     if salary > 1000000: 
#         raise ValueError(f"Salary {salary} exceeds maximum limit.")
#     return f"Salary processed: ${salary}"

# try:
#     print(process_salary(50000))
#     print(process_salary(-5000))
# except ValueError as e:
#     print(f"Salary processing error: {e}")

# Expected Output:
# Salary processed: $50000
# Salary processing error: Invalid salary: -5000. Must be positive.

# ================================================================================
# 8.4 FINALLY KEYWORD
# ================================================================================

# Example 1: Basic finally
# print("Example 1: Basic finally")
# def basic_finally_example(number):
#     try:
#         result = 100 / number # it is positive 
#         print(f"Calculation result: {result}") # it is negative
#     except ZeroDivisionError:
#         print("Division by zero occurred") 
#     finally:
#         print("Finally block executed") # we don't positve or negative it is neatural.

# print("Testing with 5:")
# basic_finally_example(5)
# print("\nTesting with 0:")
# basic_finally_example(0)

# Expected Output:
# Testing with 5:
# Calculation result: 20.0
# Finally block executed


# Testing with 0:
# Division by zero occurred
# Finally block executed

# Example 2: File operations with finally
# print("Example 2: File operations with finally")
# def read_file_safely(filename):
#     file = None
#     try:
#         file = open(filename, 'r')
#         content = file.read()
#         print(f"File content: {content}")
#         return content
#     except FileNotFoundError:
#         print("File not found")
#         return None
#     finally:
#         if file:
#             file.close()
#             print("File closed in finally block")

# print("Reading non-existent file:")
# read_file_safely("missing.txt")

# Expected Output:
# Reading non-existent file:
# File not found
# File closed in finally block

# Example 3: Finally with return
# print("Example 3: Finally with return")
# def process_data(value):
#     try:
#         if value < 0:
#             return "Negative value"
#         result = value * 2
#         return f"Result: {result}"
#     finally:
#         print("Cleanup completed for value:", value)

# print(f"Positive: {process_data(10)}")
# print(f"Negative: {process_data(-5)}")

# Expected Output:
# Cleanup completed for value: 10
# Positive: Result: 20
# Cleanup completed for value: -5
# Negative: Negative value

# Example 4: Database connection simulation
# print("Example 4: Database connection simulation")
# class Database:
#     def connect(self):
#         print("Database connected")
    
#     def disconnect(self):
#         print("Database disconnected")
    
#     def query(self, sql):
#         if "DROP" in sql.upper():
#             raise ValueError("Dangerous query detected")
#         return f"Executed: {sql}"

# def database_operation(sql):
#     db = Database()
#     db.connect()
#     try:
#         result = db.query(sql)
#         print(result)
#         return result
#     except ValueError as e:
#         print(f"Query error: {e}")
#         return None
#     finally:
#         db.disconnect()

# print("Safe query:")
# database_operation("SELECT * FROM users")
# print("\nDangerous query:")
# database_operation("DROP TABLE users")

# Expected Output:
# Safe query:
# Database connected
# Executed: SELECT * FROM users
# Database disconnected

# Dangerous query:
# Database connected
# Query error: Dangerous query detected
# Database disconnected



# ================================================================================
# 8.5 BUILT-IN EXCEPTIONS
# ================================================================================

# Example 1: Common built-in exceptions
# print("Example 1: Common built-in exceptions")
# def demonstrate_exceptions():
#     test_cases = [
#         ("ZeroDivisionError", "10 / 0"),
#         ("ValueError", "int('abc')"),
#         ("TypeError", "'text' + 123"),
#         ("IndexError", "[1,2,3][10]"),
#         ("KeyError", "{'a':1}['b']"),
#         ("FileNotFoundError", "open('missing.txt')"),
#         ("AttributeError", "'hello'.nonexistent()"),
#     ]
    
#     for name, code in test_cases:
#         try:
#             result = eval(code)
#             print(f"{name}: Success - {result}")
#         except Exception as e:
#             print(f"{name}: {type(e).__name__} - {e}")

# demonstrate_exceptions()

# Expected Output:
# ZeroDivisionError: ZeroDivisionError - division by zero
# ValueError: ValueError - invalid literal for int() with base 10: 'abc'
# TypeError: TypeError - can only concatenate str (not "int") to str
# IndexError: IndexError - list index out of range
# KeyError: KeyError - 'b'
# FileNotFoundError: FileNotFoundError - [Errno 2] No such file or directory: 'missing.txt'
# AttributeError: AttributeError - 'str' object has no attribute 'nonexistent'

# Example 2: Handling specific built-in exceptions
# print("Example 2: Handling specific built-in exceptions")
# def handle_specific_errors(data, key, divisor):
#     try:
#         value = data[key]
#         result = value / divisor
#         return f"Final result: {result}"
#     except KeyError:
#         return "Error: Key not found"
#     except TypeError:
#         return "Error: Invalid data type"
#     except ZeroDivisionError:
#         return "Error: Division by zero"

# data_dict = {'temp': 25, 'pressure': 1013}
# print(f"Valid: {handle_specific_errors(data_dict, 'temp', 5)}")
# print(f"Key error: {handle_specific_errors(data_dict, 'humidity', 5)}")
# print(f"Type error: {handle_specific_errors({'temp': 'hot'}, 'temp', 5)}")

# Expected Output:
# Valid: Final result: 5.0
# Key error: Error: Key not found
# Type error: Error: Invalid data type

# Example 3: Multiple built-in exception handling
# print("Example 3: Multiple built-in exception handling")
# def comprehensive_data_processor(values, index, operation):
#     try:
#         value = values[index]
        
#         if operation == 'sqrt':
#             if value < 0:
#                 raise ValueError("Cannot sqrt negative number")
#             result = value ** 0.5
#         elif operation == 'reciprocal':
#             result = 1 / value
        
#         return f"Operation result: {result}"
    
#     except IndexError:
#         return "Error: Index out of range"
#     except ValueError as e:
#         return f"Value error: {e}"
#     except ZeroDivisionError:
#         return "Error: Division by zero"
#     except TypeError:
#         return "Error: Invalid data type"

# numbers = [4, 9, 16, 25]
# print(f"Valid sqrt: {comprehensive_data_processor(numbers, 1, 'sqrt')}")
# print(f"Index error: {comprehensive_data_processor(numbers, 10, 'sqrt')}")
# print(f"Negative sqrt: {comprehensive_data_processor([-4], 0, 'sqrt')}")

# Expected Output:
# Valid sqrt: Operation result: 3.0
# Index error: Error: Index out of range
# Negative sqrt: Value error: Cannot sqrt negative number

# Example 4: Real-world application
# print("Example 4: Real-world application")
# def student_grade_calculator(scores):
#     try:
#         if not scores:
#             raise ValueError("No scores provided")
        
#         if any(score < 0 or score > 100 for score in scores):
#             raise ValueError("Scores must be between 0 and 100")
        
#         average = sum(scores) / len(scores)
        
#         if any(isinstance(score, str) for score in scores):
#             raise TypeError("Scores must be numbers")
        
#         return f"Average grade: {average:.2f}"
    
#     except ValueError as e:
#         return f"Data validation error: {e}"
#     except TypeError as e:
#         return f"Type error: {e}"
#     except ZeroDivisionError:
#         return "Error: Cannot calculate average of empty list"

# print(f"Valid grades: {student_grade_calculator([85, 92, 78, 96])}")
# print(f"Empty list: {student_grade_calculator([])}")
# print(f"Invalid grades: {student_grade_calculator([85, 105, 78])}")
# print(f"String grades: {student_grade_calculator([85, 'A', 78])}")

# Expected Output:
# Valid grades: Average grade: 87.75
# Empty list: Data validation error: No scores provided
# Invalid grades: Data validation error: Scores must be between 0 and 100
# String grades: Type error: Scores must be numbers
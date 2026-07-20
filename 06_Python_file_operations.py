"""
PYTHON FILE HANDLING - COMPREHENSIVE GUIDE
================================================================================
PURPOSE: File handling allows Python programs to read from and write to files, 
enabling data persistence and external data processing.

KEY TERMS:
- File I/O: Input/Output operations with files
- CSV: Comma Separated Values file format
- Excel: Spreadsheet file format (.xlsx, .xls)
- JSON: JavaScript Object Notation for data interchange
- Context Manager: Manages resources using 'with' statement
- Mode: File opening mode (r, w, a, r+, etc.)
- Encoding: Character encoding for text files
"""

# with open('sample_16_11.txt', 'r') as sample_16_11_r:
#     data = sample_16_11_r.read()
#     print(data)

# with open('sample_16_11.txt', 'w') as sample_16_11_w:
#     sample_16_11_w.write("My name is John. I am learning Python file handling. \n")

# # access the file and modify specified line in the file.
# with open('sample_16_11.txt', 'r') as sample_16_11_r:
#     data = sample_16_11_r.readlines()   
# modified_line = "My name is John. I am learning Python file handling and it is fun. \n"
# data[0] = modified_line

# with open('sample_16_11.txt', 'w') as sample_16_11_w:
#     sample_16_11_w.writelines(data)

# with open('sample_16_11.txt', 'r') as file:
#     last_line = None
#     for line in file:
#         last_line = line 
#     if last_line is not None:
#         print(last_line)  


# ================================================================================
# 9.1 PYTHON FILES I/O
# ================================================================================

# Example 1: Basic file writing and reading
# print("# Example 1: Basic file writing and reading")
# with open('sample.txt', 'w') as file:
#     file.write("Hello, World!\n")
#     file.write("This is a sample text file.\n")
#     file.write("Python File Handling Demo.\n")

# with open('sample.txt', 'r') as file:
#     content = file.read()
#     print("File content:")
#     print(content)

# Expected Output:
# File content:
# Hello, World!
# This is a sample text file.
# Python File Handling Demo.

# Example 2: Reading file line by line
# print("\n# Example 2: Reading file line by line")
# with open('sample.txt', 'r') as file:
#     print("Reading line by line:")
#     for line_num, line in enumerate(file, 1):
#         if line_num == 1:
#             print(f"Line {line_num}: {line.strip()}")

# Expected Output:
# Reading line by line:
# Line 1: Hello, World!
# Line 2: This is a sample text file.
# Line 3: Python File Handling Demo.


# Example 3: File append mode
# print("\n# Example 3: File append mode")
# with open('sample.txt', 'a') as file:
#     file.write("This line was appended.\n")
#     file.write("Another appended line.\n")

# with open('sample.txt', 'r') as file:
#     print("After appending:")
#     print(file.read())

# Expected Output:
# After appending:
# Hello, World!
# This is a sample text file.
# Python File Handling Demo.
# This line was appended.
# Another appended line.

# Example 4: File modes demonstration
# print("\n# Example 4: File modes demonstration")
# try:
#     with open('data.txt', 'w') as f:
#         f.write("Line 1\nLine 2\nLine 3\n")
    
#     with open('data.txt', 'r+') as f:
#         content = f.read()
#         f.write("Line 4 - written with r+\n")
#         print("r+ mode - read then write:")
#         print(content + "Line 4 - written with r+")
        
# except Exception as e:
#     print(f"Error: {e}")

# Expected Output:
# r+ mode - read then write:
# Line 1
# Line 2
# Line 3
# Line 4 - written with r+


# ================================================================================
# 9.2 PYTHON READ CSV FILE
# ================================================================================

# import csv

# with open('employees_data.csv', 'r') as employees_data:
#     content = csv.reader(employees_data)
#     rows_limit = 2
#     for i, rows in enumerate(content):
#         if i == 0:
#             continue
#         if i > rows_limit:
#             break
#         print(f"Index at: {i}: {rows}")

# new_employee = [
#     [105, 'John', '555-555-555']
# ]

# with open('employees_data.csv', 'a', newline='') as employees_data:
#     new_record_writer = csv.writer(employees_data)
#     new_record_writer.writerows(new_employee)

# employees_data = [
#     ['ID', 'Name', 'Salary'], 
#     [3, 'Sri', 12000]
# ]

# with open('employees_data_01.csv', 'w', newline='') as employees_data_01:
#     csv_writer = csv.writer(employees_data_01)
#     csv_writer.writerows(employees_data)

# with open('employees_data_01.csv', 'r') as employees_data_01:
#     content = csv.reader(employees_data_01)
#     for i, rows in enumerate(content):
#         if len(rows) == 0:
#             continue
#         print(f"Index at: {i}: {rows}") 


# import csv

# Example 1: Reading CSV with csv.reader
# print("\n# Example 1: Reading CSV with csv.reader")
# csv_data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', '25', 'New York'],
#     ['Bob', '30', 'London'],
#     ['Charlie', '35', 'Tokyo']
# ]

# with open('people.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(csv_data)

# with open('people.csv', 'r') as file:
#     reader = csv.reader(file)
#     print("CSV content:")
#     for row in reader:
#         print(row)

# Expected Output:
# CSV content:
# ['Name', 'Age', 'City']
# ['Alice', '25', 'New York']
# ['Bob', '30', 'London']
# ['Charlie', '35', 'Tokyo']

# Example 2: Reading CSV with DictReader
# print("\n# Example 2: Reading CSV with DictReader")
# with open('people.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     print("CSV as dictionaries:")
#     for record in reader:
#         print(record)

# Expected Output:
# CSV as dictionaries:
# {'Name': 'Alice', 'Age': '25', 'City': 'New York'}
# {'Name': 'Bob', 'Age': '30', 'City': 'London'}
# {'Name': 'Charlie', 'Age': '35', 'City': 'Tokyo'}

# Example 3: Reading CSV with different delimiter
# print("\n# Example 3: Reading CSV with different delimiter")
# pipe_data = [
#     ['Product', 'Price', 'Quantity'],
#     ['Laptop', '999.99', '5'],
#     ['Mouse', '25.50', '20'],
#     ['Keyboard', '75.00', '15']
# ]

# with open('products.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerows(pipe_data)

# with open('products.csv', 'r') as file:
#     reader = csv.reader(file, delimiter='|')
#     print("Pipe-delimited CSV:")
#     for row in reader:
#         print(row)

# Expected Output:
# Pipe-delimited CSV:
# ['Product', 'Price', 'Quantity']
# ['Laptop', '999.99', '5']
# ['Mouse', '25.50', '20']
# ['Keyboard', '75.00', '15']


# x = 2.6
# print(type(x))


# ================================================================================
# 9.3 PYTHON WRITE CSV FILE
# ================================================================================

# Example 1: Writing CSV with csv.writer
# import csv


# print("\n# Example 1: Writing CSV with csv.writer")
# students = [
#     ['StudentID', 'Name', 'Grade', 'Marks'],
#     ['S001', 'John Doe', 'A', '95'],
#     ['S002', 'Jane Smith', 'B', '85'],
#     ['S003', 'Mike Johnson', 'A', '92']
# ]
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(students)

# with open('students.csv', 'r') as file:
#     print("Written CSV file:")
#     print(file.read())

# Example 2: Writing CSV with DictWriter
# print("\n# Example 2: Writing CSV with DictWriter")
# employees = [
#     {'Name': 'Alice Brown', 'Department': 'IT', 'Salary': '75000'},
#     {'Name': 'Bob Wilson', 'Department': 'HR', 'Salary': '60000'},
#     {'Name': 'Carol Davis', 'Department': 'Finance', 'Salary': '80000'}
# ]

# with open('employees.csv', 'w', newline='') as file:
#     fieldnames = ['Name', 'Department', 'Salary']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(employees)

# with open('employees.csv', 'r') as file:
#     print("Employees CSV:")
#     print(file.read())

# Expected Output:
# Employees CSV:
# Name,Department,Salary
# Alice Brown,IT,75000
# Bob Wilson,HR,60000
# Carol Davis,Finance,80000

# Example 3: Appending to CSV file
# print("\n# Example 3: Appending to CSV file")
# new_employees = [
#     {'Name': 'David Lee', 'Department': 'Marketing', 'Salary': '65000'},
#     {'Name': 'Eva Chen', 'Department': 'IT', 'Salary': '78000'}
# ]

# with open('employees.csv', 'a', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writerows(new_employees)

# with open('employees.csv', 'r') as file:
#     print("After appending:")
#     print(file.read())

# Expected Output:
# After appending:
# Name,Department,Salary
# Alice Brown,IT,75000
# Bob Wilson,HR,60000
# Carol Davis,Finance,80000
# David Lee,Marketing,65000
# Eva Chen,IT,78000


# try:
#     import pandas as pd  # type: ignore[import]
    
#     # Example 1: Writing DataFrame to Excel
#     print("\n# Example 1: Writing DataFrame to Excel")
    
#     sales_data = {
#         'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
#         'Revenue': [50000, 55000, 52000, 58000, 60000],
#         'Expenses': [35000, 36000, 35500, 37000, 38000],
#         'Profit': [15000, 19000, 16500, 21000, 22000]
#     }
    
#     sales_df = pd.DataFrame(sales_data)
#     sales_df.to_excel('sales_report.xlsx', index=False, sheet_name='Sales_2024')
    
#     print("Sales data written to Excel:")
#     print(sales_df)


# except ImportError:
#     print("pandas library not available for Excel operations")


# ================================================================================
# 9.6 PYTHON JSON
# ================================================================================

# import json

# #Example 1: Writing and reading JSON
# print("\n# Example 1: Writing and reading JSON")
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "hobbies": ["reading", "swimming", "coding"],
#     "married": False,
#     "children": None
# }

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# with open('person.json', 'r') as file:
#     loaded_person = json.load(file)
#     print("JSON data:")
#     print(json.dumps(loaded_person, indent=2))

# Expected Output:
# JSON data:
# {
#   "name": "Alice",
#   "age": 30,
#   "city": "New York",
#   "hobbies": [
#     "reading",
#     "swimming",
#     "coding"
#   ],
#   "married": false,
#   "children": null
# }


# Example 2: JSON with lists and nested structures
# print("\n# Example 2: JSON with lists and nested structures")
# company = {
#     "company_name": "Tech Corp",
#     "employees": [
#         {
#             "id": 1,
#             "name": "John Doe",
#             "position": "Developer",
#             "skills": ["Python", "JavaScript", "SQL"]
#         },
#         {
#             "id": 2,
#             "name": "Jane Smith",
#             "position": "Designer",
#             "skills": ["Photoshop", "Figma", "UI/UX"]
#         }
#     ],
#     "founded": 2010,
#     "departments": ["IT", "HR", "Finance", "Marketing"]
# }

# with open('company.json', 'w') as file:
#     json.dump(company, file, indent=4)

# with open('company.json', 'r') as file:
#     loaded_company = json.load(file)
#     print("Company data:")
#     print(f"Company: {loaded_company['company_name']}")
#     print(f"Employees: {len(loaded_company['employees'])}")
#     for emp in loaded_company['employees']:
#         print(f"  - {emp['name']} ({emp['position']})")

# Expected Output:
# Company data:
# Company: Tech Corp
# Employees: 2
#   - John Doe (Developer)
#   - Jane Smith (Designer)

# Example 3: JSON string conversion
# print("\n# Example 3: JSON string conversion")
# python_dict = {"name": "Bob", "scores": [85, 92, 78], "active": True}

# Convert to JSON string
# json_string = json.dumps(python_dict, indent=2)
# print("Python to JSON string:")
# print(json_string)

# Convert back to Python
# python_data = json.loads(json_string)
# print("\nJSON back to Python:")
# print(python_data)

# Expected Output:
# Python to JSON string:
# {
#   "name": "Bob",
#   "scores": [
#     85,
#     92,
#     78
#   ],
#   "active": true
# }
# 
# JSON back to Python:
# {'name': 'Bob', 'scores': [85, 92, 78], 'active': True}

# ================================================================================
# 9.7 CONTEXT MANAGER IN PYTHON
# ================================================================================

# Example 1: Using built-in context managers
# print("# Example 1: Using built-in context managers")
# print("File context manager:")
# with open('context_demo.txt', 'w') as f:
#     f.write("This file is automatically closed.\n")
#     f.write("No need to call close() manually.\n")
#     print("File written successfully")

# File is automatically closed here

# Expected Output:
# File context manager:
# File written successfully

# Example 2: Custom context manager class
# print("\n# Example 2: Custom context manager class")
# class Timer:
#     def __init__(self, name):
#         self.name = name
    
#     def __enter__(self):
#         print(f"Starting {self.name}...")
#         return self
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"Finished {self.name}")
#         if exc_type:
#             print(f"An error occurred: {exc_val}")
#         return True  # Suppress exceptions

# with Timer("data processing"):
#     print("Processing data...")
#     result = 10 + 20
#     print(f"Result: {result}")

# Expected Output:
# Starting data processing...
# Processing data...
# Result: 30
# Finished data processing

# Example 3: Context manager with file operations
# print("\n# Example 3: Context manager with file operations")
# class FileLogger:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = None
    
#     def __enter__(self):
#         self.file = open(self.filename, 'a')
#         self.file.write("=== Log Started ===\n")
#         return self
    
#     def log(self, message):
#         timestamp = "2024-01-15 10:30:00"  # Simulated timestamp
#         self.file.write(f"[{timestamp}] {message}\n")
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.write("=== Log Ended ===\n")
#         self.file.close()

# with FileLogger('app.log') as logger:
#     logger.log("Application started")
#     logger.log("User logged in")
#     logger.log("Data processed successfully")

# with open('app.log', 'r') as f:
#     print("Log file content:")
#     print(f.read())

# Expected Output:
# Log file content:
# === Log Started ===
# [2024-01-15 10:30:00] Application started
# [2024-01-15 10:30:00] User logged in
# [2024-01-15 10:30:00] Data processed successfully
# === Log Ended ===

# Example 4: Context manager for database connection simulation
# print("\n# Example 4: Context manager for database connection simulation")
# class DatabaseConnection:
#     def __init__(self, db_name):
#         self.db_name = db_name
#         self.connected = False
    
#     def __enter__(self):
#         self.connected = True
#         print(f"Connected to database: {self.db_name}")
#         return self
    
#     def execute(self, query):
#         if not self.connected:
#             raise ConnectionError("Not connected to database")
#         print(f"Executing: {query}")
#         return f"Result of: {query}"
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connected = False
#         print(f"Disconnected from database: {self.db_name}")
#         if exc_type:
#             print(f"Database error: {exc_val}")

# with DatabaseConnection("my_database") as db:
#     result1 = db.execute("SELECT * FROM users")
#     result2 = db.execute("UPDATE products SET price = 100")
#     print(result1)
#     print(result2)

# Expected Output:
# Connected to database: my_database
# Executing: SELECT * FROM users
# Executing: UPDATE products SET price = 100
# Result of: SELECT * FROM users
# Result of: UPDATE products SET price = 100
# Disconnected from database: my_database
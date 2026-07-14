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

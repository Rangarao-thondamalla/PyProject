# ======================================
# 4. Python Data Structures
# ======================================
# Understand Python data structures
# • Create and manipulate Lists, Tuples, Sets and Dictionaries
# • Learn common methods
# • Compare different data structures

# ======================================
# ## Python User Input
# ======================================

# var1 = int(input("Enter fisrt number: "))
# var2 = int(input("Enter second number: "))
# print(type(var1))
# print(type(var2))
# sum = var1 + var2
# print(sum)

# name = float(input("Enter your name: ")) # floating value = 10.22
# print(type(name))
# print("Your name is: ",name)

# ------------------------------
# 4.1 Python Lists
# ------------------------------

# 1. A list is an ordered, mutable (changeable) collection of elements.
# 2. Lists can contain different data types. ex: integer, number, string, boolean.
# 3. Syntax: my_list = [item1, item2, item3] [ srqare brackets are used to define a list], 
# it starts with 0 index, and can be accessed using index values.
# we can modify, add, remove elements from a list.

# Example 1: Creating and printing a list
# fruits = ["apple", "cherry", "banana"] # index 0,1,2
# # for fruit in fruits:
# #     if fruit == "apple":
# #         print("i found apple")

# print(len(fruits)) # 3

# # Example 2: Accessing elements using index
# print(fruits[0])    # apple
# print(fruits[-1])   # banana 
# # why -1 is used to access the last element in the list. 
# # It is a negative index that counts from the end of the list, 
# # with -1 referring to the last item, -2 to the second last, and so on.
# print(fruits[1:3])  # cherry, banana


# Example 4: List slicing
# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# print(numbers[1:3])   # [20, 30] # [1:3] means start from index 1 (inclusive) and go up to index 3 (exclusive), 
# # so it includes elements at index 1 and 2.
# print(numbers[:3])    # [10, 20, 30]
# print(numbers[2:5])    # [30, 40, 50]

# Example 3: Zipping Two Lists
# fruits = ["apple", "banana", "cherry", "mango"]
# colors = ["red", "yellow", "dark red","green"]
# for fruit, color in zip(fruits, colors):
#     print(fruit, "→", color)

# ------------------------------
# 4.2 Python List Methods
# ------------------------------
# Common Methods with Examples

# append(value)
# my_list = [1, 2]
# print(my_list)
# my_list.append(3)
# my_list.append("Apple")
# my_list.append([10.11, -10])
# print(my_list)   # [1, 2, 3]

# list methods: extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()

# extend() example
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)  # [1, 2, 3, 4, 5, 6]

# insert(position, values)
# print(my_list)
# my_list.insert(1, 10)
# print(my_list)
# my_list.insert(2, 100)
# print(my_list)   # [1, 10, 2, 3]

# remove(value)
# my_list = [2, 1, 1, 2]
# my_list.remove(1)
# print(my_list)  

# pop()
# my_list = [2, 1, 1, 2]
# print(my_list.pop())  
# print(my_list)        

# sort()
# nums = [3, 1, 2]
# nums.sort()
# print(nums)   # [1, 2, 3]
# names = ['a', 'b', 'z', 'x']
# print(names)
# names.sort()
# print(names)

# reverse()
# nums.reverse()
# print(nums)   # [3, 2, 1]
# names.reverse()
# print(names)


# ------------------------------
# 4.3 Python Tuples
# ------------------------------

# 1. Tuples are ordered but immutable (cannot be changed).
# 2. Defined using parentheses ().
# 3. Useful for fixed collections of items.
# Syntax: my_tuple = (item1, item2, item3)

# Example 1: Creating tuple
# colors = ("red", "green", "blue")
# print(colors)

# # Example 2: Accessing elements
# print(colors[0])    # red
# print(colors[-1])   # blue

# # Example 3: Attempting modification (will error)
# colors[0] = "yellow"   # TypeError

# Example 1: Concatenating Tuples
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# result = t1 + t2
# print("Concatenated:", result)   # (1, 2, 3, 4, 5, 6)

# Example 2: Repeating Tuples
# t = (7, 8)
# print("Repeated:", t * 3)        # (7, 8, 7, 8, 7, 8)

# Example 3: Iterating with Index
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ("red", "yellow", "dark red")
# for i in range(len(tuple1)):
#     print(tuple1[i], "→", tuple2[i])

# Example 4: Using Zip with Tuples
# colors = ("blue", "green", "orange", "red")
# fruits = ("berry", "melon", "mango")
# for c, f in zip(colors, fruits):
#     print(c, "matches with", f)

# Example 5: Nesting Tuples
# tup1 = (1, 2)
# tup2 = (3, 4)
# nested = (tup1, tup2)
# print("Nested Tuple:", nested)   # ((1, 2), (3, 4))
# print(nested[0])


# ------------------------------
# 4.4 Python Tuple Methods
# ------------------------------
# count()
nums = (1, 2, 2, 3,3,3,3,4,5,6,7,8,9)
print(nums.count(3))   # 4

# index()
# print(nums.index(2))   # 3
# print(len(nums))

# Taking input from use & type casting list to tuple
# numbers = []

# while True:
#     number = int(input("Enter the tuple element: "))
#     if number == 10:
#         break
#     numbers.append(number)

# print(type(numbers))
# print(numbers)
# numbers_tuple = tuple(numbers)    
# print(type(numbers_tuple))    
# print(numbers_tuple)

# tuple methods: count(), index() 

# 4.5 Difference between List and Tuple
# ------------------------------
# 1. List → mutable, Tuple → immutable
# 2. List uses [], Tuple uses ()
# 3. Lists are slower than tuples because of mutability



# ------------------------------
# 4.6 Python Sets
# ------------------------------

# 1. A set is an unordered collection of unique items.
# 2. Defined using curly braces {1,2,3}.
# 3. No duplicate elements allowed.

# Example 1: Creating a set
# my_set = {1, 2, 3, 2, 2, 2, 3, 1}
# print(type(my_set))
# print(my_set)   # {1, 2, 3}

# emails = {'ajay@gmail.com', 'srilakshmi@gmail.com', 'pradeep@gmail.com', 'ajay@gmail.com', None, None, 10, 10.11}
# print(type(emails))
# print(emails)


# list_names = ['Ajay', 'Srilakshmi', 'Pradeep', 'Saket', 'Sridhar', 'Rami', 'Sridhar']
# print(list_names)
# list_names = set(list_names)
# print(list_names)

# Example 2: Adding element
# my_set.add(4)
# print(my_set)   # {1, 2, 3, 4}

# Example 3: Removing element
# my_set.remove(20)
# print(my_set)   # {1, 3, 4}

# Working with Two Sets

# Example 1: Union (all unique elements from both sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# print("Union:", set1 | set2)        # {1, 2, 3, 4, 5}
# print("Union (method):", set1.union(set2))
# print(set1)
# set3 = set1 + set2
# print(set3)

# Example 2: Intersection (common elements)
# print("Intersection:", set1 & set2)   # {3}
# print("Intersection (method):", set1.intersection(set2))

# Example 3: Difference (elements in set1 but not in set2)
# print("Difference:", set1 - set2)     # {1, 2}
# print("Difference (method):", set2.difference(set1)) # {4, 5}

# Example 4: Symmetric Difference (elements in either but not both)
# print("Symmetric Difference:", set1 ^ set2)  # {1, 2, 4, 5}
# print("Symmetric Difference (method):", set1.symmetric_difference(set2))

# Example 5: Iterating Two Sets Together
# names = {"Alice", "Bob", "Ajay"}
# roles = {"Admin", "User", "Editor"}
# for n, r in zip(names, roles):
#     print(n, "→", r)

# Example 6: Subset and Superset
# a = {1, 2}
# b = {1, 2, 3, 4}

# print("a is subset of b:", a.issubset(b))    # True
# print("b is superset of a:", b.issuperset(a)) # True
# print("a is superset of b:", a.issuperset(b)) # False

# ------------------------------
# 4.7 Python Set Methods
# ------------------------------
# a = {1, 2, 3}
# b = {3, 4, 5}

# # union()
# print(a.union(b))     # {1, 2, 3, 4, 5} 

# # intersection()
# print(a.intersection(b))   # {3}

# # difference()
# print(a.difference(b))     # {1, 2}


# ------------------------------
# 4.8 Python Dictionary
# ------------------------------

# 1. A dictionary is an unordered collection of key-value pairs.
# 2. Defined using curly braces {} with keys and values.
# 3. Keys must be unique and immutable; values can be anything.

# Example 1: Creating dictionary
# student = {"name": "Alice", "age": 21, "name": "Bob", "f_name": "Bob"}
# print(student)
# keys = student.keys()
# print(type(keys))
# print(keys)
# count = len(student)
# print(count)
# print(student.values())

# # Example 2: Accessing values
# print(student["name"])   # Alice

# # Example 3: Updating values
# student["age"] = 22
# print(student)

# # Example 4: Adding new key-value
# student["course"] = "Python"
# print(student)

# # Example 5: Removing key-value
# student.pop("age")
# print(student)

# 1. Disctory several keys value pairs but list does not have key value pairs
# 2. list are like tuple we can change the values.
# 3. in set there no duplicate values.


# Working with Two Dictionaries

# Example 1: Merging Two Dictionaries (Python 3.9+)
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merge = dict1 | dict2d
# print("Merged:", merged)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 2: Merging with Update (modifies dict1)
# dict1.update(dict2)
# print("After update:", dict1)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(dict2) # No change

# Example 3: Iterating Two Dicts Together
# names = {"id1": "Alice", "id2": "Bob", "id3": "Charlie", "id4": "Ajay"}
# print(names["id2"])
# keys = list(names.keys())
# print(keys)
# len_dict = len(names)
# print(len_dict)
# i = 0
# while i < len_dict:
#     key = keys[i]
#     value = names[key]
#     print(key + ":" + value)
#     i += 1

# if "id7" in names:
#     print("present") 
# else:
#     print("Not present")     

# value = names.get("id9")
# print(value)

# roles = {"id1": "Admin", "id2": "User", "id3": "Editor", "id4": "Learner"}
# for key in names:
#     print(names[key], "→", roles[key])

# Example 4: Dictionary Comprehension with Two Dicts
# prices1 = {"apple": 50, "banana": 30}
# prices2 = {"banana": 40, "cherry": 60}
# take higher price for common fruits
# combined = {k: max(prices1.get(k, 0), prices2.get(k, 0)) for k in set(prices1) | set(prices2)}
# print("Combined Prices:", combined)  
# {'apple': 50, 'banana': 40, 'cherry': 60}

# Example 5: Zipping Two Dicts
# keys = {"k1": 1, "k2": 2}
# values = {"v1": "A", "v2": "B"}
# zipped_dict = dict(zip(keys, values))
# print("Zipped Dict:", zipped_dict)   # {'k1': 'v1', 'k2': 'v2'}

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.9 Python Dictionary Methods
# ------------------------------
# person = {"name": "Bob", "age": 25}

# keys()
# print(person.keys())    # dict_keys(['name', 'age'])

# values()
# print(person.values())  # dict_values(['Bob', 25])

# items()
# print(person.items())   # dict_items([('name', 'Bob'), ('age', 25)])

# get()
# print(person.get("name"))   # Bob

# pop()
# person.pop("age")
# print(person)    # {"name": "Bob"}

# ------------------------------
# 4.10 Difference between List and Dictionary 
# ------------------------------
# 1. List stores items in order by index, Dictionary stores data as key-value pairs.
# 2. List accessed by index, Dictionary accessed by key.
# 3. Lists allow duplicate items, Dictionary keys must be unique.


# ------------------------------
# 4.11 Difference between List, Set, Tuple, and Dictionary
# ------------------------------
# List → Ordered, mutable, duplicates allowed.
# Tuple → Ordered, immutable, duplicates allowed.
# Set → Unordered, mutable, unique elements only.
# Dictionary → Unordered, key-value pairs, keys unique.


# ------------------------------
# 4.12 Difference between Set and Dictionary
# ------------------------------
# 1. Set contains only values, Dictionary contains key-value pairs.
# 2. Syntax: Set → {1,2,3}, Dictionary → {"a":1, "b":2}.
# 3. Set used for membership testing and unique storage.
# 4. Dictionary used for mapping relationships between keys and values.

# ============================================================
# Practice Questions: Python Data Structures
# ============================================================

# 1. Create a list of 5 numbers. 
#    - Print the first and last element. 
#    - Add a new element to the list and display it.

# 2. Write a program to count how many times the value "apple" 
#    appears in a given list using a list method.

# 3. Create a tuple with 4 strings. 
#    - Print the second element. 
#    - Try to modify one element and explain why it fails.

# 4. Create a set with duplicate values and print it.  
#    - Observe how duplicates are handled.  

# 5. Create a dictionary with keys as student names and values as marks.  
#    - Access the marks of one student using their name as the key.

# 6. Create two lists: one with student names, another with their ages.  
#    - Combine them into a dictionary using `zip()`.  
#    - Print each student’s name and age.

# 7. Write a program to demonstrate the difference between a List and a Set  
#    by inserting duplicate values into both and printing the results.

# 8. Create a dictionary of 5 products with prices.  
#    - Add a new product.  
#    - Update an existing product’s price.  
#    - Remove one product using a dictionary method.

# 9. Given two sets of student roll numbers (one for sports, one for music club):  
#    - Find students who are in both clubs (intersection).  
#    - Find students only in sports but not in music (difference).  
#    - Find all students in either club (union).

# 10. Write a program to compare List, Tuple, Set, and Dictionary:  
#     - Create a List of numbers, Tuple of numbers, Set of numbers,  
#       and Dictionary (with index as key, number as value).  
#     - Print all and explain the differences in:
#       - Order  
#       - Duplicates allowed or not  
#       - Mutability (changeable or not)  

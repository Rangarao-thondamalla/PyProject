# ============================
# 3. Python Control Statements 
# ============================ 

# Example 1: Simple If-Else
# age = 18
# if age >= 18: (one condition)
#     print("Eligible to vote")
# else:
#     print("Not eligible")

#Example 2: If-Elif-Else
# marks = 55.9
# if marks >= 90: (if the marks are greater than or equal to 90)
#     print("Grade: A")
# elif marks >= 60: (if the marks are greater than or equal to 60)
#     print("Grade: B")
# elif marks >= 50: (if the marks are greater than or equal to 50)  
#     print("Grade: C")
# else:
#     print("Invalid entry")

# Example 3: Nested If
# num = 1
# if num >= 0: 
#     if num == 0:
#         print("Zero")
#     elif num == 1:
#         print("One")        
#     else:
#         print("Positive")
# else:
#     print("Negative")

# Example 4: Multiple Conditions with 'and'
# salary = 40000
# experience = 1
# if salary >= 40000 and experience >= 2: # 2 true conditions # salary is greater than 40000 and experience is greater than or equal to 2
#     print("Eligible for promotion")
# else:
#     print("Not eligible")
# and will expect both conditions to be true, while or will expect at least one condition to be true.


# Invalid Scenarios
# if without colon → SyntaxError
# if age >= 18
#     print("Eligible")

# Misleading truthy/falsy check
# if "5":
#     print("Runs because 5 → True")

# if "":
#     print("Does not run because '' → False")

# ---------------------------------------------------------------------------------------------

# ======================================
# 3.2 Python Loops 
# ======================================


# 1. Loops are used to repeat a block of code multiple times.
# 2. Python supports two main types of loops: for loop and while loop.
# 3. for loop → Iterates over sequences (list, tuple, string, range, etc.).
# 4. while loop → Executes as long as a condition is True.
# 5. Loops can be controlled using break, continue, and pass.
# 6. Infinite loops occur if the condition never becomes False.
# 7. Loops improve efficiency by avoiding repeated code writing.

# ======================================
# 3.3 Python For Loop
# ======================================


# 1. A for loop iterates through each element in a sequence.
# 2. Works with iterables: list, tuple, dictionary, string, set, range().
# 3. Syntax: for variable in sequence:  # block of code
# 4. range() is commonly used to generate sequences of numbers.
# 5. range(start, stop, step) → start is inclusive, stop is exclusive, step defines increment.
# 6. Nested for loops are allowed.
# 7. Non-iterable objects (like int) will raise an error.

# Example 1: Using range(stop)
# for i in range(5):  # 0 to 4
#     print(i)   
# Example 2: Using range(start, stop)
# for i in range(2, 6):  # 2 to 5
#     print(i)
# Example 3: Using range(start, stop, step)
# for i in range(1, 10, 2):  # Odd numbers from 1 to 9 1,,3,,5,,7,,9,
#     print(i)
# for i in range(5, 0, -1): # 5 ,4, 3, 2, 1 # -1 is the step value, which means the loop will decrement by 1 in each iteration.
#     print(i)

# Example 4: Nested For Loops
# for i in range(1, 4): # 1 2 3
#     for j in range(1, 3): # 1 2 
#         print(f"i={i}, j={j}") # 1,1 1,2 2,1 2,2 3,1 3,2
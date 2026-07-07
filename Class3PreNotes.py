#3.1 Python If  
# python if statements are used for decision making. It allows you to execute certain code based on a condition. 
# Example:
x = 10  
if x > 5:
    print("x is greater than 5")   

#3.1.1 Python If Else
# The if statement can be followed by an optional else statement, which executes when the condition is false.
# Example:
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#3.1.2 Python If Elif Else
# The if statement can be followed by an optional elif (else if) statement, which allows you to check multiple conditions.
# Example:
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")

# 3.1.3 Nested If Statements
# You can also nest if statements within each other to check for multiple conditions.
# Example:
x = 15
if x > 10:
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is greater than 10 but less than or equal to 20")  

# 3.1.4 Python Ternary Operator
# Python also supports a ternary operator, which allows you to write a simple if-else statement in a single line.
# Example:
x = 8
result = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(result)


# 3.1.5 Python Pass Statement
# The pass statement is used as a placeholder for future code. It allows you to create an empty block of code that does nothing.
# Example:
x = 10
if x > 5:
    pass  # This block does nothing


# 3.1.6 Python If Statement with Logical Operators
# You can use logical operators (and, or, not) to combine multiple conditions in an if statement.
# Example:
x = 7
if x > 5 and x < 10:
    print("x is between 5 and 10")

# 3.1.7 Python Match Case
# The match case statement is a new feature in Python 3.10 that allows you to perform pattern matching on values.
# Example:
x = 5
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _:
        print("x is something else")


# 3.2 Python While Loop
# The while loop is used to execute a block of code repeatedly as long as a condition is true.
# Example:
i = 0
while i < 5:
    print(i)
    i += 1


# 3.2.1 Python While Loop with Else
# The while loop can also have an optional else statement, which executes when the loop condition becomes false.
# Example:
i = 0 
while i < 5:
    print(i)
    i += 1
else:
    print("Loop ended")


# 3.2.2 Python Break Statement
# The break statement is used to exit a loop prematurely when a certain condition is met.
# Example:
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1


# 3.2.3 Python Continue Statement
# The continue statement is used to skip the current iteration of a loop and move on to the next iteration.
# Example:
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# 3.2.4 Python Nested While Loop
# You can also nest while loops within each other to create more complex looping structures.
# Example:
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1


#3.3 Python For Loop
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.
# Example:
for i in range(5):
    print(i)


#3.3.1 Python For Loop with Else
# The for loop can also have an optional else statement, which executes when the loop has completed all iterations.
# Example:
for i in range(5):
    print(i)
else:
    print("Loop completed")

#3.3.2 Python Break Statement in For Loop
# The break statement can also be used in a for loop to exit the loop prematurely when a certain condition is met.
# Example:
for i in range(10):
    if i == 5:
        break
    print(i)

#3.3.3 Python Continue Statement in For Loop
# The continue statement can also be used in a for loop to skip the current iteration and move on to the next iteration.
# Example:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#3.3.4 Python Nested For Loop
# You can also nest for loops within each other to create more complex looping structures.
# Example:
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

#3.5 Difference between Break and Continue in Python  
# The break statement exits the loop completely when a certain condition is met.
# The continue statement skips the current iteration of the loop and moves on to the next iteration when a certain condition is met.

# 3.6 Difference Between For Loop and While Loop in Python 
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.
# The while loop is used to execute a block of code repeatedly as long as a condition is true.

# 3.7 Control Statements in Python
# Control statements are used to control the flow of execution in a program. The main control statements in Python are break, continue, and pass.   


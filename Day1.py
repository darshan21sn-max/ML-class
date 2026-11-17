# Problem 1
a=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print(a[1][1][3:0:-1] + a[0][1][1::-1])
# [12, 11, 5, 4]

# Problem 2
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0:11:3])
# [1, 4, 7, 10]

# Types of Error in python:
# There are 3 main types of errors in Python:
# 1. Syntax Errors
# 2. Runtime Errors (Exceptions)
# 3. Logical Errors


# 1. Syntax Errors
# A syntax error occurs when you don't follow Python's grammar or coding rules.
#    1.Missing colons
#    2.Incorrect indentation

# 2. Runtime Errors (Exceptions)
# Runtime errors occur while the program is executing.
# Error	                        Meaning
# ZeroDivisionError	   Dividing a number by zero
# NameError	           Using an undefined variable
# TypeError	           Performing an invalid operation on data types
# ValueError	       Passing an invalid value
# IndexError	       Accessing an invalid list index
# KeyError	           Accessing a dictionary key that doesn't exist
# AttributeError	   Accessing an unavailable attribute or method
# ImportError	       Unable to import something
# ModuleNotFoundError  Required module is not found
# FileNotFoundError	   Requested file doesn't exist
# OverflowError	       A numeric operation exceeds the supported range

# 3. Logical Errors
# Logical errors occur when your code executes successfully but produces the wrong output.
# Example:
a = 10
b = 20
result = a - b
print(result)
# -10
# Expecting output is:
# 30
# Because we used subtraction (-) instead of addition (+).
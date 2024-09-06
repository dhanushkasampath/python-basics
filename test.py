print("hellow world");

# every variable in python is an object
# Python supports two types of numbers, integers and floating point numbers(decimals)


myint = 7
print(myint)

# There are 2 ways of defining floating point numbers
myNum1 = 7.5
print(myNum1)

myNum2 = float(7.5)
print(myNum2)

# Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
mystring = "Don't worry about apostrophes"
print(mystring)


# Assignments can be done on more than one variable "simultaneously" on the same line like this
# Mixing operators between numbers and strings is not supported:
a, b = 3, 4
print(a, b)
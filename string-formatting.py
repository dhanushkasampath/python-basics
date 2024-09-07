# Python uses C-style string formatting to create new, formatted strings.
# This prints out "Hello, John!"
name = "John"
print('1', "Hello, %s!" % name)

# here s is for strings. d is for digits
name = "John"
age = 23
city = "matara"
print('2', "%s is %d years old. he lives in %s " % (name, age, city))

mylist = [1,2,3]
print('3', "A list: %s" % mylist)


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print('4', format_string % data)
# What are Functions?
# Functions are a convenient way to divide your code into useful 
# blocks, allowing us to order our code, make it more readable, 
# reuse it and save some time. Also functions are a key way to define interfaces 
# so programmers can share their code.

def my_function():
    print("Hello From My Function!")

my_function()    

# Functions may also receive arguments (variables passed from the caller to the function). For example:
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_function_with_args('dhanushka', 'Hi')   

# Functions may return a value to the caller, using the keyword- 'return' 

def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(4, 6))  


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

print(build_sentence("redability"))
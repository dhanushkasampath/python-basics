# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
# Each value stored in a dictionary can be accessed using a key, which is any type of 
# object (a string, a number, a list, etc.) instead of using its index to address it.

# For example, a database of phone numbers could be stored using a dictionary like this:

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Alternatively, a dictionary can be initialized with the same values in the following notation:

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# Dictionaries can be iterated over, just like a list. 
# However, a dictionary, unlike a list, does not keep the order of the values stored in it.
# To iterate over key value pairs, use the following syntax:

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# To remove a specified index, use either one of the following notations:    
del phonebook["John"]
print(phonebook)

# or

phonebook.pop("Jack")
print(phonebook)
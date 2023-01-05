"""
Write a python script to print any number and its binary equivalent
"""

# to print binary equivalent of any number we uses a builtins method called
# "bin()" function which accepts a "integer" as an argument and returns the 
# binary representation of a specified argument in the "str" type
# prefixed with '0b' which represents binary value


int_var = int(input("Enter a number : "))

print("Binary representation of", int_var, "is", bin(int_var))
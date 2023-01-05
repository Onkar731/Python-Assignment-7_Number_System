"""
Write a python script to store an octal number 125 in a variable and print it in
binary format
"""

# to store a number in octal format it must prefixed with '0o'
# '0o' represents number is in octal format
oct_var = 0o125

# to convert octal number into binary number we uses a builtins method called
# "bin()" function which accepts a octal, hexadecimal and decimal value and 
# returns corresponding binary equivalent of the specified argument

print("Binary format of \'bin(0o125)\' is", bin(oct_var))
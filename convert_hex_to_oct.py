"""
Write a python script to store a hexadecimal number 2F in a variable and
print it in octal format
"""

# to store a hexadecimal number in a variable, prefixed it with '0x'
# '0x' represents hexadecimal format of the number
hex_var = 0x2F

# to print it in octal format we uses a builtins method called
# "oct()" function which accepts an argument in decimal, hexadecimal and binary
# format and returns the corresponding octal value as str type

print("Octal value of \'oct(0x2F)\' is", oct(hex_var))
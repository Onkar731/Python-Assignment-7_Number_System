"""
Write a python script to add two numbers 25(in Octal) and 39(in hexadecimal) and
display the result in binary format
"""

# as we know to store octal and hexadecimal value we uses '0o' and '0x' respectively
oct_var = 0o25
hex_var = 0x39

# adding octal and hexadecimal value and converting into binary equivalent
bin_var = bin(oct_var + hex_var)

# printing binary equivalent of the corresponding result
print("Binary equivalent of the result \"octal + hex\" is", bin_var)
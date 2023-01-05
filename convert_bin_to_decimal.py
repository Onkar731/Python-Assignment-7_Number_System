"""
Write a python script to store binary number 1100101 
in a varaible and print it in decimal format
"""

# storing binary number 1100101 into a variable
# to store binary number in a variable, binary number must be prefixed with '0b'
# '0b' represents the given number is in binary format
bin_var = 0b1100101

# to convert binary number into decimal number there is not a builtins method
# instead we uses the print method to print decimal number in python
# by default numbers used in decimal number system in python
# call print method and pass binary format it will print decimal equivalent of that binary

print("Decimal value of \'binary(0b1100101)\' is", bin_var)
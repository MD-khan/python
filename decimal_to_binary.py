#!/usr/bin/env python3

# Find the highest decimal value that is less than or equal to the given decimal
# Set the bit in the 128 column to 1.
# Subtract 128 from given decimal to get a remainder
# Find the highest decimal value that is less than or equal to the reminder.
# Set the bit in the next column to 1
# Subtract 64 from the reminder.
# Repeat the preceding pattern for each remainder value until the remainder is 0.

def decimal_to_binary( number ):
    decimal_values = [128, 64, 32, 16, 8, 4, 2, 1]
    binary_digits = []
    #input_d=214
    for decimal in decimal_values:
        if decimal <= number:
            binary_digits.append(1)
            number = number - decimal
        else:
            binary_digits.append(0)
    
    # format the binary
    separator =  ""
    return separator.join(map(str, binary_digits))


  print(decimal_to_binary(1))
  print(decimal_to_binary(192))
  print(decimal_to_binary(209))
  

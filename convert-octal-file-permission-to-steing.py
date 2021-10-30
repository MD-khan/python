def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result +="-"
    return result
 
# Example of use
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(642)) # Should be rw-r---w-
print(octal_to_string(751)) # Should be rw-r-x--x
print(octal_to_string(400)) # Should be r--------

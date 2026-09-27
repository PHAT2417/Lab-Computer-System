# ------------------------------------------------------------
# Name: Fernanda Lugo
# Lab: Simplified Floating-Point Representation
# Question 1
#
# Description:
# This program converts a decimal floating-point number into
# a simplified floating-point representation using:
# 1 sign bit, 5 exponent bits with Excess-15,
# and 8 significand bits.
# ------------------------------------------------------------

def convert_float(number):

    # Determine sign bit
    if number < 0:
        sign_bit = "1"
        number = abs(number)
    else:
        sign_bit = "0"

    # Handle zero
    if number == 0:
        return "0 00000 00000000"

    # Normalize the number into the form 1.xxxxx × 2^exponent
    exponent = 0

    while number >= 2:
        number = number / 2
        exponent += 1

    while number < 1:
        number = number * 2
        exponent -= 1

    # Add Excess-15 bias to exponent
    biased_exponent = exponent + 15

    # Make sure exponent fits in 5 bits
    if biased_exponent < 0 or biased_exponent > 31:
        return "ERROR: Number is out of range."

    # Convert exponent to 5-bit binary
    exponent_bits = format(biased_exponent, "05b")

    # Remove the leading 1 from normalized number
    fraction = number - 1

    # Create 8 significand bits
    significand_bits = ""

    for i in range(8):
        fraction = fraction * 2

        if fraction >= 1:
            significand_bits += "1"
            fraction -= 1
        else:
            significand_bits += "0"

    # Combine sign, exponent, and significand
    return sign_bit + " " + exponent_bits + " " + significand_bits


# Ask the user for input
user_input = input("Enter a floating-point number: ")

# Check for illegal input
try:
    number = float(user_input)

    result = convert_float(number)

    print("Simplified floating-point representation:")
    print(result)

except ValueError:
    print("ERROR: Illegal input. Please enter a valid number.")

     

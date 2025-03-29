import re
from helpers import (
    binary_re,
    octal_re,
    hex_int_re,
    hex_float_re,
    decimal_re,
    decimal_lead_dot_re
)
# text = '123 "456" -7.8 \'9.10\' 42 "test" 100 0b001001'

# # Combined regex: Skips quoted strings, matches numbers outside them
# combined_regex = r'"[^"]*"|\'[^\']*\'|(-?\d+\.?\d*)'

# # Extract non-quoted numbers (filter out empty matches)
# numbers = [num for num in re.findall(combined_regex, text) if num]


text = '\'123\' 0b1010 "456" 0o755 0xFFFF -7.8 1.23e+10 0x1.2p3'

# Improved regex: Non-capturing groups for quotes, single capture for numbers
combined_regex = r'''
    (?:"[^"]*"|'[^']*')  # Skip quoted strings (non-capturing)
    |
    (                     # Capture JS numbers:
        -?                # Optional negative sign
        (?:
            0[bB][01]+(_[01]+)*        # Binary (0b1010)
            |0[oO][0-7]+(_[0-7]+)*    # Octal (0o755)
            |0[xX][0-9a-fA-F]+(_[0-9a-fA-F]+)*            # Hex integer (0xFFFF)
            |0[xX][0-9a-fA-F]+\.[0-9a-fA-F]*(p[+-]?\d+)?  # Hex float (0x1.2p3)
            |\d+\.?\d*(?:[eE][+-]?\d+)?                   # Decimal (123, 1.23e+10)
            |\.\d+(?:[eE][+-]?\d+)?                       # Decimal (.5)
        )
        \b               # Word boundary
    )
'''

# Extract numbers (filter out None/empty matches)
numbers = [match[0] for match in re.findall(
    combined_regex, text, re.VERBOSE) if match[0]]

# print(numbers)
# Output: ['123', '0b1010', '0o755', '0xFFFF', '-7.8', '1.23e+10', '0x1.2p3']
number_to_test = '123'
is_decimal_number = bool(re.fullmatch(decimal_re, number_to_test))
print(f"is_decimal_number: {is_decimal_number}")

number_to_test = '0xF12312'
is_hex_number = bool(re.fullmatch(hex_int_re, number_to_test))
print(f"is_hex_number: {is_hex_number}")


#  Function to indentify radix and parse any number to decimal
#  - get radix (aka number type. Ex: decimal, binary -> 10, 2) using regex
#  - Create a function that converts a number by a radix
#    - for example: (15).toString(16) // output: 'f'


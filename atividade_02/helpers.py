# Binary numbers (0b1010, 0B1100)
binary_re = r'0[bB][01]+(_[01]+)*'

# Octal numbers (0o755, 0O644)
octal_re = r'0[oO][0-7]+(_[0-7]+)*'

# Hexadecimal integers (0xFFFF, 0Xa1b2)
hex_int_re = r'0[xX][0-9a-fA-F]+(_[0-9a-fA-F]+)*'

# Hexadecimal floats (0x1.2p3, 0X1.ABp-10)
hex_float_re = r'0[xX][0-9a-fA-F]+\.[0-9a-fA-F]*(p[+-]?\d+)?'

# Decimal numbers (123, -45.67, 1.23e+10)
decimal_re = r'[-+]?\d+\.?\d*(?:[eE][+-]?\d+)?'

# Decimal numbers starting with . (.5, .67e-10)
decimal_lead_dot_re = r'[-+]?\.\d+(?:[eE][+-]?\d+)?'

number_core_re = fr'''
    -?  # Optional negative sign
    (?:
        {binary_re}
        |{octal_re}
        |{hex_int_re}
        |{hex_float_re}
        |{decimal_re}
        |{decimal_lead_dot_re}
    )
    \b  # Word boundary
'''


non_quoted_js_numbers_regex = fr'''
    (?:"[^"]*"|\'[^\']*\')  # Skip quoted strings
    |
    (?:^|(?<=[\s(,;=+*/%-]))  # Start or after delimiters
    ({number_core_re})       # Capture numbers
'''


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

def float_equal(a: str, b: str, precision: int = 10) -> bool:
    """Compare two float strings with limited precision"""
    if a == b:
        return True
    
    a_int, _, a_frac = a.partition('.')
    b_int, _, b_frac = b.partition('.')
    
    if a_int != b_int:
        return False
    
    return a_frac[:precision] == b_frac[:precision]


def digit_to_char(d: int) -> str:
    """Convert digit (0-35) to corresponding character (0-9 then a-z)"""
    if d < 10:
        return str(d)
    return chr(ord('a') + d - 10)


def format_digits(number, min_digits=1):
    num_str = str(number)

    sign = ''
    if num_str.startswith('-'):
        sign = '-'
        num_str = num_str[1:]
    elif num_str.startswith('+'):
        sign = '+'
        num_str = num_str[1:]

    return sign + num_str.zfill(max(min_digits, len(num_str)))

import re
from helpers import (
    binary_re,
    octal_re,
    hex_int_re,
    hex_float_re,
    decimal_re,
    decimal_lead_dot_re
)

def get_radix(number_str: str) -> int:
    # Add start/end anchors to each pattern for strict validation
    patterns = [
        (2, fr'^{binary_re}$'),      # Binary
        (8, fr'^{octal_re}$'),       # Octal
        (16, fr'^{hex_int_re}$'),    # Hex integer
        (16, fr'^{hex_float_re}$'),  # Hex float
        (10, fr'^{decimal_re}$'),    # Decimal
        (10, fr'^{decimal_lead_dot_re}$')  # Decimal with leading dot
    ]
    
    for radix, pattern in patterns:
        if re.fullmatch(pattern, number_str, re.VERBOSE):
            return radix
    
    return None  # No valid format found
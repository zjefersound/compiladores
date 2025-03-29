import re
from typing import Union
from helpers import (
    binary_re,
    octal_re,
    hex_int_re,
    hex_float_re,
    decimal_re,
    decimal_lead_dot_re
)

def parse_number_str_to_decimal(number_str: str) -> Union[int, float]:
    cleaned = re.sub(r'_', '', number_str.strip().lower())
    
    try:
        # Binary
        if re.fullmatch(binary_re, cleaned):
            return int(cleaned[2:], 2)
        
        # Octal
        elif re.fullmatch(octal_re, cleaned):
            return int(cleaned[2:], 8)
        
        # Hexadecimal integer
        elif re.fullmatch(hex_int_re, cleaned):
            return int(cleaned[2:], 16)
        
        # Hexadecimal float
        elif re.fullmatch(hex_float_re, cleaned):
            return float.fromhex(cleaned)
        
        # Decimal (regular or scientific notation)
        elif re.fullmatch(decimal_re, cleaned) or \
             re.fullmatch(decimal_lead_dot_re, cleaned):
            return float(cleaned) if '.' in cleaned or 'e' in cleaned else int(cleaned)
        
        raise ValueError(f"Invalid number format: {number_str}")
    
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Failed to parse {number_str}: {str(e)}")

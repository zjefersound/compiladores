import re
import math
from typing import Union
from helpers import (
    binary_re,
    octal_re,
    hex_int_re,
    hex_float_re,
    decimal_re,
    decimal_lead_dot_re,
    float_equal,
    digit_to_char
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

def number_to_radix(number: Union[int, float], radix: int = 10, max_fraction_digits: int = 20) -> str:
    """
    Convert a number to a string representation in the specified radix (base).
    Mimics JavaScript's Number.prototype.toString(radix) behavior.

    Args:
        number: The number to convert (int or float)
        radix: The target base (2-36, default 10)
        max_fraction_digits: Maximum fractional digits for non-integers (default 20)

    Returns:
        str: The number represented in the specified radix

    Raises:
        ValueError: If radix is not between 2 and 36
    """
    if not 2 <= radix <= 36:
        raise ValueError("radix must be between 2 and 36")

    # Handle special cases
    if number == 0:
        return "0"
    if math.isnan(number):
        return "NaN"
    if number == math.inf:
        return "Infinity"
    if number == -math.inf:
        return "-Infinity"

    sign = "-" if number < 0 else ""
    number = abs(number)

    # Split into integer and fractional parts
    integer_part = int(number)
    fractional_part = number - integer_part

    # Convert integer part
    if integer_part == 0:
        int_str = "0"
    else:
        int_str = ""
        while integer_part > 0:
            remainder = integer_part % radix
            int_str = digit_to_char(remainder) + int_str
            integer_part = integer_part // radix

    # Convert fractional part if it exists
    frac_str = ""
    if fractional_part > 0 and radix != 10:
        frac_str = "."
        for _ in range(max_fraction_digits):
            if fractional_part == 0:
                break
            fractional_part *= radix
            digit = int(fractional_part)
            frac_str += digit_to_char(digit)
            fractional_part -= digit

    # Combine parts
    return sign + int_str + frac_str


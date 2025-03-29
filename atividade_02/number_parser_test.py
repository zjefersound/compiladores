from number_parser import parse_number_str_to_decimal, number_to_radix
import math
from helpers import float_equal

tests = [
    ("0b1010", 10),
    ("0b1010z", 10),
    ("0o755", 493),
    ("0o75599", 493),
    ("0xFF", 255),
    ("0x1.2p3", 9.0),
    ("123", 123),
    ("-45.67", -45.67),
    ("1.23e+10", 12300000000.0),
    (".5", 0.5),
    ("1_000_000", 1000000),
    ("0x1.ffffp1023", float.fromhex('0x1.ffffp1023'))
]
    
for num_str, expected in tests:
    try:
        result = parse_number_str_to_decimal(num_str)
        assert result == expected, f"{num_str}: {result} != {expected}"
        print(f"✓ {num_str:12} → {result}")
    except ValueError as e:
        print(f"✗ {num_str}: {e}")

tests = [
    # (number, radix, expected)
    (10, 2, "1010"),
    (255, 16, "ff"),
    (10, 8, "12"),
    (3.5, 2, "11.1"),
    (-10, 16, "-a"),
    (0.1, 2, ("0.0001100110011001101", 15)),  # Tuple with expected and precision
    (1/3, 3, "0.1"),
    (10.5, 8, "12.4"),
    (0, 16, "0"),
    (float('nan'), 16, "NaN"),
    (float('inf'), 16, "Infinity"),
    (float('-inf'), 16, "-Infinity"),
    # Edge cases
    (123456789, 36, "21i3v9"),
    (0.5, 2, "0.1"),
]

print("Running number_to_radix tests...\n" + "="*50)

for number, radix, expected in tests:
    try:
        result = number_to_radix(number, radix)
        
        # Handle special cases
        if math.isnan(number):
            assert result == expected, f"NaN test failed: got {result}"
            print(f"✓ {str(number):>5}, radix {radix:2} → {result}")
            continue
            
        # Handle flexible float comparison
        if isinstance(expected, tuple):
            expected_str, precision = expected
            if float_equal(result, expected_str, precision):
                print(f"✓ {str(number):>5}, radix {radix:2} → {result} (Approx match to {expected_str})")
            else:
                print(f"✗ {str(number):>5}, radix {radix:2} → {result} (Expected ~{expected_str})")
        else:
            assert result == expected, f"{number} (base {radix}): {result} != {expected}"
            print(f"✓ {str(number):>5}, radix {radix:2} → {result}")
            
    except AssertionError as e:
        print(f"✗ {str(number):>5}, radix {radix:2} → {result} (Expected: {expected})")
    except Exception as e:
        print(f"✗ {str(number):>5}, radix {radix:2} → Error: {str(e)}")

print("="*50 + "\nTests completed")
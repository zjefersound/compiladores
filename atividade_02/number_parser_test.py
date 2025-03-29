from number_parser import parse_number_str_to_decimal

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
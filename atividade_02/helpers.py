non_quoted_js_numbers_regex = r'''
    (?:"[^"]*"|'[^']*')  # Skip quoted strings (non-capturing)
    |
    (?:^|(?<=[\s(,;=+*/%-]))  # Start or after whitespace/delimiters
    (                        # Capture JS numbers:
        -?                   # Optional negative sign
        (?:
            0[bB][01]+(_[01]+)*        # Binary (0b1010)
            |0[oO][0-7]+(_[0-7]+)*     # Octal (0o755)
            |0[xX][0-9a-fA-F]+(_[0-9a-fA-F]+)*            # Hex integer (0xFFFF)
            |0[xX][0-9a-fA-F]+\.[0-9a-fA-F]*(p[+-]?\d+)?  # Hex float (0x1.2p3)
            |\d+\.?\d*(?:[eE][+-]?\d+)?                   # Decimal (123, 1.23e+10)
            |\.\d+(?:[eE][+-]?\d+)?                      # Decimal (.5)
        )
        \b                  # Word boundary
    )
'''
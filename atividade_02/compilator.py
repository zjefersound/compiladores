import os
import re
from collections import defaultdict
from helpers import non_quoted_js_numbers_regex
from number_detector import get_radix
from number_parser import parse_number_str_to_decimal, number_to_radix

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    return None


def extract_ascii_characters(file_path):
    lines = read_file(file_path)
    if lines is None:
        return []
    content = "".join(lines)
    return [char for char in content if ord(char) < 128]


def filter_unwanted_characters(char_list, unwanted_chars):
    return [char for char in char_list if char not in unwanted_chars]


def get_numbered_lines(file_path):
    lines = read_file(file_path)
    if lines is None:
        return []
    max_digits = len(str(len(lines)))
    return [f"{str(i+1).rjust(max_digits)} | {line.rstrip()}" for i, line in enumerate(lines)]


def extract_word_occurrences(file_path):
    lines = read_file(file_path)
    if lines is None:
        return {}
    word_map = defaultdict(set)
    for i, line in enumerate(lines, start=1):
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            word_map[word].add(i)
    return dict(sorted(word_map.items()))


def extract_number_occurrences(file_path):
    # Creates a structure of dictionaries to store the original number and
    # its converted value to decimal. Also keeps important infos as radix and lines
    # { '1000': { radix: 10, decimal_value: 1000, lines: {10} } }
    # { '0xf': { radix: 16, decimal_value: 15, lines: {8} } }
    lines = read_file(file_path)
    if lines is None:
        return {}
    number_map = {}
    for i, line in enumerate(lines, start=1):
        numbers = [match[0] for match in re.findall(
            non_quoted_js_numbers_regex, line.lower(), re.VERBOSE) if match[0]]

        for number in numbers:
            number_map[number] = {}
            number_map[number]["radix"] = get_radix(number)
            number_map[number]["decimal_value"] = parse_number_str_to_decimal(number)
            number_map[number]["lines"] = []
            number_map[number]["lines"].append(i)

    return dict(number_map.items())


# Vai para uma camada de input
file_name = "our_strange_code.txt"
file_path = os.path.join(os.path.dirname(__file__), file_name)

# Códigos que poderá ser abstraído em uma camada de settings do compilador
unwanted_chars = [' ', '\t', '\n', '\r', '\f', '\v', '🖕🏻']

# Código que será parte da implementação principal

# Exercício 1
ascii_characters = extract_ascii_characters(file_path)
# Exercício 2
filtered_characters = filter_unwanted_characters(ascii_characters, unwanted_chars)
if filtered_characters:
    print("Caracteres ASCII extraídos:")
    print(filtered_characters)


# Exercício 3
numbered_lines = get_numbered_lines(file_path)
if numbered_lines:
    print("\nTexto com numeração de linhas:")
    for line in numbered_lines:
        print(line)


# Exercício 4
word_occurrences = extract_word_occurrences(file_path)
if word_occurrences:
    print("\nTabela de referências cruzadas:")
    for word, lines in word_occurrences.items():
        print(f"{word}: {', '.join(map(str, sorted(lines)))}")

# Exercício 5
number_occurrences = extract_number_occurrences(file_path)
print(number_occurrences)

# Convertendo todos os números encontrados para binário:
binary_conversions = {}
for num_str, data in number_occurrences.items():
    decimal_value = data['decimal_value']
    binary_value = number_to_radix(decimal_value, 2)
    binary_conversions[num_str] = {
        'original': num_str,
        'decimal': decimal_value,
        'binary': binary_value,
        'lines': data['lines']
    }

print("Decimal to Binary Conversions:")
print("=" * 40)
for original, conversion in binary_conversions.items():
    print(f"Original: {original:>6}")
    print(f"Decimal: {conversion['decimal']:>7}")
    print(f"Binario:  {conversion['binary']:>7}")
    print("-" * 40)
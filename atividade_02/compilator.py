import os
import re
from collections import defaultdict


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
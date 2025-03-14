import os


def extract_ascii_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            ascii_chars = [char for char in content if ord(char) < 128]
            return ascii_chars
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def filter_unwanted_characters(char_list, unwanted_chars):
    return [char for char in char_list if char not in unwanted_chars]

def get_numbered_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            max_digits = len(str(len(lines)))
            return [f"{str(i+1).rjust(max_digits)} | {line.rstrip()}" for i, line in enumerate(lines)]
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Vai para uma camada de input
file_name = "our_strange_code.txt"
file_path = os.path.join(os.path.dirname(__file__), file_name)

# Códigos que poderá ser abstraído em uma camada de settings do compilador
unwanted_chars = [' ', '\t', '\n', '\r', '\f', '\v', '🖕🏻']

# Código que será parte da implementação principal
ascii_characters = extract_ascii_characters(file_path)
filtered_characters = filter_unwanted_characters(ascii_characters, unwanted_chars)

if filtered_characters:
    print("Caracteres ASCII extraídos:")
    print(filtered_characters)


numbered_lines = get_numbered_lines(file_path)
if numbered_lines:
    print("\nTexto com numeração de linhas:")
    for line in numbered_lines:
        print(line)
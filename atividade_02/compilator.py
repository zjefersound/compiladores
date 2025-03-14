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

file_name = "ex_01_file.txt"
file_path = os.path.join(os.path.dirname(__file__), file_name)
ascii_characters = extract_ascii_characters(file_path)

if ascii_characters:
    print("Caracteres ASCII extraídos:")
    print(ascii_characters)

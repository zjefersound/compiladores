from fixed_content_table import FixedContentTable

def setup_reserved_words_table():
    reserved_words = [
        'if', 'else', 'while', 'for', 'return',
        'break', 'continue', 'class', 'def', 'import',
        'try', 'except', 'finally', 'raise', 'with',
        'lambda', 'yield', 'async', 'await', 'nonlocal',
        'global', 'True', 'False', 'None', 'and', 'or', 'not'
    ]
    return FixedContentTable(reserved_words)


def table_search():
    table = setup_reserved_words_table()

    print("Contains 'lambda':", table.contains('lambda'))
    print("Contains 'lambda no c#':", table.contains('lambda'))
    print("Contains 'IF':", table.contains('IF'))
    print("Case-insensitive contains 'IF':", table.contains_case_insensitive('IF'))
    
    print("Prefix 'wh':", table.search_prefix('wh'))
    print("Case-insensitive prefix 'WH':", table.search_prefix_case_insensitive('WH'))
    
    print("All reserved words:", table.get_all_items())


if __name__ == "__main__":
    table_search()
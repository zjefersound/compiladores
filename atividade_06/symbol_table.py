class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, attributes=None):
        if name in self.symbols:
            return False
        self.symbols[name] = attributes if attributes is not None else {}
        return True
    
    def remove_symbol(self, name):
        if name in self.symbols:
            del self.symbols[name]
            return True
        return False
    
    def find_symbol(self, name):
        return self.symbols.get(name, None)
    
    def add_attribute(self, name, key, value):
        if name in self.symbols:
            self.symbols[name][key] = value
            return True
        return False
    
    def remove_attribute(self, name, key):
        if name in self.symbols and key in self.symbols[name]:
            del self.symbols[name][key]
            return True
        return False
    
    def get_sorted_symbols(self):
        return sorted(self.symbols.keys())
    
    def get_all_symbols(self):
        return self.symbols.copy()
    
    def export_to_file(self, filename):
        try:
            with open(filename, 'w') as f:
                for name in sorted(self.symbols.keys()):
                    f.write(f"{name}: {self.symbols[name]}\n")
            return True
        except (IOError, OSError):
            return False
    
    def import_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                temp_symbols = {}
                for line in f:
                    if ':' in line:
                        name, attributes = line.split(':', 1)
                        name = name.strip()
                        try:
                            attributes = eval(attributes.strip())
                            temp_symbols[name] = attributes
                        except:
                            continue
                self.symbols = temp_symbols
            return True
        except (FileNotFoundError, IOError, OSError):
            return False
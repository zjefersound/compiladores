from symbol_table import SymbolTable

def interactive_menu():
    table = SymbolTable()
    
    while True:
        print("\n=== SYMBOL TABLE MANAGER ===")
        print("1. Add symbol")
        print("2. Remove symbol")
        print("3. Find symbol")
        print("4. Add attribute")
        print("5. Remove attribute")
        print("6. List all symbols")
        print("7. Export to file")
        print("8. Import from file")
        print("0. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            name = input("Enter symbol name: ").strip()
            if table.add_symbol(name):
                print(f"Symbol '{name}' added successfully.")
            else:
                print(f"Symbol '{name}' already exists.")
        
        elif choice == '2':
            name = input("Enter symbol name to remove: ").strip()
            if table.remove_symbol(name):
                print(f"Symbol '{name}' removed successfully.")
            else:
                print(f"Symbol '{name}' not found.")
        
        elif choice == '3':
            name = input("Enter symbol name to find: ").strip()
            result = table.find_symbol(name)
            if result is not None:
                print(f"Symbol '{name}' found with attributes: {result}")
            else:
                print(f"Symbol '{name}' not found.")
        
        elif choice == '4':
            name = input("Enter symbol name: ").strip()
            key = input("Enter attribute name: ").strip()
            value = input("Enter attribute value: ").strip()
            if table.add_attribute(name, key, value):
                print(f"Attribute '{key}' added to '{name}' successfully.")
            else:
                print(f"Failed to add attribute. Symbol '{name}' not found.")
        
        elif choice == '5':
            name = input("Enter symbol name: ").strip()
            key = input("Enter attribute name to remove: ").strip()
            if table.remove_attribute(name, key):
                print(f"Attribute '{key}' removed from '{name}' successfully.")
            else:
                print(f"Failed to remove attribute. Symbol or attribute not found.")
        
        elif choice == '6':
            symbols = table.get_sorted_symbols()
            if symbols:
                print("\nSYMBOLS (alphabetical order):")
                for name in symbols:
                    attributes = table.find_symbol(name)
                    print(f"{name}: {attributes}")
            else:
                print("Symbol table is empty.")
        
        elif choice == '7':
            filename = input("Enter filename for export: ").strip()
            if table.export_to_file(filename):
                print(f"Symbol table exported to '{filename}' successfully.")
            else:
                print(f"Failed to export to '{filename}'.")
        
        elif choice == '8':
            filename = input("Enter filename to import: ").strip()
            if table.import_from_file(filename):
                print(f"Symbol table imported from '{filename}' successfully.")
            else:
                print(f"Failed to import from '{filename}'.")
        
        elif choice == '0':
            print("Exiting program.")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    interactive_menu()
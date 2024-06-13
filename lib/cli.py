from helpers import (
    exit_program,
    list_items,
    find_item_by_id,
    find_item_by_name,
    create_item,
    update_item,
    delete_item,
    list_categories,
    create_category,
    delete_category,
    filter_items_by_category_or_supplier,
    list_suppliers,
    create_supplier,
    update_supplier,
    delete_supplier,
)

def main_menu():
    print("""
    Main Menu:
    1. Items
    2. Categories
    3. Suppliers
    4. Exit
    """)

def items_menu():
    print("""
    Items Menu:
    1. List Items
    2. Find Item by Name
    3. Find Item by ID
    4. Add Item
    5. Update Item
    6. Delete Item
    7. Filter Items by Category or Supplier
    8. Back to Main Menu
    """)

def categories_menu():
    print("""
    Categories Menu:
    1. List Categories
    2. Add Category
    3. Delete Category
    4. Back to Main Menu
    """)

def suppliers_menu():
    print("""
    Suppliers Menu:
    1. List Suppliers
    2. Add Supplier
    3. Update Supplier
    4. Delete Supplier
    5. Back to Main Menu
    """)

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "1":
            items_submenu()
        elif choice == "2":
            categories_submenu()
        elif choice == "3":
            suppliers_submenu()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")

def items_submenu():
    while True:
        items_menu()
        choice = input("> ")
        if choice == "1":
            list_items()
        elif choice == "2":
            find_item_by_name()
        elif choice == "3":
            find_item_by_id()
        elif choice == "4":
            create_item()
        elif choice == "5":
            update_item()
        elif choice == "6":
            delete_item()
        elif choice == "7":
            filter_items_by_category_or_supplier()
        elif choice == "8":
            break
        else:
            print("Invalid choice")

def categories_submenu():
    while True:
        categories_menu()
        choice = input("> ")
        if choice == "1":
            list_categories()
        elif choice == "2":
            create_category()
        elif choice == "3":
            delete_category()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def suppliers_submenu():
    while True:
        suppliers_menu()
        choice = input("> ")
        if choice == "1":
            list_suppliers()
        elif choice == "2":
            create_supplier()
        elif choice == "3":
            update_supplier()
        elif choice == "4":
            delete_supplier()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

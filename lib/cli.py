from helpers import (
    exit_program,
    list_items,
    find_item_by_id,
    create_item,
    update_item,
    delete_item,
    list_categories,
    create_category,
    filter_items_by_name,
    filter_items_by_category_or_supplier
)

def menu():
    print("""
    1. List Items
    2. Find Item by Name
    3. Find Item by ID
    4. Create Item
    5. Update Item
    6. Delete Item
    7. List Categories
    8. Create Category
    9.Filter
    10. Exit
    """)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_items()
        elif choice == "2":
            filter_items_by_name()
        elif choice == "3":
            find_item_by_id()
        elif choice == "4":
            create_item()
        elif choice == "5":
            update_item()
        elif choice == "6":
            delete_item()
        elif choice == "10":
            exit_program()
        elif choice == "7":
            list_categories()
        elif choice == "8":
            create_category()
        elif choice == "9":
            filter_items_by_category_or_supplier()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

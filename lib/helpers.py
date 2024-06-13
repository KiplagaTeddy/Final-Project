from models.item import Item
from models.category import Category
from models.supplier import Supplier

def list_items():
    items = Item.get_all()
    for item in items:
        print(item)

def exit_program():
    print("Exiting program")
    exit()

def find_item_by_id():
    id_ = input("Enter the item's id: ")
    item = Item.find_by_id(id_)
    print(item) if item else print(f'Item {id_} not found')

def create_item():
    name = input("Enter the item's name: ")
    quantity = int(input("Enter the item's quantity: "))
    price = float(input("Enter the item's price: "))
    category_id = int(input("Enter the item's category id: "))
    supplier_id = int(input("Enter the item's supplier id: "))
    try:
        item = Item.create(name, quantity, price, category_id, supplier_id)
        print(f'Success: {item}')
    except Exception as exc:
        print("Error creating item: ", exc)

def create_category():
    name = input("Enter the category name: ")
    description = input("Enter the category description: ")
    try:
        category = Category.create(name, description)
        print(f'Success: Category {category.name} created')
    except Exception as exc:
        print("Error creating category: ", exc)

def list_categories():
    categories = Category.get_all()
    print("Categories:")
    for category in categories:
        print(f"- {category.name}: {category.description}")

def update_item():
    id_ = input("Enter the item's id: ")
    if item := Item.find_by_id(id_):
        try:
            name = input("Enter the item's new name: ")
            item.name = name
            quantity = int(input("Enter the item's new quantity: "))
            item.quantity = quantity
            price = float(input("Enter the item's new price: "))
            item.price = price
            category_id = int(input("Enter the item's new category id: "))
            item.category_id = category_id
            supplier_id = int(input("Enter the item's new supplier id: "))
            item.supplier_id = supplier_id
            item.update()
            print(f'Success: {item}')
        except Exception as exc:
            print("Error updating item: ", exc)
    else:
        print(f'Item {id_} not found')

def filter_items_by_name():
    keyword = input("Enter item name: ")
    items = Item.find_by_name(keyword)
    if items:
        for item in items:
            print(f"- {item.name}: Quantity - {item.quantity}, Price - ${item.price}")
    else:
        print("No items found matching the keyword.")

def filter_items_by_category_or_supplier():
    choice = input("Filter by (C)ategory or (S)upplier: ").lower()
    if choice == 'c':
        filter_items_by_category()
    elif choice == 's':
        filter_items_by_supplier()
    else:
        print("Invalid choice")

def filter_items_by_category():
    categories = Category.get_all()
    print("Available Categories:")
    for category in categories:
        print(f"{category.id}. {category.name}")

    category_input = input("Enter the ID or name of the category to filter by: ")
    category = Category.find_by_id(category_input) or Category.find_by_name(category_input)
    if category:
        items = Item.get_items_by_category_id(category.id)
        if items:
            print(f"Items in Category '{category.name}':")
            for item in items:
                print(f"- {item.name}: Quantity - {item.quantity}, Price - ${item.price}")
        else:
            print(f"No items found in Category '{category.name}'.")
    else:
        print("Invalid category ID or name.")

def filter_items_by_supplier():
    suppliers = Supplier.get_all()
    print("Available Suppliers:")
    for supplier in suppliers:
        print(f"{supplier.id}. {supplier.name}")

    supplier_input = input("Enter the ID or name of the supplier to filter by: ")
    supplier = Supplier.find_by_id(supplier_input) or Supplier.find_by_name(supplier_input)
    if supplier:
        items = Item.get_items_by_supplier_id(supplier.id)
        if items:
            print(f"Items from Supplier '{supplier.name}':")
            for item in items:
                print(f"- {item.name}: Quantity - {item.quantity}, Price - ${item.price}")
        else:
            print(f"No items found from Supplier '{supplier.name}'.")
    else:
        print("Invalid supplier ID or name.")


def delete_item():
    id_ = input("Enter the item's id: ")
    if item := Item.find_by_id(id_):
        Item.delete(item.id)
        print(f'Item {id_} deleted')
    else:
        print(f'Item {id_} not found')



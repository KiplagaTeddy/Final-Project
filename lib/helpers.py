from models.item import Item
from models.category import Category
from models.supplier import Supplier

def list_items():
    items = Item.get_all()
    if items:
        for item in items:
            if item:
                print(item)
            else:
                print("Invalid item reference found and skipped.")

def exit_program():
    print("Exiting program")
    exit()

def find_item_by_id():
    id_ = input("Enter the item's id: ")
    item = Item.find_by_id(id_)
    print(item) if item else print(f'Item {id_} not found')

def find_item_by_name():
    name = input("Enter the item's name: ")
    items = Item.find_by_name(name)
    if items:
        for item in items:
            print(f"- {item.name}: Quantity - {item.quantity}, Price - ${item.price}")
    else:
        print("No items found matching the keyword.")

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
            print("Oops! Error updating item: ", exc)
    else:
        print(f'Item {id_} not found')

def delete_item():
    id_ = input("Enter the item's id: ")
    if item := Item.find_by_id(id_):
        Item.delete(item.id)
        print(f'Item {id_} deleted')
    else:
        print(f'Item {id_} not found')

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

def list_categories():
    categories = Category.get_all()
    print("Categories:")
    for category in categories:
        print(f"- {category.name}: {category.description}")

def create_category():
    name = input("Enter the category name: ")
    description = input("Enter the category description: ")
    try:
        category = Category.create(name, description)
        print(f'Success: Category {category.name} created')
    except Exception as exc:
        print("Error creating category: ", exc)

def delete_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        Category.delete(category.id)
        print(f'Category {id_} deleted')
    else:
        print(f'Category {id_} not found')

def list_suppliers():
    suppliers = Supplier.get_all()
    print("Suppliers:")
    for supplier in suppliers:
        print(f"- {supplier.name}")



def create_supplier():
    name = input("Enter the supplier name: ")
    contact = input("Enter the supplier contact: ")
    address = input("Enter the supplier address: ")
    try:
        supplier = Supplier.create(name, contact, address)
        print(f'Success: Supplier {supplier.name} created')
    except Exception as exc:
        print("Error creating supplier: ", exc)



def update_supplier():
    id_ = input("Enter the supplier's id: ")
    if supplier := Supplier.find_by_id(id_):
        try:
            name = input("Enter the supplier's new name: ")
            supplier.name = name
            contact = input("Enter the supplier's new contact: ")
            supplier.contact = contact
            address = input("Enter the supplier's new address: ")
            supplier.address = address
            supplier.update()
            print(f'Success: {supplier}')
        except Exception as exc:
            print("Error updating supplier: ", exc)
    else:
        print(f'Supplier {id_} not found')


def delete_supplier():
    id_ = input("Enter the supplier's id: ")
    if supplier := Supplier.find_by_id(id_):
        Supplier.delete(supplier.id)
        print(f'Supplier {id_} deleted')
    else:
        print(f'Supplier {id_} not found')

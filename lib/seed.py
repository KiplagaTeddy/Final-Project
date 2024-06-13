#!/usr/bin/env python3
from models.__init__ import CONN ,CURSOR
from models.category import Category
from models.supplier import Supplier
from models.item import Item

def seed_database():
    # Drop existing tables
    Item.drop_table()
    Category.drop_table()
    Supplier.drop_table()

    # Create new tables
    Category.create_table()
    Supplier.create_table()
    Item.create_table()

    # Create seed data for Category and Supplier
    electronics = Category.create("Electronics", "All kinds of electronics")
    groceries = Category.create("Groceries", "Daily grocery items")
    
    supplier1 = Supplier.create("Supplier 1", "Address 1", "1234567890")
    supplier2 = Supplier.create("Supplier 2", "Address 2", "0987654321")
    
    # Create seed data for Items
    Item.create("Laptop", 10, 999.99, electronics.id, supplier1.id)
    Item.create("Smartphone", 20, 599.99, electronics.id, supplier1.id)
    Item.create("Apples", 50, 0.99, groceries.id, supplier2.id)
    Item.create("Bananas", 30, 0.69, groceries.id, supplier2.id)

seed_database()
print("Seeded database")

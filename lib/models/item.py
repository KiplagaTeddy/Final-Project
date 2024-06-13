from models.__init__ import CURSOR, CONN
from models.category import Category
from models.supplier import Supplier

class Item:
    all = {}

    def __init__(self, name, quantity, price, category_id, supplier_id, id=None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category_id = category_id
        self.supplier_id = supplier_id

    def __repr__(self):
        return f"{self.id}: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Category ID: {self.category_id}, Supplier ID: {self.supplier_id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a non-negative integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = price
        else:
            raise ValueError("Price must be a non-negative number")

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int) and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError("Category ID must reference a valid Category")

    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        if isinstance(supplier_id, int) and Supplier.find_by_id(supplier_id):
            self._supplier_id = supplier_id
        else:
            raise ValueError("Supplier ID must reference a valid Supplier")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT,
                quantity INTEGER,
                price REAL,
                category_id INTEGER,
                supplier_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories (id),
                FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS items"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO items (name, quantity, price, category_id, supplier_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.quantity, self.price, self.category_id, self.supplier_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, quantity, price, category_id, supplier_id):
        item = cls(name, quantity, price, category_id, supplier_id)
        item.save()
        return item
    
    @classmethod
    def instance_from_db(cls, row):
        item = cls.all.get(row[0])
        if item:
            item.name = row[1]
            item.quantity = row[2]
            item.price = row[3]
            item.category_id = row[4]
            item.supplier_id = row[5]
        else:
            try:
                item = cls(row[1], row[2], row[3], row[4], row[5])
                item.id = row[0]
                cls.all[item.id] = item
            except ValueError as e:
                print(f"Warning: {e} - Skipping item with ID {row[0]}")
            return None
        return item

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM items"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM items WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM items WHERE name = ?"
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_items_by_category_id(cls, category_id):
        sql = "SELECT * FROM items WHERE category_id = ?"
        rows = CURSOR.execute(sql, (category_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_items_by_supplier_id(cls, supplier_id):
        sql = "SELECT * FROM items WHERE supplier_id = ?"
        rows = CURSOR.execute(sql, (supplier_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def update(self):
        sql = """
        UPDATE items
        SET name = ?, quantity = ?, price = ?, category_id = ?, supplier_id = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.quantity, self.price, self.category_id, self.supplier_id, self.id))
        CONN.commit()

    @classmethod
    def delete(cls, id):
        sql = """
        DELETE FROM items
        WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        CONN.commit()
        if id in cls.all:
            del cls.all[id]

    @property
    def category(self):
        return Category.find_by_id(self.category_id)

    @property
    def supplier(self):
        return Supplier.find_by_id(self.supplier_id)

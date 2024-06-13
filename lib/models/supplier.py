from models.__init__ import CURSOR, CONN

class Supplier:
    all = {}

    def __init__(self, name, address, phone, id=None):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone

    def __repr__(self):
        return f"<Supplier {self.id}: {self.name}, {self.address}, {self.phone}>"

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
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str) and len(address):
            self._address = address
        else:
            raise ValueError("Address must be a non-empty string")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if isinstance(phone, str) and len(phone):
            self._phone = phone
        else:
            raise ValueError("Phone must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                phone TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS suppliers"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO suppliers (name, address, phone) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.name, self.address, self.phone))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, address, phone):
        supplier = cls(name, address, phone)
        supplier.save()
        return supplier

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM suppliers"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM suppliers WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM suppliers WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        supplier = cls.all.get(row[0])
        if supplier:
            supplier.name = row[1]
            supplier.address = row[2]
            supplier.phone = row[3]
        else:
            supplier = cls(row[1], row[2], row[3])
            supplier.id = row[0]
            cls.all[supplier.id] = supplier
        return supplier

    def items(self):
        from models.item import Item
        sql = "SELECT * FROM items WHERE supplier_id = ?"
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Item.instance_from_db(row) for row in rows]

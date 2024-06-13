from models.__init__ import CURSOR, CONN

class Supplier:
    all = {}

    def __init__(self, name, contact=None, address=None, id=None):
        self.id = id
        self.name = name
        self.contact = contact
        self.address = address

    def __repr__(self):
        return f"<Supplier {self.id}: {self.name}>"

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
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            contact TEXT,
            address TEXT
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
        if self.id:
            self.update()
        else:
            sql = "INSERT INTO suppliers (name, contact, address) VALUES (?, ?, ?)"
            CURSOR.execute(sql, (self.name, self.contact, self.address))
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self

    @classmethod
    def create(cls, name, contact, address):
        supplier = cls(name, contact, address)
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

    def update(self):
        sql = "UPDATE suppliers SET name = ?, contact = ?, address = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.contact, self.address, self.id))
        CONN.commit()

    @classmethod
    def delete(cls, id):
        sql = "DELETE FROM suppliers WHERE id = ?"
        CURSOR.execute(sql, (id,))
        CONN.commit()
        del cls.all[id]

    @classmethod
    def instance_from_db(cls, row):
        supplier = cls.all.get(row[0])
        if supplier:
            supplier.name = row[1]
            supplier.contact = row[2]
            supplier.address = row[3]
        else:
            supplier = cls(row[1], row[2], row[3])
            supplier.id = row[0]
            cls.all[supplier.id] = supplier
        return supplier

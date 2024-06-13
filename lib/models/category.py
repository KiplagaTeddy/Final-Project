from models.__init__ import CURSOR, CONN

class Category:
    all = {}

    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Category {self.id}: {self.name}, {self.description}>"

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
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError("Description must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS categories"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO categories (name, description) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.description))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, description):
        category = cls(name, description)
        category.save()
        return category

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM categories"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM categories WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM categories WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def delete(cls, id_):
        sql = "DELETE FROM categories WHERE id = ?"
        CURSOR.execute(sql, (id_,))
        CONN.commit()
        cls.all.pop(id_, None)

    @classmethod
    def instance_from_db(cls, row):
        category = cls.all.get(row[0])
        if category:
            category.name = row[1]
            category.description = row[2]
        else:
            category = cls(row[1], row[2])
            category.id = row[0]
            cls.all[category.id] = category
        return category

    def items(self):
        from models.item import Item
        sql = "SELECT * FROM items WHERE category_id = ?"
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Item.instance_from_db(row) for row in rows]

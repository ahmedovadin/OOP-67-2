import sqlite3

connect = sqlite3.connect('store.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50) NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

connect.commit()

# CRUD
def create_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products(name, price, quantity) VALUES(?,?,?)',
        (name, price, quantity)
    )
    connect.commit()
    print("Продукт создан!")

create_product("Arzy", 33, "кушать-спать-играть")


def get_products():
    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    print(data)

get_products()

def update_product(price, id):
    cursor.execute(
        'UPDATE products SET price=? WHERE id=?',
        (price, id)
    )
    connect.commit()
    print("Продукт обновлен!")

update_product(500, 1)

def delete_product(id):
    cursor.execute(
        'DELETE FROM products WHERE id=?',
        (id,)
    )
    connect.commit()
    print("Продукт удален!")

delete_product(1)

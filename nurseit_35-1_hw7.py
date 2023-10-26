import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('hw.dw')
cursor = connection.cursor()
cursor.execute
sql_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,  
    quantity INTEGER NOT NULL
);
'''


def create_products(connection):
    products = [
        ('Kefir', 58.25, 5),
        ('Carrots', 45.15, 8),  # штучно
        ('ASU', 45.07, 1),
        ('Chips', 65.30, 2),
        ('Cookies', 80.38, 10),  # штучно
        ('Milk', 35.15, 2),
        ('Eggs', 15.00, 10),  # штучно
        ('Sausages', 70.25, 4),
        ('Butter', 40.40, 2),
        ('мыло', 68.15, 1),
        ('Жидкое мыло', 45.15, 1),  # мешок
        ('Хозяйственное мыло', 65.05, 1),  # мешок
        ('Детское мыло', 25.00, 2),
        ('Лечебно-косметическое мыло', 70.10, 2),
        ('Bread', 35.15, 2)
    ]
    sql = """
         INSERT INTO products 
         (product_title, price, quantity) 
         VALUES (?, ?, ?)
         """
    cursor = connection.cursor()
    cursor.execute(sql, connection)
    connection.commit()


def add_product(product_title, price, quantity):
    sql = "INSERT INTO products ?, ?, ?"
    cursor = connection.cursor()
    cursor.execute(sql, (product_title, price, quantity))
    connection.commit()


def change_quantity(connection, new_quantity, product_id):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_quantity, product_id))
    connection.commit()


def change_price(connection, new_price, product_id):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_price, product_id))
    connection.commit()


def delete_products(connection, products_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (products_id,))
    connection.commit()


def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    cursor = connection.cursor()
    cursor.execute(sql)
    products = cursor.fetchall()
    for product in products:
        print()


def select_cheap_products(connection):
    sql = '''SELECT * FROM products WHERE price < 100.00 AND quantity > 5'''
    cursor = connection.cursor()
    cursor.execute(sql)
    products = cursor.fetchall()
    for product in products:
        print()


def search_products_by_title():
    sql = '''
    SELECT * FROM products WHERE product_title LIKE ?
    '''
    cursor = connection.cursor()
    cursor.execute(sql)
    products = cursor.fetchall()
    for product in products:
        print()


    connection.close()

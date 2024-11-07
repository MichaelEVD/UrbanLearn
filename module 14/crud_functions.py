import sqlite3
connection = sqlite3.connect("catalog_prod.db")
cursor = connection.cursor()
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    # for i in range(1,5):
    #     cursor.execute('INSERT INTO Products (title,description,price) VALUES(?,?,?)',
    #                    (f'Продукт {i}', f'Описание {i}', f'{i*100}'))

    connection.commit()
def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    all_product = cursor.fetchall()
    return all_product


initiate_db()




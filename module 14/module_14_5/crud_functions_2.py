import sqlite3
connection = sqlite3.connect("catalog_prod.db")
connection_2 = sqlite3.connect('table_users.db')
cursor = connection.cursor()
cursor_2 = connection_2.cursor()
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
    cursor_2.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL)
        ''')

    connection.commit()
    connection_2.commit()
def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    all_product = cursor.fetchall()
    return all_product
def add_user(username, email, age):
    cursor_2.execute("SELECT COUNT(*) FROM Users")
    num_user = cursor_2.fetchone()[0] + 1
    cursor_2.execute(f'''
    INSERT INTO Users VALUES('{num_user}', '{username}', '{email}', '{age}', '1000')
    ''')
    connection_2.commit()

def is_included(username):
    flag = True
    check_user = cursor_2.execute('SELECT * FROM Users WHERE username=?',(username,))
    if check_user.fetchone() is None:
        flag = False
    return flag


initiate_db()
print(get_all_products())
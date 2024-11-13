import sqlite3


def initiate_db():
    """
    Создает таблицу базы данных, если она не существует.
    Таблица должна содержать следующие поля:
        id - целое число, первичный ключ
        title(название продукта) - текст (не пустой)
        description(описание) - текст
        price(цена) - целое число (не пустой)
    """
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    # Создаем таблицу products
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER
        )
    """)
    connection.commit()

    # Создаем таблицу Users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    """)
    connection.commit()
    connection.close()


def add_user(username, email, age):
    """
    Добавляет пользователя в базу данных в таблицу Users
    """
    if is_included(username):
        return "Пользователь уже существует"

    initial_balance = 1000
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   [username, email, age, initial_balance])
    connection.commit()
    connection.close()
    return "ok"


def is_included(username):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    user_result = cursor.execute("SELECT * FROM Users WHERE username = ?",
                                 [username]).fetchone()
    if user_result is not None:
        return True
    else:
        return False


def get_all_products():
    """
    Возвращает все продукты из базы данных.
    """
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()

    connection.close()
    return rows


def fill_data():
    """
    Заполняет базу данных продуктами из словаря.
    """
    product_data = {"Private Jet": ["Самолет", "На нем можно летать куда угодно", 100],
                    "Yacht": ["Яхта", "На ней можно уплыть куда угодно", 200],
                    "Private Island": ["Остров", "На нем можно жить сколько угодно", 550],
                    "Private Castle": ["Замок", "В нем можно жить как угодно", 300]}

    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    for key_item in product_data.keys():
        title = product_data[key_item][0]
        description = product_data[key_item][1]
        price = product_data[key_item][2]
        cursor.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)",
                       (title, description, price))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    print("Hello!")
    # add_user("admin","admin@mail.com",35)
    # initiate_db()
    # fill_data()

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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER
        )
    """)

    connection.commit()
    connection.close()


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
    product_data = {"Private Jet": ["Самолет", "На нем можно летать куда угодно", 100000000],
                    "Yacht": ["Яхта", "На ней можно уплыть куда угодно", 20000000],
                    "Private Island": ["Остров", "На нем можно жить сколько угодно", 150000000],
                    "Private Castle": ["Замок", "В нем можно жить как угодно", 70000000]}

    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    for key_item in product_data.keys():
        title = product_data[key_item][0]
        description = product_data[key_item][1]
        price = product_data[key_item][2]
        cursor.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    initiate_db()
    fill_data()

import sqlite3
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute(""
               "CREATE TABLE IF NOT EXISTS Users ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "username TEXT NOT NULL,"
               "email TEXT NOT NULL,"
               "age INTEGER,"
               "balance INTEGER);"
               "")

connection.commit()

for i in range(1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (f"User{i}", f"example{i}@gmail.com", i*10, 1000))
    connection.commit()

for i in range( 1, 11, 2):
    cursor.execute("UPDATE Users SET balance = 500 WHERE username = ?", (f"User{i}",))
    connection.commit()

for i in range( 1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))
    connection.commit()

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]}, Почта: {user[2]}, Возраст: {user[3]}, Баланс: {user[4]}")
connection.commit()

# Добавлено для задания 14.2
cursor.execute("DELETE FROM Users WHERE id=?",(6,))
connection.commit()

cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]
print(f"Всего пользователей: {total}")

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]
print(f"Суммарный баланс: {total_balance}")

cursor.execute("SELECT AVG(balance) FROM Users")
average_balance = cursor.fetchone()[0]
print(f"Средний баланс: {average_balance}")


connection.close()
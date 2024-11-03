import sqlite3

def initiate_db():                                     # Функция для создания таблицы Products в файле not_telegram.db
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEDGER PRIMARY KEY, 
    title TEXT NOT NULL,
    description TEXT,
    price INTEDGER NOT NULL
    )
    """)

    # Цикл для заполнения таблицы Products

    for i in range(1,5):
        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)",
                       (i, f"Product: {i}", f"Описание: {i}", f"Цена: {i * 100}"))
    connection.commit()  # Сохраняем состояние
    connection.close()

def get_all_products(id):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
    connection.commit()  # Сохраняем состояние
    prod = cursor.fetchall() # Сохраняем записи в переменной prod
    id, title, description, price = prod[0]
    return f"Название: {title} | Описание: {description} | Цена: {price}"
    connection.close()

# initiate_db()  # Запускать функцию initiate_db для создания (если ее нет) и заполнение таблицы Products.
# Далее закомментировать вызов функции initiate_db()



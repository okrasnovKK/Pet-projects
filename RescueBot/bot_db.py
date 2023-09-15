import sqlite3


with sqlite3.connect('db_rescue_bot.db', check_same_thread=False) as db:
    c = db.cursor()


# # Создание таблицы
#     c.execute("""CREATE TABLE requests (
#     request_id INT PRIMARY KEY,
#     request text,
#     person_id INT,
#     date_time DATETIME DEFAULT CURRENT_TIMESTAMP)
#         """)


# Добавление записей
    def add(info_1, info_2):
        c.execute(f"""INSERT INTO requests(request, person_id) VALUES('{info_1}', '{info_2}')""")
        db.commit()


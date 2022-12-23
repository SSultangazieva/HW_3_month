import random
import sqlite3

# СУБД - Система управления базой данных
# SQL = Structured Query Language

# создаем базу данных
def sql_create():
    global db, cursor
    # в db хранится подключение
    db = sqlite3.connect("db.sqlite3") # или bot.sqlite3
    # cursor - ею мы отправляем наши запросы в БД
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    # создаем таблицу в БД  db.execute - когда
    db.execute("CREATE TABLE IF NOT EXISTS mentors"
               "(id INTEGER PRIMARY KEY, username TEXT, "
               "name TEXT,direction TEXT, age INTEGER, gruppa TEXT, "
               "photo TEXT)")
    # сохранить изменения (подтвердить наши изменения)
    db.commit()
# сам запуск в main.py

# заполнение таблицы в БД
async def sql_command_insert(state):
    # открываем кэш
    async with state.proxy() as data:
        # cursor.execute - передаем данных кэш на бд
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    await message.answer_photo(
        random_user[6],
        caption=f"{random_user[2]} {random_user[3]} {random_user[4]} "
                f"{random_user[5]}\n{random_user[1]}"
    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()

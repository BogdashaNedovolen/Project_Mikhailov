"""
Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета информации
о промышленных предприятиях республики. БД содержит таблицу Предприятия,
имеющую следующую структуру записи: Код предприятия, Наименование предприятия,
Физический адрес, Филиалы (количество филиалов), Общая числ. персонала, 
Общая стоим. оборудования, Объем выпускаемой продукции, Дата регистрации.
"""

import sqlite3
import csv

db_file = "industry.db"
csv_file = "enterprises.csv"


def init_db():
    con = sqlite3.connect(db_file)
    con.execute("""
            CREATE TABLE IF NOT EXISTS enterprises (
                code INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                fillials INTEGER DEFAULT 0,
                staff_kolvo INTEGER,
                equipment_cost REAL,
                production_size REAL,
                reg_date TEXT
            )
        """
        )
    con.commit()

    if con.execute("SELECT COUNT(*) FROM enterprises").fetchone()[0] == 0:
        with open(csv_file, encoding="utf-8") as file:
            rows = [
                (r["name"], r["address"], int(r["fillials"]),
                 int(r["staff_kolvo"]), float(r["equipment_cost"]),
                 float(r["production_size"]), r["reg_date"])
                for r in csv.DictReader(file)
            ]
        con.executemany(
            "INSERT INTO enterprises "
            "(name,address,fillials,staff_kolvo,equipment_cost,production_size,reg_date) "
            "VALUES (?,?,?,?,?,?,?)", rows
        )
        con.commit()

    return con


HEADERS = ["Код", "Название", "Адрес", "Филиалы", "Персонал", "Стоимость оборудования", "Объём продукции", "Дата регистрации"]

def show(rows):
    if not rows:
        print("Нет данных.")
        return
    print(" ".join(HEADERS))
    for r in rows:
        print(" ".join(str(x) for x in r))


def show_all(con, cur):
    cur.execute("SELECT * FROM enterprises ORDER BY code")
    show(cur.fetchall())


def add(con, cur):
    try:
        cur.execute(
            "INSERT INTO enterprises "
            "(name,address,fillials,staff_kolvo,equipment_cost,production_size,reg_date) "
            "VALUES (?,?,?,?,?,?,?)",
            (
                input("Название: "),
                input("Адрес: "),
                int(input("Филиалы: ")),
                int(input("Персонал: ")),
                float(input("Стоимость оборудования: ")),
                float(input("Объём продукции: ")),
                input("Дата регистрации (ГГГГ-ММ-ДД): ")
            )
        )
        con.commit()
        print("Добавлено.")
    except Exception as e:
        print(f"Ошибка: {e}")


def search(con, cur):
    print("1-по коду  2-по названию  3-по дате")
    choice = input("Вариант: ")
    try:
        if choice == "1":
            cur.execute("SELECT * FROM enterprises WHERE code=?",
                        (int(input("Код: ")),))
        elif choice == "2":
            cur.execute("SELECT * FROM enterprises WHERE name LIKE ?", (f"%{input('Название: ')}%",))
        elif choice == "3":
            cur.execute("SELECT * FROM enterprises WHERE reg_date=?", (input("Дата (ГГГГ-ММ-ДД): "),))
        else:
            return
        show(cur.fetchall())
    except Exception as e:
        print(f"Ошибка: {e}")


def edit(con, cur):
    print("1. По коду 2. По адресу  3. По дате")
    choice = input("Вариант: ")
    try:
        if choice == "1":
            code = int(input("Код: "))
            cur.execute("SELECT * FROM enterprises WHERE code=?", (code,))
            row = cur.fetchone()
            if not row:
                print("Не найдено.")
                return
            print(f"Текущие данные: {row}")
            print("1. Название  2. Адрес  3. Филиалы  4. Персонал  5. Стоимость оборудования  6. Объём продаж  7. Дата регистрации")
            field_map = {
                "1": "name", "2": "address", "3": "fillials",
                "4": "staff_kolvo", "5": "equipment_cost",
                "6": "production_size", "7": "reg_date"
            }
            field = input("Поле: ")
            if field not in field_map:
                print("Неверный выбор.")
                return
            value = input("Новое значение: ")
            if field in ("3", "4"):
                value = int(value)
            elif field in ("5", "6"):
                value = float(value)
            cur.execute(f"UPDATE enterprises SET {field_map[field]}=? WHERE code=?", (value, code))

        elif choice == "2":
            address = input("Адрес (часть): ")
            cur.execute("SELECT * FROM enterprises WHERE address LIKE ?", (f"%{address}%",))
            rows = cur.fetchall()
            if not rows:
                print("Не найдено.")
                return
            show(rows)
            field_map = {
                "1": "name", "2": "address", "3": "fillials",
                "4": "staff_kolvo", "5": "equipment_cost",
                "6": "production_size", "7": "reg_date"
            }
            print("1. Название  2. Адрес  3. Филиалы  4. Персонал  5. Стоимость оборудования  6. Объём продаж  7. Дата регистрации")
            field = input("Поле: ")
            if field not in field_map:
                print("Неверный выбор.")
                return
            value = input("Новое значение: ")
            if field in ("3", "4"):
                value = int(value)
            elif field in ("5", "6"):
                value = float(value)
            cur.execute(f"UPDATE enterprises SET {field_map[field]}=? WHERE address LIKE ?", (value, f"%{address}%"))

        elif choice == "3":
            date = input("Дата (ГГГГ-ММ-ДД): ")
            cur.execute("SELECT * FROM enterprises WHERE reg_date=?", (date,))
            rows = cur.fetchall()
            if not rows:
                print("Не найдено.")
                return
            show(rows)
            field_map = {
                "1": "name", "2": "address", "3": "fillials",
                "4": "staff_kolvo", "5": "equipment_cost",
                "6": "production_size", "7": "reg_date"
            }
            print("1. Название  2. Адрес  3. Филиалы  4. Персонал  5. Стоимость оборудования  6. Объём продаж  7. Дата регистрации")
            field = input("Поле: ")
            if field not in field_map:
                print("Неверный выбор.")
                return
            value = input("Новое значение: ")
            if field in ("3", "4"):
                value = int(value)
            elif field in ("5", "6"):
                value = float(value)
            cur.execute(f"UPDATE enterprises SET {field_map[field]}=? WHERE reg_date=?", (value, date))

        else:
            return

        con.commit()
        print(f"Обновлено: {cur.rowcount} запись.")
    except Exception as e:
        print(f"Ошибка: {e}")


def delete(con, cur):
    print("1-по коду  2-по адресу  3-по дате")
    choice = input("Вариант: ")
    try:
        if choice == "1":
            cur.execute("DELETE FROM enterprises WHERE code=?",
                        (int(input("Код: ")),))
        elif choice == "2":
            cur.execute("DELETE FROM enterprises WHERE address LIKE ?",
                        (f"%{input('Адрес (часть): ')}%",))
        elif choice == "3":
            cur.execute("DELETE FROM enterprises WHERE reg_date=?",
                        (input("Дата (ГГГГ-ММ-ДД): "),))
        else:
            return
        con.commit()
        print(f"Удалено: {cur.rowcount} запись.")
    except Exception as e:
        print(f"Ошибка: {e}")


def main():
    con = init_db()
    cur = con.cursor()

    while True:
        print("\nПРОМЫШЛЕННОСТЬ")
        print("1. Показать все")
        print("2. Добавить")
        print("3. Найти")
        print("4. Редактировать")
        print("5. Удалить")
        print("0. Выход")
        ch = input("Действие: ").strip()

        if ch == "1":
            show_all(con, cur)
        elif ch == "2":
            add(con, cur)
        elif ch == "3":
            search(con, cur)
        elif ch == "4":
            edit(con, cur)
        elif ch == "5":
            delete(con, cur)
        elif ch == "0":
            print("Выход.")
            break
        else:
            print("Неверный ввод.")

    con.close()


if __name__ == "__main__":
    main()

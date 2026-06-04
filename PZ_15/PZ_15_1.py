"""
Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета информации
о промышленных предприятиях республики. БД содержит таблицу Предприятия,
имеющую следующую структуру записи: Код предприятия, Наименование предприятия,
Физический адрес, Филиалы (количество филиалов), Общая числ. персонала, 
Общая стоим. оборудования, Объем выпускаемой продукции, Дата регистрации.
"""

import sqlite3 as sq

DB = "industry.db"


def get_db():
    """Подключение к БД и создание таблицы при отсутствии."""
    con = sq.connect(DB)
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS enterprises(
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
    return con


def show(rows):
    """Вывод данных в консоль без жесткого форматирования ширины."""
    if not rows:
        print("Нет данных")
        return
    
    headlines = [
        "Код", "Название", "Адрес", "Филиалы", 
        "Персонал", "Стоимость оборудования", "Объем продаж", "Дата регистрации"
    ]
    
    # Заголовки через табуляцию для естественного выравнивания
    print("\t".join(headlines))
    print("-" * 90)
    
    for r in rows:
        # Преобразуем все элементы в строки для безопасного join
        line = "\t".join(str(x) for x in r)
        print(line)


def search(cur):
    """Поиск по 3 вариантам SQL-запросов."""
    c = input("Поиск: 1-по коду, 2-по названию, 3-фильтр персонал/стоимость: ")
    try:
        if c == '1':
            cur.execute("SELECT * FROM enterprises WHERE code=?", (int(input("Код: ")),))
        elif c == '2':
            cur.execute(
                "SELECT * FROM enterprises WHERE name LIKE ?", 
                (f"%{input('Часть названия: ')}%",)
            )
        elif c == '3':
            s = int(input("Мин. персонал: "))
            cost = float(input("Мин. стоимость оборудования: "))
            cur.execute(
                "SELECT * FROM enterprises WHERE staff_kolvo>? AND equipment_cost>?", 
                (s, cost)
            )
        else:
            return
        show(cur.fetchall())
    except Exception as e:
        print(f"Ошибка поиска: {e}")


def delete(con, cur):
    """Удаление по 3 вариантам SQL-запросов."""
    c = input("Удаление: 1-по коду, 2-без филиалов, 3-до даты регистрации: ")
    try:
        if c == '1':
            cur.execute("DELETE FROM enterprises WHERE code=?", (int(input("Код: ")),))
        elif c == '2':
            confirm = input("Удалить ВСЕ предприятия без филиалов? (y/n): ")
            if confirm.lower() != 'y':
                print("Отменено.")
                return
            cur.execute("DELETE FROM enterprises WHERE fillials=0")
        elif c == '3':
            date = input("Дата (ГГГГ-ММ-ДД), до которой удалить: ")
            cur.execute("DELETE FROM enterprises WHERE reg_date<?", (date,))
        else:
            return
        
        con.commit()
        print(f"Удалено записей: {cur.rowcount}")
    except Exception as e:
        print(f"Ошибка удаления: {e}")
        con.rollback()


def edit(con, cur):
    """
    Редактирование по 3 РЕАЛИСТИЧНЫМ бизнес-сценариям:
    1. Ребрендинг и переезд (смена имени + адреса)
    2. Индексация стоимости оборудования (бухгалтерская переоценка)
    3. Кадровая ротация + дата аттестации
    """
    choose = input(
        "\nРЕДАКТИРОВАНИЕ\n"
        "1 - Ребрендинг и переезд (новое имя + адрес)\n"
        "2 - Индексация стоимости оборудования (коэффициент)\n"
        "3 - Кадровая ротация + дата аттестации\n"
        "Выбор: "
    )
    
    try:
        if choose == '1':
            # Сценарий: предприятие сменило название и переехало
            code = int(input("Код предприятия: "))
            new_name = input("Новое наименование: ")
            new_addr = input("Новый физический адрес: ")
            
            # Обновляем два поля одновременно по первичному ключу
            sql = "UPDATE enterprises SET name=?, address=? WHERE code=?"
            cur.execute(sql, (new_name, new_addr, code))
            
        elif choose == '2':
            # Сценарий: ежегодная индексация ОС из-за инфляции
            city_part = input("Часть города в адресе (для выборки): ")
            index_coeff = float(input("Коэффициент индексации (например, 1.15 для +15%): "))
            
            # Умножаем текущую стоимость на коэффициент для всех предприятий города
            sql = "UPDATE enterprises SET equipment_cost=equipment_cost*? WHERE address LIKE ?"
            cur.execute(sql, (index_coeff, f"%{city_part}%"))
            
        elif choose == '3':
            # Сценарий: изменение штата после сокращения/найма + фиксация даты проверки
            code = int(input("Код предприятия: "))
            new_staff = int(input("Актуальная численность персонала: "))
            attest_date = input("Дата последней аттестации (ГГГГ-ММ-ДД): ")
            
            # Обновляем персонал и дату аттестации
            sql = "UPDATE enterprises SET staff_kolvo=?, reg_date=? WHERE code=?"
            cur.execute(sql, (new_staff, attest_date, code))
        else:
            print("Неверный выбор.")
            return
            
        con.commit()
        print(f"Операция выполнена. Затронуто строк: {cur.rowcount}")
        
    except ValueError:
        print("Ошибка: проверьте числовые значения и формат даты.")
    except Exception as e:
        print(f"Ошибка редактирования: {e}")
        con.rollback()


def main():
    """Главное меню приложения."""
    with get_db() as con:
        cur = con.cursor()
        
        while True:
            print(
                "\nПРОМЫШЛЕННОСТЬ\n"
                "1. Показать все предприятия\n"
                "2. Добавить предприятие\n"
                "3. Поиск предприятия\n"
                "4. Редактировать данные\n"
                "5. Удалить запись\n"
                "0. Выход"
            )
            
            ch = input("Выберите действие: ").strip()
            
            if ch == '1':
                cur.execute("SELECT * FROM enterprises ORDER BY code")
                show(cur.fetchall())
                
            elif ch == '2':
                try:
                    mass_input = [
                        input("Наименование: "),
                        input("Физический адрес: "),
                        int(input("Количество филиалов: ")),
                        int(input("Численность персонала: ")),
                        float(input("Стоимость оборудования: ")),
                        float(input("Объем выпускаемой продукции: ")),
                        input("Дата регистрации (ГГГГ-ММ-ДД): ")
                    ]
                    cur.execute(
                        "INSERT INTO enterprises "
                        "(name,address,fillials,staff_kolvo,equipment_cost,production_size,reg_date) "
                        "VALUES (?,?,?,?,?,?,?)", 
                        mass_input
                    )
                    con.commit()
                    print("Предприятие добавлено!")
                except Exception as e:
                    print(f"Ошибка добавления: {e}")
                    
            elif ch == '3':
                search(cur)
            elif ch == '4':
                edit(con, cur)
            elif ch == '5':
                delete(con, cur)
            elif ch == '0':
                print("Работа завершена.")
                break
            else:
                print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()

import sqlite3 as sq
import csv

conn = sq.connect('phonbook1.db')

cur = conn.cursor()
# abonid INTEGER PRIMARY KEY AUTOINCREMENT,

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook(
    fname TEXT,
    lname TEXT NOT NULL,
    phone TEXT );
""")
conn.commit()

def lower_string(_str):
    return _str.lower()

conn.create_function("mylower", 1, lower_string)

def add_abon():
    global abon
    abon = ()
    lname = input('Введите фамилию ')
    fname = input('Введите имя ')
    phone = input('Введите номер телефона ')
    abon = (fname, lname, phone)
    print(abon)
    cur.execute(
        "INSERT INTO phonebook VALUES(?, ?, ?)", abon)
    conn.commit()


def find_abon():
    flag = ''
    lname = input('Введите фамилию или ее часть для поиска \n или Enter для выхода ')
    flag = lname
    cur.execute("SELECT * FROM phonebook WHERE mylower(lname) LIKE ? or mylower(fname) LIKE  ? or phone LIKE ?;", ("%" + lname + "%", "%" + lname + "%", "%" + lname + "%",))
    all_results = cur.fetchall()
    print('\n')
    if flag == '':
        return flag

    elif all_results == []:
        print('Данные отсутствуют. Уточните условия поиска ')
    else:
        for q in all_results:
            print(' '.join(q), '\n')


while True:

    if find_abon() == '':
        break
    else:
        find_abon

conn.close()
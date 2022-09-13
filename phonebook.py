import sqlite3 as sq
import exim

conn = sq.connect('phonbook.db')

cur = conn.cursor()

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
    cur.execute("SELECT rowid, fname, lname, phone FROM phonebook WHERE mylower(lname) LIKE ? or mylower(fname) LIKE  ? or phone LIKE ?;", ("%" + lname + "%", "%" + lname + "%", "%" + lname + "%",))
    all_results = cur.fetchall()
    print('\n')
    if flag == '':
        return flag

    elif all_results == []:
        print('Данные отсутствуют. Уточните условия поиска ')
    else:
        for q in all_results:
            q1 = q[0]
            q2 = q[1:]
            print(q1, ' '.join(q2), '\n')




def update_abon():
    find_abon()
    r = input('Для выбора измененяемой записи введите соответсвующую цифру слева  если передумали - Enter ')
    if r != '':
        r_id = int(r)
        cur.execute("SELECT * FROM phonebook WHERE  rowid = ?;", ( r_id , ))
        result = cur.fetchall()
        for q in result:
            print('\n', ' '.join(q))
        while True:
            flag = input('Меняем? Y/N ')
            if flag == 'y' or flag == 'Y':
                lname = input('Введите фамилию или ENTER, если не меняем ')
                if lname == '':
                    lname = q[1]
                fname = input('Введите имя или ENTER, если не меняем ')
                if fname == '':
                    fname = q[0]
                phone = input('Введите номер телефона или ENTER, если не меняем ')
                if phone == '':
                    phone = q[2]
                #print(fname)
                cur.execute("UPDATE phonebook SET fname = ?,lname = ?, phone = ? WHERE rowid = ?;", (fname, lname, phone, r_id))
                conn.commit()
                print('Записано')
                break
            elif flag == 'n' or flag == 'N':
                break

def delet_abon():
    find_abon()
    r = input('Для выбора удаляемой записи введите соответсвующую цифру слева  если передумали - Enter ')
    if r != '':
        r_id = int(r)
        cur.execute("SELECT * FROM phonebook WHERE  rowid = ?;", ( r_id , ))
        result = cur.fetchall()
        for q in result:
            print('\n', ' '.join(q))
        while True:
            flag = input('Удаляем? Y/N ')
            if flag == 'y' or flag == 'Y':
                cur.execute("DELETE FROM phonebook WHERE rowid = ?;", (r_id,))
                conn.commit()
                print('Удалено')
                break
            elif flag == 'n' or flag == 'N':
                break

def show_all():
    cur.execute("SELECT * FROM phonebook;")
    all_results = cur.fetchall()
    for q in all_results:
            #q1 = q[0]
            #q2 = q[1:]
            print(' '.join(q), '\n')


while True:
    fl = input('1 - телефонная книга \n2 - импорт/экспорт данных \nдля выхода - 0 ')
    fl = int(fl)
    if fl == 1:

        while True:
            fl1 = input('1 - просмотр всех записей \n2 - поиск записей \n3 - изменений записей \n4- удаление записей \nдля выхода - 0 ')
            fl1 = int(fl1)

            if fl1 == 1:
                show_all()

            elif fl1 == 2:
                find_abon()

            elif fl1 == 3:
                update_abon()

            elif fl1 == 4:
                delet_abon()

            elif fl1 == 0:
                break

    elif fl == 2:
        while True:
            fl2 = input('1 - импорт txt \n2 - экспорт txt \n3 - импорт csv \n4 - экспорт csv \nдля выхода - 0 ')
            fl2 = int(fl1)
            if fl2 == 1:
                zz =input('Не забудьте положить файл import_txt.txt в каталог приложения')
                try:
                    exim.import_txt()
                except FileNotFoundError:
                    zz= input('Нет файла с данными для импорта')

            elif fl2 == 2:
                exim.export_txt()

            elif fl2 == 3:
                zz =input('Не забудьте положить файл import_csv.csv в каталог приложения')
                try:
                    exim.import_csv()
                except FileNotFoundError:
                    zz= input('Нет файла с данными для импорта')

            elif fl2 == 4:
                exim.export_csv

            elif fl2 == 0:
                break

    elif fl == 0:
        break


conn.close()
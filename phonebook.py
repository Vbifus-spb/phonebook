import sqlite3 as sq
import exim

conn = sq.connect('phonbook1.db')

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
            flag = input('Меняем? Y/N ')
            if flag == 'y' or flag == 'Y':
                cur.execute("DELETE FROM users WHERE rowid = ?;", (r_id,))
                conn.commit()
                print('Удалено')
                break
            elif flag == 'n' or flag == 'N':
                break



    #print(result)


#find_abon()
#choos_adon()
update_abon()

'''
while True:

    if find_abon() == '':
        break
    else:
        find_abon
'''
conn.close()
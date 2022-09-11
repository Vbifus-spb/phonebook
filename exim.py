

import sqlite3 as sq
import csv

conn = sq.connect('phonbook1.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook(
    fname TEXT,
    lname TEXT NOT NULL,
    phone TEXT );
""")
conn.commit()


def import_csv():
    with open('import_csv.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        print(reader)
        for row in reader:
            print(row)
            r = tuple(row)
            print(r)
            cur.execute(
                    "INSERT INTO phonebook VALUES(?, ?, ?)", r)
            conn.commit()


def export_csv():
    cur.execute("SELECT * FROM phonebook;")
    all_results = cur.fetchall()

    with open('export_csv.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        for row in all_results:
            writer.writerow((row))
            print(row)


def import_txt():
    with open('import_txt.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            t = tuple(item for item in line.split(','))
            #print(t)
            cur.execute(
                    "INSERT INTO phonebook VALUES(?, ?, ?)", t)
            conn.commit()

def export_txt():
    cur.execute("SELECT * FROM phonebook;")
    all_results = cur.fetchall()
    #print(all_results)
    txt_str = ''
    for i in all_results:
        txt_str += ','.join(i)
        txt_str += '\n'
    #print(txt_str)
    with open('export_txt.txt', 'w') as file:
        file.writelines(txt_str)


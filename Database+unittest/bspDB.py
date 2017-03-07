# -*- coding: utf-8 -*-

import sqlite3


def create_db():
    """create database"""

    conn = sqlite3.connect("bsp.db")
    cursor = conn.cursor()

    #create Table
    cursor.execute("CREATE TABLE daten("
                    "name TEXT, datum DATE, preis DEC(10,2), anzahl INT,"
                    "id INTEGER PRIMARY KEY)")

    #insert values
    cursor.execute("INSERT INTO daten(name,datum,preis,anzahl) VALUES("
                    "'Meyer', '2017/23/05', '100.50', 3)")

    #mulitple insertions
    daten = [('Holz', '2012/12/12', '54.95', '9'),
            ('Mueller', '1984/03/04', '33.12', '2'),
            ('Schulz', '2020/09/11', '3000', '5')]

    cursor.executemany("INSERT INTO daten VALUES(?,?,?,?, NULL)", daten)

    #save
    conn.commit()


def select_all_data(what='name', crit=''):
    """selects everything from a given column if the given criterium is met
    (still too hard coded) """

    conn = sqlite3.connect('bsp.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM daten WHERE %s LIKE ?" % (what)
    cursor.execute(sql, (crit + "%",))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def update_data(what, data, new):
    """Changes values in a given column(what) """

    conn = sqlite3.connect('bsp.db')
    cursor = conn.cursor()
    sql = "UPDATE daten SET %s = ? WHERE %s = ?" % (what, what)
    cursor.execute(sql, (new, data))
    conn.commit()
    cursor.close()
    conn.close()


def delete_data(column, crit):
    """Deletes data from given column if criterium is met"""
    conn = sqlite3.connect("bsp.db")
    cursor = conn.cursor()

    sql = "DELETE FROM daten WHERE %s = ?" % (column)
    cursor.execute(sql, (crit,))
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    import os
    #check if database is already there; if not create it
    if not os.path.exists('bsp.db'):
        create_db()

    update_data('anzahl', '5', '6')
    #delete_data('name', 'Mueller')
    print select_all_data('preis', '3')

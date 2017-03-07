# -*- coding: utf-8 -*-
import os
import sqlite3
import unittest
import bspDB


class TestDatabase(unittest.TestCase):

    """runs the unittest multiple times where setUp builds the DB and tearDown deletes it after each
    testfunction
    test__** as well as setUp and tearDown are required keywords"""

    def setUp(self):
        #create db
        conn = sqlite3.connect("bsp.db")
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE daten("
                    "name TEXT, datum DATE, preis DEC(10,2), anzahl INT,"
                    "id INTEGER PRIMARY KEY)")

        cursor.execute("INSERT INTO daten(name,datum,preis,anzahl) VALUES("
                    "'Meyer', '2017/23/05', '100.50', 3)")

        conn.commit()

        daten = [('Holz', '2012/12/12', '54.95', '9'),
            ('Mueller', '1984/03/04', '33.12', '2'),
            ('Schulz', '2020/09/11', '3000', '5')]

        cursor.executemany("INSERT INTO daten VALUES (?,?,?,?, NULL)", daten)
        conn.commit()

    def tearDown(self):
        #delete db
        os.remove("bsp.db")

    def test_update_data(self):
        #test if db updates correctly
        bspDB.update_data('name', 'Schulz', 'Schultz')
        result = bspDB.select_all_data('name', 'Schultz')
        expected = [('Schultz', '2020/09/11', 3000, 5, 4)]
        self.assertEqual(result, expected)


    def test_name_does_not_exist(self):
        #test if test really deletes db
        result = bspDB.select_all_data(crit = 'Schultz')
        self.assertFalse(result)

    def test_select_variability(self):
        # test if wildcard in select works
        result =bspDB.select_all_data('name', 'Muell')
        result2 =bspDB.select_all_data('name', 'Mu')
        expected = [('Mueller','1984/03/04', 33.12, 2, 3)]
        self.assertEqual(result, result2, expected)

    def test_deletion(self):
        bspDB.delete_data('id', '3')
        result = bspDB.select_all_data('name', 'Mu')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
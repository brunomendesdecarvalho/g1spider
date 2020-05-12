# -*- coding: utf-8 -*-

import sqlite3


class G1Pipeline(object):

    def __init__(self):
        self.criar_conexao()
        self.criar_tabela()

    def criar_conexao(self):
        self.con = sqlite3.connect("manchetes_g1.db")
        self.cursor = self.con.cursor()

    def criar_tabela(self):
        self.cursor.execute("""DROP TABLE IF EXISTS manchetes_g1""")
        self.cursor.execute("""create table manchetes_g1(
            Manchete text,
	        Link text
            )
        """)

    def process_item(self, item, spider):
        self.guardar_db(item)
        return item

    def guardar_db(self, item):
        self.cursor.execute("""insert into manchetes_g1 values(
                ?, ?
            )""",
            (
		item['Manchete'],
		item['Link'],
		    ))

        self.con.commit()
import sqlite3


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('prestador.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists prestadores(
                     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     nome text,
                     CPF_CNPJ text,
                     nascimento text,
                     endereço endereço, 
                     contato text)""") #vou precisar criar uma classe endereço
        self.conexao.commit()
        c.close()

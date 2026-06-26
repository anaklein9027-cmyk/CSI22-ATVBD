import sqlite3


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('prestador.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists prestadores(
                     ID integer primary key autoincrement,
                     nome text,
                     CPF_CNPJ integer,
                     nascimento text,
                     endereço endereço, 
                     contato integrer)""") #vou precisar criar uma classe endereço
        self.conexao.commit()
        c.close()

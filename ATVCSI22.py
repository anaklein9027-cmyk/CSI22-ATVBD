#Catálogo de Prestadores de Serviço em Tecnologia da Informação (TI)
from Banco import Banco #ainda não terminei a parte do banco do endereço - acho que a parte do CEP vai precisar de outra função aqui
from tkinter import *
from tkinter import ttk


class Prestador(object):
        def __init__(self, ID=0, nome="", CPF_CNPJ="", nascimento="", endereço="", contato=""):
        self.info = {}
        self.ID = ID
        self.nome = nome
        self.CPF_CNPJ = CPF_CNPJ
        self.nascimento = nascimento
        self.endereço = endereço
        self.contato = contato

        def createPrestador(self):
                banco = Banco();
                try:

                    c = banco.conexao.cursor()
        
                    c.execute("insert into prestadores (ID, nome, CPF_CNPJ, nascimento, endereço, contato) values('" + self.ID + "', '" +
                              self.nome + "', '" + self.CPF_CNPJ + "','" + self.nascimento + "','" + self.endereço + "', '" + self.contato + "' )")
        
                    banco.conexao.commit()
                    c.close()
        
                    return "Prestador cadastrado com sucesso!"
                except:
                    return "Ocorreu um erro no cadastro do prestador"

        
        def readPrestador(self, ID):
                banco = Banco();
                try:

                    c = banco.conexao.cursor()
        
                    c.execute("select * from prestadores where ID = " + ID + "  ")
        
                    for linha in c:
                        self.ID = linha[0]
                        self.nome = linha[1]
                        self.CPF_CNPJ = linha[2]
                        self.nascimento = linha[3]
                        self.endereço = linha[4]
                        self.contato = linha[5]
                    c.close()
        
                    return "Leitura feita com sucesso!"
                except:
                    return "Ocorreu um erro na leitura dos dados do prestador"
                
        def updatePrestador(self):
                banco = Banco();
                try:
        
                    c = banco.conexao.cursor()
        
                    c.execute("update prestadores set nome = '" + self.nome +
                              "', CPF_CNPJ = '" + self.CPF_CNPJ + "', nascimento = '" + self.nascimento + "', endereço = '" + self.endereço + "', contato = '" + self.contato + "' where ID = " + self.ID + " ")
                         #não sei se devo fazer a alterção ser por uma busca de ID Ou de nome - talvez nome faça mais sentido
                    banco.conexao.commit()
                    c.close()
        
                    return "Prestador atualizado com sucesso!"
                except:  
                    return "Ocorreu um erro na alteração das informações do prestador"


        
        def deletePrestador(self):
                banco = Banco();
                try:

                    c = banco.conexao.cursor()
        
                    c.execute("delete from prestadores where ID = " + self.ID + " ")
        
                    banco.conexao.commit()
                    c.close()

                    return "Prestador excluido com sucesso!"
                except:
                    return "Ocorreu um erro na exclusão do prestador"
           

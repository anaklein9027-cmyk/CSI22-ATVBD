from Banco import Banco #ainda não terminei a parte do banco do endereço - acho que a parte do CEP vai precisar de outra função aqui
from tkinter import *
from tkinter import ttk

class Usuarios(object):
    def __init__(self, idusuario = 0, nome = "", telefone = 0, email = "", usuario = "", senha = ""):
        self.idusuario = idusuario
        self.nome = nome
        self.CPF_CNPJ = CPF_CNPJ
        self.nascimento = nascimento
        self.endereço = endereço
        self.contato = contato

    def insertUser(self):
            banco = Banco();
            try:

                c = banco.conexao.cursor()
    
                c.execute("insert into prestadores (ID, nome, CPF_CNPJ, nascimento, endereço, contato) values('" + str(self.idusuario) + "', '" +
                            self.nome + "', '" + self.CPF_CNPJ + "', '" + self.nascimento + "','" + self.endereço + "','" + self.contato + "')")
                
                #c.execute(f"insert into prestadores (ID, nome, CPF_CNPJ, nascimento, endereço, contato) values({self.idusuario},{self.nome},{self.telefone},{self.email},{self.usuario},{self.senha})")
    
                banco.conexao.commit()
                c.close()
    
                return "Prestador cadastrado com sucesso!"
            except:
                raise
                return "Ocorreu um erro no cadastro do prestador"
            
    def updateUser(self):
            banco = Banco();
            try:
    
                c = banco.conexao.cursor()
    
                c.execute("update prestadores set nome = '" + self.nome +
                            "', CPF_CNPJ = '" + self.CPF_CNPJ + "', nascimento = '" + self.nascimento + "', endereço = '" + self.endereço + "', contato = '" + self.contato + "' where ID = " + str(self.idusuario) + " ")
                        #não sei se devo fazer a alterção ser por uma busca de ID Ou de nome - talvez nome faça mais sentido
                banco.conexao.commit()
                c.close()
    
                return "Prestador atualizado com sucesso!"
            except:
                raise
                return "Ocorreu um erro na alteração das informações do prestador"
            
    def deleteUser(self):
            banco = Banco();
            try:

                c = banco.conexao.cursor()
    
                c.execute("delete from prestadores where ID = " + str(self.idusuario) + " ")
    
                banco.conexao.commit()
                c.close()

                return "Prestador excluido com sucesso!"
            except:
                return "Ocorreu um erro na exclusão do prestador"        
    def selectUser(self, ID):
                    banco = Banco();
                    try:
    
                        c = banco.conexao.cursor()
            
                        c.execute("select * from prestadores where ID = " + ID + "  ")
            
                        for linha in c:
                            self.idusuario = linha[0]
                            self.nome = linha[1]
                            self.CPF_CNPJ = linha[2]
                            self.nascimento = linha[3]
                            self.endereço = linha[4]
                            self.contato = linha[5]
                        c.close()
    
                        return "Leitura feita com sucesso!"
                    except:
                        raise
                        return "Ocorreu um erro na leitura dos dados do prestador"

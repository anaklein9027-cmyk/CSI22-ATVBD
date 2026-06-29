from Banco import Banco
from tkinter import *
from Usuarios import Usuarios
import requests

class Application:
    def __init__(self, master=None):
        self.contador_id = 0
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master) # Titulo
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master) # idUsuario
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master) # Nome
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master) # CPF ou CNPJ
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master) #nascimento
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master) # Endereço - CEP
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master) # Endereço - CEP
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        
        self.container8 = Frame(master) # Contato
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master) # Inserir, Alterar, Excluir
        self.container9["padx"] = 20
        self.container9["pady"] = 10
        self.container9.pack()
        self.container10 = Frame(master) # Espaçamento inferior
        self.container10["pady"] = 15
        self.container10.pack()

        self.container11 = Frame(master) # Listagem
        self.container11["pady"] = 15
        self.container11.pack()
        self.container12 = Frame(master) # Listagem
        self.container12["pady"] = 15
        self.container12.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidusuario = Label(self.container2,
        text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.lblnome = Label(self.container3, text="Nome:",
        font =self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblCPF_CNPJ = Label(self.container4, text="CPF ou CNPJ:",
        font=self.fonte, width=10)
        self.lblCPF_CNPJ.pack(side=LEFT)

        self.txtCPF_CNPJ = Entry(self.container4)
        self.txtCPF_CNPJ["width"] = 25
        self.txtCPF_CNPJ["font"] = self.fonte
        self.txtCPF_CNPJ.pack(side=LEFT)

        self.lblnascimento= Label(self.container5, text="Nascimento:",
        font=self.fonte, width=10)
        self.lblnascimento.pack(side=LEFT)

        self.txtnascimento = Entry(self.container5) 
        self.txtnascimento["width"] = 25
        self.txtnascimento["font"] = self.fonte
        self.txtnascimento.pack(side=LEFT)

        self.lblCEP= Label(self.container6, text="CEP:",
        font=self.fonte, width=10)
        self.lblCEP.pack(side=LEFT)

        self.txtCEP = Entry(self.container6)
        self.txtCEP["width"] = 25
        self.txtCEP["font"] = self.fonte
        self.txtCEP.pack(side=LEFT)

        self.btnCEP = Button(self.container6, text="Buscar",
        font=self.fonte, width=10)
        self.btnCEP["command"] = self.buscarEndereco
        self.btnCEP.pack(side=RIGHT)
    #com o CEP retorna o endereço
        self.txtResultado = Entry(self.container7)
        self.txtResultado["width"] = 60
        self.txtResultado["font"] = self.fonte
        self.txtResultado.pack(side=LEFT)

        self.lblcontato= Label(self.container8, text="Contato:",
        font=self.fonte, width=10)
        self.lblcontato.pack(side=LEFT)

        self.txtcontato = Entry(self.container8)
        self.txtcontato["width"] = 25
        self.txtcontato["font"] = self.fonte
        self.txtcontato.pack(side=LEFT)

        self.bntInsert = Button(self.container9, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container9, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container9, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container10, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        self.btnListar = Button(self.container11, text="Listar Prestadores",
        font=self.fonte, width=40)
        self.btnListar["command"] = self.listar
        self.btnListar.pack(side=LEFT)

        self.lbllista = Label(self.container12, text="")
        self.lbllista["font"] = ("Verdana", "9")
        self.lbllista.pack()

    def inserirUsuario(self):
        user = Usuarios()

        #print (self.contador_id)
        user.idusuario = self.contador_id
        self.contador_id += 1

        user.nome = self.txtnome.get()
        user.CPF_CNPJ = self.txtCPF_CNPJ.get()
        user.nascimento = self.txtnascimento.get()
        user.CEP = self.txtCEP.get()
        user.Endereco = self.txtResultado.get()
        user.contato = self.txtcontato.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtCPF_CNPJ.delete(0, END)
        self.txtnascimento.delete(0, END)
        self.txtCEP.delete(0, END)
        self.txtResultado.delete(0, END)
        self.txtcontato.delete(0, END)



    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.CPF_CNPJ = self.txtCPF_CNPJ.get()
        user.nascimento = self.txtnascimento.get()
        user.CEP = self.txtCEP.get()
        user.Endereco  = self.txtResultado.get()
        user.contato = self.txtcontato.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtCPF_CNPJ.delete(0, END)
        self.txtnascimento.delete(0, END)
        self.txtCEP.delete(0, END)
        self.txtResultado.delete(0, END)
        self.txtcontato.delete(0, END)



    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtCPF_CNPJ.delete(0, END)
        self.txtnascimento.delete(0, END)
        self.txtCEP.delete(0, END)
        self.txtResultado.delete(0, END)
        self.txtcontato.delete(0, END)


    def listar(self):
        banco = Banco()
        try:
                 
            c = banco.conexao.cursor()

            c.execute('''SELECT * FROM prestadores''')

            resultados = c.fetchall()

            #print(resultados)

            for res in resultados:
                idd, nome, cpf_cnpj, nascimento, CEP, endereço, contato = res
                print(f"Id: {idd}\nNome: {nome}\nCPF/CNPJ: {cpf_cnpj}\nNascimento: {nascimento}\nCEP: {CEP}, Endereço: {endereço}\nContato: {contato}\n")
                self.lbllista["text"] = f"Id: {idd}\nNome: {nome}\nCPF/CNPJ: {cpf_cnpj}\nNascimento: {nascimento}\nCEP: {CEP},\n Endereço: {endereço}\nContato: {contato}\n"

        except:
            raise
            return "Erro!"


    def buscarEndereco(self):
        cep = self.txtCEP.get()
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        if resposta.status_code != 200:
            return

        dados = resposta.json()

        if "erro" in dados:
            return

        endereco = (
            f'{dados["logradouro"]} - '
            f'{dados["bairro"]} - '
            f'{dados["localidade"]}/{dados["uf"]}'
        )

        self.txtResultado.delete(0, END)
        self.txtResultado.insert(0, endereco)



    
root = Tk()
Application(root)
root.title("Catálogo de TI")
root.mainloop()

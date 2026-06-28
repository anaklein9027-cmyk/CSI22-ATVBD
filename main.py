from Banco import Banco
from tkinter import *
from Usuarios import Usuarios

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
        self.container4 = Frame(master) # Telefone
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master) # CPF ou CNPJ
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master) # Usuario
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master) # Senha
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master) # Inserir, Alterar, Excluir
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master) # Espaçamento inferior
        self.container9["pady"] = 15
        self.container9.pack()

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

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:",
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblCPF_CNPJ= Label(self.container5, text="CPF ou CNPJ:",
        font=self.fonte, width=10)
        self.lblCPF_CNPJ.pack(side=LEFT)

        self.txtemail = Entry(self.container5) #aqui eu uso numero e não texto - precisa alterar
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblusuario= Label(self.container6, text="Usuário:",
        font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha= Label(self.container7, text="Senha:",
        font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirUsuario(self):
        user = Usuarios()

        #print (self.contador_id)
        user.idusuario = self.contador_id
        self.contador_id += 1

        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)



    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)



    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.CPF_CNPJ)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,user.nascimento)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.endereço)

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.contato)

root = Tk()
Application(root)
root.title("Catálogo de TI")
root.mainloop()

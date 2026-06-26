#Catálogo de Prestadores de Serviço em Tecnologia da Informação (TI)
from Banco import Banco #ainda não terminei a parte do banco do endereço
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
        def readPrestador(self):
           banco = Banco();
        def updatePrestador(self):
           banco = Banco();
        def deletePrestador(self):
           banco = Banco();
           

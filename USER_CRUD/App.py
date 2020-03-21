from USER_CRUD.Struct.Usuarios import Usuarios
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 5
        self.container4["padx"] = 20
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 5
        self.container5["padx"] = 20
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 5
        self.container6["padx"] = 20
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["pady"] = 5
        self.container7["padx"] = 20
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["pady"] = 10
        self.container8["padx"] = 20
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbl_usuario_id = Label(self.container2, text="usuario_id:", font=self.fonte, width=10)
        self.lbl_usuario_id.pack(side=LEFT)

        self.txt_usuario_id = Entry(self.container2)
        self.txt_usuario_id["width"] = 10
        self.txt_usuario_id["font"] = self.fonte
        self.txt_usuario_id.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lbl_nome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lbl_nome.pack(side=LEFT)

        self.txt_nome = Entry(self.container3)
        self.txt_nome["width"] = 25
        self.txt_nome["font"] = self.fonte
        self.txt_nome.pack(side=LEFT)

        self.lbl_telefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbl_telefone.pack(side=LEFT)

        self.txt_telefone = Entry(self.container4)
        self.txt_telefone["width"] = 25
        self.txt_telefone["font"] = self.fonte
        self.txt_telefone.pack(side=LEFT)

        self.lbl_email = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lbl_email.pack(side=LEFT)

        self.txt_email = Entry(self.container5)
        self.txt_email["width"] = 25
        self.txt_email["font"] = self.fonte
        self.txt_email.pack(side=LEFT)

        self.lbl_usuario = Label(self.container6, text="Uuario:", font=self.fonte, width=10)
        self.lbl_usuario.pack(side=LEFT)

        self.txt_usuario = Entry(self.container6)
        self.txt_usuario["width"] = 25
        self.txt_usuario["font"] = self.fonte
        self.txt_usuario.pack(side=LEFT)

        self.lbl_senha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lbl_senha.pack(side=LEFT)

        self.txt_senha = Entry(self.container7)
        self.txt_senha["width"] = 25
        self.txt_senha["show"] = "*"
        self.txt_senha["font"] = self.fonte
        self.txt_senha.pack(side=LEFT)

        self.btnInserir = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.btnInserir["command"] = self.inserirUsuario
        self.btnInserir.pack(side=LEFT)

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarUsuario
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluirUsuario
        self.btnExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.txt_nome.get()
        user.telefone = self.txt_telefone.get()
        user.email = self.txt_email.get()
        user.usuario = self.txt_usuario.get()
        user.senha = self.txt_senha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txt_usuario_id.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_usuario.delete(0, END)
        self.txt_senha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.usuario_id = self.txt_usuario_id.get()
        user.nome = self.txt_nome.get()
        user.telefone = self.txt_telefone.get()
        user.email = self.txt_email.get()
        user.usuario = self.txt_usuario.get()
        user.senha = self.txt_senha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txt_usuario_id.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_usuario.delete(0, END)
        self.txt_senha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.usuario_id = self.txt_usuario_id.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txt_usuario_id.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_usuario.delete(0, END)
        self.txt_senha.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        usuario_id = self.txt_usuario_id.get()

        self.lblmsg["text"] = user.selectUser(usuario_id)

        # if(self.lblmsg["text"] == "Ocorreu um erro na busca"):
        #     self.txt_usuario_id.delete(0, END)
        #     self.txt_nome.delete(0, END)
        #     self.txt_telefone.delete(0, END)
        #     self.txt_email.delete(0, END)
        #     self.txt_usuario.delete(0, END)
        #     self.txt_senha.delete(0, END)
        #     self.lblmsg["text"] = "Ocorreu um erro na busca"

        self.txt_usuario_id.delete(0, END)
        self.txt_usuario_id.insert(INSERT, user.usuario_id)

        self.txt_nome.delete(0, END)
        self.txt_nome.insert(INSERT, user.nome)

        self.txt_telefone.delete(0, END)
        self.txt_telefone.insert(INSERT, user.telefone)

        self.txt_email.delete(0, END)
        self.txt_email.insert(INSERT, user.email)

        self.txt_usuario.delete(0, END)
        self.txt_usuario.insert(INSERT, user.usuario)

        self.txt_senha.delete(0, END)
        self.txt_senha.insert(INSERT, user.senha)

root = Tk()
Application(root)
root.mainloop()
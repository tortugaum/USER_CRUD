from .Banco import Banco
import sys


class Usuarios(object):

    def __init__(self, usuario_id = 0, nome = "", telefone = "", email = "", usuario="", senha=""):
        self.info = {}
        self.usuario_id = usuario_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except OSError as err :
            print(err)
            return "Ocorreu um erro durante a alteração"

    def updateUser(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("update usuarios set nome= '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where usuario_id = '" + self.usuario_id + "' ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except OSError as err :
            print(err)
            return "Ocorreu um erro na atualização"

    def deleteUser(self):

        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("delete from usuarios where usuario_id = " + self.usuario_id + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluido com sucesso!"
        except OSError as err :
            print(err)
            return  "Ocorreu um erro durante a exclusão"

    def selectUser(self, usuario_id):

        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("select * from usuarios where usuario_id = '" + usuario_id + "' ")

            for linha in c:
                self.usuario_id = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca realizada!"
        except OSError as err:
            # print(err)
            return "Ocorreu um erro na busca"


import mysql.connector
from prettytable import PrettyTable


class ConexaoBanco:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='003003',
            database='gym_tb',
        )
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()


class OperacoesBanco:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def executar_comando(self, comando):
        self.cursor.execute(comando)
        self.conexao.commit()

    def buscar_dados(self, comando):
        self.cursor.execute(comando)
        tupla = self.cursor.fetchall()

        lista = [list(i) for i in tupla]

        tabela = PrettyTable()
        tabela.field_names = ['matricula', 'nome', 'cpf']
        for row in lista:
            tabela.add_row(row)

        return tabela


def exibir_menu():
    print("Escolha uma opção:")
    print("1. DELETE")
    print("2. CREATE")
    print("3. READ")
    print("4. UPDATE")
    print("5. Sair\n")

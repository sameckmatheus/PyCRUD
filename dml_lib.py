import mysql.connector


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
        return self.cursor.fetchall()


def exibir_menu():
    print("Escolha uma opção:")
    print("1. DELETE")
    print("2. CREATE")
    print("3. READ")
    print("4. UPDATE")
    print("5. Sair")


conexao = ConexaoBanco()
operacoes = OperacoesBanco(conexao.conexao, conexao.cursor)

while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada (1-5): ")

    if opcao == "1":  # DELETE
        nome_aluno_delete = input("Digite o nome do aluno a ser removido: ")
        comando_delete = f'DELETE FROM alunos WHERE nome = "{nome_aluno_delete}"'
        operacoes.executar_comando(comando_delete)

    elif opcao == "2":  # CREATE
        nome_aluno_create = input("Digite o nome do novo aluno: ")
        matricula_create = input("Digite o matricula do novo aluno: ")
        comando_create = f'INSERT INTO alunos (nome, matricula) VALUES ("{nome_aluno_create}", {matricula_create})'
        operacoes.executar_comando(comando_create)

    elif opcao == "3":  # READ
        comando_read = f'SELECT * FROM alunos'
        resultado_read = operacoes.buscar_dados(comando_read)
        print(resultado_read)

    elif opcao == "4":  # UPDATE
        nome_aluno_update = input("Digite o nome do produto a ser atualizado: ")
        codigo_update = input("Digite o novo valor do produto: ")
        comando_update = f'UPDATE vendas SET valor = {codigo_update} WHERE nome_produto = "{nome_aluno_update}"'
        operacoes.executar_comando(comando_update)

    elif opcao == "5":  # Sair
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

conexao.fechar_conexao()

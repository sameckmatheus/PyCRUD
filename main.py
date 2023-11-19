from dml_lib import *

conexao = ConexaoBanco()
operacoes = OperacoesBanco(conexao.conexao, conexao.cursor)

while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada (1-5): ")

    if opcao == "1":  # DELETE
        matricula_aluno_delete = input("Digite a matricula do aluno a ser removido: ")
        comando_delete = f'DELETE FROM albinos WHERE matricula = "{matricula_aluno_delete}"'
        operacoes.executar_comando(comando_delete)

    elif opcao == "2":  # CREATE
        nome_aluno_create = input("Digite o nome do novo aluno: ")
        matricula_create = input("Digite a matricula do novo aluno: ")
        cpf_create = input("Digite o CPF do novo aluno: ")

        comando_create = (f'INSERT INTO alunos (nome, matricula, cpf) VALUES ('
                          f'"{nome_aluno_create}", '
                          f'{matricula_create}, '
                          f'"{cpf_create}")')
        operacoes.executar_comando(comando_create)

    elif opcao == "3":  # READ
        comando_read = f'SELECT * FROM alunos'
        resultado_read = operacoes.buscar_dados(comando_read)
        print(resultado_read)

    elif opcao == "4":  # UPDATE
        nome_aluno_update = input("Digite o nome do produto a ser atualizado: ")
        matricula_update = input("Digite a nova matricula do aluno: ")
        comando_update = f'UPDATE alunos SET matricula = {matricula_update} WHERE nome = "{nome_aluno_update}"'
        operacoes.executar_comando(comando_update)

    elif opcao == "5":  # Sair
        break

    else:
        print("pção inválida. Por favor, escolha uma opção válida.")
        continue

conexao.fechar_conexao()

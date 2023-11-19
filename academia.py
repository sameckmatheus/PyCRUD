import mysql.connector
from prettytable import PrettyTable

# Conectar ao servidor MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='003003',
    database='academia'
)

# Criar um cursor
cursor = conexao.cursor()


# Função para criar tabelas
def criar_tabelas():
    # Tabela alunos
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS `alunos` (
                    `matricula` int NOT NULL,
                    `nome` varchar(256) NOT NULL,
                    `cpf` char(11) NOT NULL,
                    PRIMARY KEY (`matricula`)
                )
            """)

    # Tabela funcionários
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS `funcionarios` (
                    `id_funcionario` int NOT NULL AUTO_INCREMENT,
                    `nome` varchar(256) NOT NULL,
                    `cpf` char(11) NOT NULL,
                    `departamento` int DEFAULT NULL,
                    `salario` decimal(8,2) DEFAULT NULL,
                    PRIMARY KEY (`id_funcionario`)
                )
            """)

    # Tabela modalidades
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS modalidades (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255),
                    descricao TEXT
                )
            """)

    # Tabela personal
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS personal (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255),
                    especialidade VARCHAR(255)
                )
            """)


# Função para inserir dados
def inserir_dados(tabela, dados):
    colunas = ', '.join(dados.keys())
    valores = ', '.join(['%s'] * len(dados))
    sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
    cursor.execute(sql, list(dados.values()))
    conexao.commit()
    print(f"Registro inserido com sucesso na tabela {tabela}.")


# Função para exibir dados
def exibir_dados(tabela):
    cursor.execute(f"SELECT * FROM {tabela}")
    registros = cursor.fetchall()

    if not registros:
        print(f"Nenhum registro encontrado na tabela {tabela}.")
        return

    colunas = [desc[0] for desc in cursor.description]

    tabela_formatada = PrettyTable(colunas)
    tabela_formatada.align = "l"  # Alinhamento à esquerda

    for registro in registros:
        tabela_formatada.add_row(registro)

    print(f"Dados da tabela {tabela}:")
    print(tabela_formatada)


def atualizar_dados(tabela, id_registro, novos_dados):
    sets = ', '.join([f"{coluna} = %s" for coluna in novos_dados.keys()])
    sql = f"UPDATE {tabela} SET {sets} WHERE id = %s"
    cursor.execute(sql, list(novos_dados.values()) + [id_registro])
    conexao.commit()
    print(f"Registro atualizado com sucesso na tabela {tabela}.")


def excluir_dados(tabela, id_registro):
    cursor.execute(f"DELETE FROM {tabela} WHERE id = %s", (id_registro,))
    conexao.commit()
    print(f"Registro excluído com sucesso na tabela {tabela}.")


def menu_interativo():
    criar_tabelas()

    while True:
        print("\n--- MENU ---")
        print("1. Selecionar tabela")
        print("2. Inserir dados")
        print("3. Exibir dados")
        print("4. Atualizar dados")
        print("5. Excluir dados")
        print("6. Sair")

        escolha_menu_principal = input("Escolha uma opção (1-6): ")

        if escolha_menu_principal == '6':
            break

        if escolha_menu_principal == '1':
            tabela_selecionada = input("Digite o nome da tabela: ")
            if tabela_selecionada not in {'alunos', 'funcionarios', 'modalidades', 'personal'}:
                print("Tabela inválida.")
                continue

            while True:
                print(f"\n--- Tabela: {tabela_selecionada.upper()} ---")
                print("1. Inserir dados")
                print("2. Exibir dados")
                print("3. Atualizar dados")
                print("4. Excluir dados")
                print("5. Voltar ao menu principal")

                escolha_tabela = input("Escolha uma opção (1-5): ")

                if escolha_tabela == '5':
                    break

                if escolha_tabela == '2' or escolha_tabela == '3' or escolha_tabela == '4':
                    exibir_dados(tabela_selecionada)

                dados_padrao = None if escolha_tabela == '2' else obter_dados_usuario(tabela_selecionada)

                if escolha_tabela == '1':
                    inserir_dados(tabela_selecionada, dados_padrao)
                elif escolha_tabela == '3':
                    id_registro = int(input("Digite o ID do registro a ser atualizado: "))
                    atualizar_dados(tabela_selecionada, id_registro, dados_padrao)
                elif escolha_tabela == '4':
                    id_registro = int(input("Digite o ID do registro a ser excluído: "))
                    excluir_dados(tabela_selecionada, id_registro)
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")


def obter_dados_usuario(tabela):
    dados = {}
    cursor.execute(f"DESCRIBE {tabela}")
    colunas = [coluna[0] for coluna in cursor.fetchall() if coluna[0] != 'id']

    for coluna in colunas:
        valor = input(f"Digite o valor para '{coluna}': ")
        dados[coluna] = valor

    return dados


if __name__ == "__main__":
    menu_interativo()

# Fechar cursor e conexão ao final
cursor.close()
conexao.close()

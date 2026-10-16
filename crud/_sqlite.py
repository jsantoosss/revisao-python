
import sqlite3

# 1. Conectar ao banco de dados (cria o arquivo 'banco_ads.db' automaticamente)
conexao = sqlite3.connect("banco_ads.db")
cursor = conexao.cursor()

# 2. Criar a tabela de alunos se ela ainda não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        curso TEXT NOT NULL
    )
""")
conexao.commit()

def cadastrar_aluno():
    print("\n--- CADASTRO DE ALUNO ---")
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso (ex: ADS, CC, SI): ")
    
    cursor.execute("INSERT INTO alunos (nome, curso) VALUES (?, ?)", (nome, curso))
    conexao.commit()
    print(f"✅ Aluno '{nome}' cadastrado com sucesso!")

def listar_alunos():
    print("\n--- LISTA DE ALUNOS CADASTRADOS ---")
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    
    if not alunos:
        print("Nenhum aluno encontrado no banco de dados.")
    else:
        for aluno in alunos:
            print(f"ID: {aluno} | Nome: {aluno} | Curso: {aluno}")

def excluir_aluno():
    listar_alunos()
    print("\n--- EXCLUIR ALUNO ---")
    id_aluno = input("Digite o ID do aluno que deseja excluir: ")
    
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
    conexao.commit()
    print(f"🗑️ Registro com ID {id_aluno} removido com sucesso!")

# Menu Principal do Sistema
while True:
    print("\n==========================================")
    print("    SISTEMA DE CADASTRO DE ALUNOS (SQL)   ")
    print("==========================================")
    print("1 - Cadastrar novo aluno")
    print("2 - Listar todos os alunos")
    print("3 - Excluir aluno")
    print("0 - Sair")
    
    opcao = input("Escolha uma opcao: ")
    
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        excluir_aluno()
    elif opcao == "0":
        print("\nSaindo do sistema e fechando conexao com o banco...")
        break
    else:
        print("Opcao invalida! Tente novamente.")

# Fechar conexao ao sair
conexao.close()
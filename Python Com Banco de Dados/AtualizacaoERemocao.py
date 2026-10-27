import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(dotenv_path="../DB.env")

# Criando a conexão
conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexao.cursor()
print("Conectado com sucesso!")

# Definição dos comandos
comando = '''DELETE FROM Pessoa WHERE cpf= 2000000009;'''
cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
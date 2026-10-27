import os
import mysql.connector
from modelo import Pessoa
from dotenv import load_dotenv


load_dotenv(dotenv_path="../../DB.env")

# Criando a conexão
conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexao.cursor()
print("Conectado com sucesso!")

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(2000000009, 'José', '1990-02-28', False)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) 
             VALUES (%s, %s, %s, %s);'''

cursor.execute(comando, (
    pessoa.cpf,
    pessoa.nome,
    pessoa.data_nascimento,
    pessoa.usa_oculos
))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
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

comando = '''CREATE TABLE Pessoa(
                cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf)
                ) '''

cursor.execute(comando)

#Efetivação do comando
conexao.commit()

#Fechamento das conexões
cursor.close()
conexao.close()
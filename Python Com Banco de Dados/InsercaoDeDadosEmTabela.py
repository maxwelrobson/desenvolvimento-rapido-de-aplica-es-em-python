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

comando = '''
            INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
            VALUES (123456789, 'João', '2000-01-31', 1);
            '''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
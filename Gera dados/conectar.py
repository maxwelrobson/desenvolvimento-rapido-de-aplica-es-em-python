import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(dotenv_path="../DBP.env")

#cria conexão
conexao = psycopg2.connect(
    host=os.getenv("HOST"),  # Troque "HOST" pelo nome exato que está no seu db.env
    port=os.getenv("PORTA"),  # Troque "PORTA" pelo nome exato
    database=os.getenv("BANCO"),  # Troque "BANCO" pelo nome exato
    user=os.getenv("USUARIO"),  # Troque "USUARIO" pelo nome exato
    password=os.getenv("SENHA")  # Troque "SENHA" pelo nome exato
)

print("Conectado com sucesso")
meu_cursor = conexao.cursor()
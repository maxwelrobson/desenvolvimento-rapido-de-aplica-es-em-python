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

comando1 = "DROP TABLE Veiculo"

cursor.execute(comando1)

comando2 = '''CREATE TABLE Veiculo(
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                motor REAL NOT NULL,
                propietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY(propietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id)
                )'''

cursor.execute(comando2)

conexao.commit()

cursor.close()
conexao.close()

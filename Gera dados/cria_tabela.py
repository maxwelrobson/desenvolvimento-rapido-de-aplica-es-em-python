from conectar import conexao, meu_cursor

#Criação da tabela
meu_cursor.execute('''
    CREATE TABLE PRODUTO (
        CODIGO SERIAL PRIMARY KEY,
        NOME VARCHAR(100) NOT NULL,
        PRECO NUMERIC(10, 2) NOT NULL
    );
''')

#just in case
conexao.commit()
print("Conectado com sucesso")
conexao.close()
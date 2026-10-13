import os

#Abrindo o arquivo no modo escrita
arquivo = open('exemplo.txt', 'w', encoding='utf-8')

# Exibindo os atributos do arquivo
print("Nome do arquivo:", arquivo.name)
print("Modo de abertura:", arquivo.mode)
print("Arquivo esta fechado?", arquivo.closed)

#Escrevendo no arquivo
arquivo.write("Ola, mundo!")
#exit()

#Fechando o arquivo
arquivo.close()

#Verificando se o arquivo está fechado
print("Arquivo  esta  fechado  agora?", arquivo.closed)

# Exibindo caminhos relativo e absoluto
#exit()
relpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)
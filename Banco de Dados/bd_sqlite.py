import sqlite3

#Cria uma nova conecção >> sera passado um arquivo para um banco de dados
conexao = sqlite3.connect('teste.sqlite')
#Cria um cursor que serve de iunterface para a utilização do sqlite atravez do Python
cursor = conexao.cursor()

#comando para criar uma tabela (caso a tabela não exista)
#elemento da tabela : (id integer PRIMARY KEY, nome text NOT NULL, email text NOT NULL);
sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY,
            nome text NOT NULL, email text NOT NULL);"""

#Povoar o banco de dados
nome = 'romuere'
email = 'romuere@gmail.com'

#executar o comando dentro da variavel
cursor.execute(sql)

#inserindo dados
for i in range(5):
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?,?)', (nome,email))

#recuperar dados do banco
cursor.execute('SELECT * from usuarios')
#mostrar os valores do banco de dados
for c in cursor:
    print(c)

#comandos de finalização
conexao.commit()
conexao.close()
import mysql.connector as mysql

conexao = mysql.connect(host = 'localhost',db='teste_4',user='root')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios_senha(id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL, senha VARCHAR(32) NOT NULL, email text NOT NULL);"""

nome = 'Jeands'
senha = 'jeands'
email = 'jeands@gmail.com'

cursor.execute(sql)
#cursor.execute('INSERT INTO usuarios_senha (nome, senha, email) VALUES (%s,MD5(%s),%s)',(nome,senha,email))

print(cursor.execute('SELECT * FROM usuarios_senha WHERE nome= %s AND senha=MD5(%s)',(nome,senha)))

for c in cursor:
    print(c)

conexao.commit()
conexao.close()
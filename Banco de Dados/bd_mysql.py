import mysql.connector as mysql

conexao = mysql.connect(host = 'localhost',db='teste_4',user='root')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios (id int AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL, email text NOT NULL);"""

nome = 'Jeanderson'
email = 'jeanderson@gmail.com'

cursor.execute(sql)
for i in range(3):
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (nome,email))

cursor.execute('SELECT * from usuarios')

for c in cursor:
    print(c)

conexao.commit()
conexao.close()
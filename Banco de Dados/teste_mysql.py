import mysql

banco = mysql.connector.connector(
    host = "localhost",
    user = "root",
    passwd=""
)

print(banco)
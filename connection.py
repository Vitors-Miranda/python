from mysql.connector import (connection)
db_conexao = connection.MySQLConnection(host="localhost", user="root", password="", database="inteiros")


#Criar cursor para executar as consultas
cursor = db_conexao.cursor()
cursor.execute("INSERT INTO inteiros VALUES (6)")
db_conexao.commit()
cursor.execute("SELECT * FROM inteiros")
data = cursor.fetchall()

for linha in data:
    print(linha)

db_conexao.close()
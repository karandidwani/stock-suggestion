import sqlite3

conn = sqlite3.connect('login.db')
cursor=conn.cursor()


cursor.execute('CREATE TABLE login (Username VARCHAR(20) UNIQUE, Email VARCHAR(20), Password VARCHAR(20))')

conn.commit()
conn.close()

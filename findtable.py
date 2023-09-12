import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

table_list = [a for a in cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
print(table_list)

connection.close()

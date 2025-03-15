import sqlite3

db_connection = sqlite3.connect("sqlite.db")
print(db_connection)

db_cursor = db_connection.cursor()
print(db_cursor)

query1 = "Select * from demo"
db_cursor.execute(query1)
print("Reading 2 rows")
row = db_cursor.fetchone()
print(row)
row = db_cursor.fetchone()
print(row)


print("Reading all rows")
rows = db_cursor.fetchall()
for r in rows:
    print(r)
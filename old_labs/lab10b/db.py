import sqlite3
from old_labs.lab10b import function

db_connection = sqlite3.connect("sqlite.db")
print(db_connection)

db_cursor = db_connection.cursor()
print(db_cursor)

query3 = "Insert into demo (Name, Hint) Values ('James', 'Jones')"
db_cursor.execute(query3)
db_connection.commit()

query2 = "Select * from demo"
# db_cursor.execute(query2)
# print("Reading 3 rows")
# row = db_cursor.fetchmany(3)
# print(row)
function.query_responder(db_cursor, "fetchmany", 3)


query1 = "Select * from demo"
db_cursor.execute(query1)
print("Reading 2 rows")
row = db_cursor.fetchone()
print(row)
row = db_cursor.fetchone()
print(row)

print("Reading all rows")
# rows = db_cursor.fetchall()
# for r in rows:
#    print(r)
function.query_responder(db_cursor, "fetchall")

id = int(input("Enter an ID: "))
query4 = "Select * from demo where ID > ?"
db_cursor.execute(query4, (id,))
function.query_responder(db_cursor, "fetchall")

# Close connections
db_cursor.close()
db_connection.close()








import sqlite3 as sql

con = sql.connect('db_web.db')
cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
sql = '''
    CREATE TABLE "projects" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" VARCHAR(100)
    )
'''
cur.execute(sql)
con.commit()
con.close()

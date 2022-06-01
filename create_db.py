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

# sql = '''
#     CREATE TABLE "tags" (
#         "id" INTEGER PRIMARY KEY AUTOINCREMENT,
#         "text" VARCHAR(100)
#     )
# '''

# sql = '''
#     DROP TABLE IF EXISTS "tags"
# '''

# sql = '''
#     CREATE TABLE "tags_to_projects" (
#         "tag_id" INTEGER PRIMARY KEY AUTOINCREMENT,
#         "project_id" INTEGER
#     )
# '''


cur.execute(sql)
con.commit()
con.close()

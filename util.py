from typing import List
import sqlite3 as sql


def fetch_rows(query: str) -> List:
    try:
        with sql.connect("db_web.db") as conn:
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute(query)
            return cur.fetchall()
    except Exception as error:
        raise sql.Error(error)


def execute_query(query: str) -> None:
    try:
        with sql.connect("db_web.db") as conn:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
    except Exception as error:
        raise sql.Error(error)

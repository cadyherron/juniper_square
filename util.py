from typing import List
import sqlite3 as sql
from werkzeug.exceptions import HTTPException


def fetch_rows(query: str) -> List:
    try:
        with sql.connect("db_web.db") as conn:
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute(query)
            return cur.fetchall()
    except Exception as error:
        raise sql.Error(error)


# TODO: handle exceptions in the same way, always
def execute_query(query: str) -> int:
    try:
        with sql.connect("db_web.db") as conn:
            cur = conn.cursor()
            cur.execute(query)
            last_row_id = cur.lastrowid
            conn.commit()
            return last_row_id
    except Exception as error:
        raise sql.Error(error)


def validate_fields_from_json(request_json, valid_fields) -> None:
    request_keys = set(request_json.keys())
    invalid_keys = [key for key in request_keys if key not in valid_fields]
    if invalid_keys:
        raise HTTPException(f"Unexpected keys: {invalid_keys}")
    missing_keys = [key for key in valid_fields if key not in request_keys]
    if missing_keys:
        raise HTTPException(f"Missing keys: {missing_keys}")

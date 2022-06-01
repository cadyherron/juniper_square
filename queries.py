INSERT_NEW_PROJECT = """
    INSERT INTO projects (name) VALUES ('{name}');
"""

SELECT_PROJECT_BY_ID = """
    SELECT * FROM projects WHERE id = {last_row_id}
"""

SELECT_ALL_PROJECTS = """
    SELECT * FROM projects;
"""
# juniper_square

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=development # optional
flask run
````

```bash
curl -d '{"name": "project1"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/create
curl -X GET http://127.0.0.1:5000/projects
curl -d '{"name": "project100"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/update_project/1
curl -X GET http://127.0.0.1:5000/delete_project/1
```
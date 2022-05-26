# juniper_square

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=development # optional
flask run


curl -d '{"name": "project1"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/create
```
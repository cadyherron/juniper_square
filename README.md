# juniper_square

Running locally:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=development # optional
flask run
````

```bash
curl --request GET 'http://127.0.0.1:5000/projects'

curl --request POST 'http://127.0.0.1:5000/projects' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "my cool project"}'


curl --request PUT 'http://127.0.0.1:5000/projects/2' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "my cool project2"}'


curl --request DELETE 'http://127.0.0.1:5000/projects/2' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "my cool project2"}'

```
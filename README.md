# juniper_square

```bash
python -m venv .venv
source .venv/bin/activate
brew install postgres # if you're on mac and don't have postgres installed
export PATH=/opt/homebrew/Cellar/postgresql/14.3/bin/:$PATH # if you get an error about pg_config
# follow these instructions to create a database: https://gist.github.com/phortuin/2fe698b6c741fd84357cec84219c6667
pip install -r requirements.txt
export FLASK_ENV=development # optional
flask run
```
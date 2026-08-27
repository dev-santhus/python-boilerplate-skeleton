# ${{ values.name }}

Minimal Django starter project for a Backstage scaffolder skeleton.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Run tests

```bash
python manage.py test
```

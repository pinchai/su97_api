
# Flask Database Migration Guide

In Flask, **migration** refers to managing changes to your database schema over time without having to manually drop and recreate tables.

This is typically done with:

- **Flask-Migrate** → A Flask extension that handles SQLAlchemy database migrations using **Alembic** under the hood.

---

## 1️⃣ Install Required Packages
```bash
pip install flask flask-sqlalchemy flask-migrate
```

---

## 2️⃣ Basic Project Structure
```
myapp/
│── app.py
│── models.py
│── migrations/  (auto-created later)
│── instance/
│── config.py
```

---

## 3️⃣ app.py (Flask + Migrate setup)
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from models import User

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 4️⃣ models.py (Define Models)
```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
```

---

## 5️⃣ Initialize Migrations
Run these commands in your terminal:
```bash
# Initialize migration folder
flask db init

# Create first migration file (detect changes in models)
flask db migrate -m "Initial migration"

# Apply migration to database
flask db upgrade
```

---

## 6️⃣ Making Changes
If you add a new field in `User`:
```python
email = db.Column(db.String(120), unique=True)
```
Then:
```bash
flask db migrate -m "Added email field to User"
flask db upgrade
```

---

## 7️⃣ Common Commands Summary
| Command | Description |
|---------|-------------|
| `flask db init` | Initialize migrations folder |
| `flask db migrate -m "msg"` | Create migration script |
| `flask db upgrade` | Apply migration |
| `flask db downgrade` | Revert migration |
| `flask db history` | Show migration history |
| `flask db current` | Show current migration version |

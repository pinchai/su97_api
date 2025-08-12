# Flask Session

In **Flask**, a **session** is a way to store data **per user** between requests.  
It works like a dictionary and is signed (not encrypted) using `SECRET_KEY` so that users cannot tamper with it.

---

## 1️⃣ How Sessions Work in Flask
- **Storage**: By default, Flask stores session data **in a cookie** on the client.
- **Security**: The session is signed with your app's `SECRET_KEY` so it cannot be modified without detection.
- **Persistence**: Sessions last until the browser is closed, unless `session.permanent = True`.

---

## 2️⃣ Basic Setup

```python
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session security

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username  # store in session
        session.permanent = True        # session lasts longer
        return redirect(url_for("profile"))
    return '''
        <form method="post">
            Username: <input name="username">
            <input type="submit">
        </form>
    '''

@app.route("/profile")
def profile():
    if "username" in session:
        return f"Hello {session['username']}!"
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)  # remove from session
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 3️⃣ Common Session Methods
| Method | Description |
|--------|-------------|
| `session['key'] = value` | Store data |
| `session.get('key')` | Get data safely |
| `session.pop('key', None)` | Remove key |
| `'key' in session` | Check if exists |
| `session.clear()` | Clear all session data |

---

## 4️⃣ Permanent Sessions  
By default, sessions expire when the browser closes.  
You can make them permanent:

```python
from datetime import timedelta
app.permanent_session_lifetime = timedelta(days=7)  # lasts 7 days
session.permanent = True
```

---

## 5️⃣ Accessing Session in Templates
```jinja
{% if 'username' in session %}
  <p>Welcome {{ session['username'] }}</p>
{% else %}
  <p>Please log in.</p>
{% endif %}
```

---

## 6️⃣ Using Server-Side Sessions (Optional)
If you don’t want session data in cookies, you can store them in Redis, database, or filesystem using **Flask-Session**:
```bash
pip install flask-session
```

```python
from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
```

# Flask Cookies

In **Flask**, cookies are a way to store data on the **client-side** that can be sent back to the server with each request.  
Unlike **sessions** (which are signed with a secret key), cookies are just plain text stored in the browser.

---

## 1️⃣ How Cookies Work in Flask
- **Location**: Stored in the user's browser.
- **Lifetime**: Can be set to expire at a certain date/time or persist until the browser is closed.
- **Security**: Cookies can be read/edited by the user unless secured with flags like `HttpOnly` and `Secure`.

---

## 2️⃣ Setting a Cookie
You can use Flask's `make_response()` to attach a cookie to a response.

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/set-cookie")
def set_cookie():
    resp = make_response("Cookie has been set!")
    resp.set_cookie("username", "chai", max_age=60*60*24)  # lasts 1 day
    return resp
```

**Parameters of `set_cookie`:**
- `key`: Cookie name
- `value`: Cookie value
- `max_age`: Lifetime in seconds
- `expires`: Datetime object or string
- `path`: Path for which the cookie is valid
- `domain`: Domain name
- `secure`: If `True`, only sent over HTTPS
- `httponly`: If `True`, not accessible via JavaScript

---

## 3️⃣ Getting a Cookie
```python
@app.route("/get-cookie")
def get_cookie():
    username = request.cookies.get("username")
    return f"Username stored in cookie: {username}"
```

---

## 4️⃣ Deleting a Cookie
```python
@app.route("/delete-cookie")
def delete_cookie():
    resp = make_response("Cookie deleted!")
    resp.delete_cookie("username")
    return resp
```

---

## 5️⃣ Example with Login
```python
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        resp = make_response(f"Welcome {username}")
        resp.set_cookie("username", username, max_age=60*60*24)
        return resp
    return '''
        <form method="post">
            Username: <input name="username">
            <input type="submit">
        </form>
    '''

@app.route("/profile")
def profile():
    username = request.cookies.get("username")
    if username:
        return f"Hello {username}!"
    return "You are not logged in."
```

---

## 6️⃣ Security Tips for Cookies
- Use **`httponly=True`** to prevent JavaScript access.
- Use **`secure=True`** for HTTPS-only cookies.
- Avoid storing sensitive data directly in cookies; store an ID and keep data server-side.
- Consider **signing** cookies if you need integrity checks.

---

## 7️⃣ Accessing Cookies in Templates
```jinja
<p>Cookie Username: {{ request.cookies.get('username') }}</p>
```

---

**Cookies are great for small bits of data that don’t need to be kept secret**, but for secure and tamper-proof storage, use **Flask sessions**.

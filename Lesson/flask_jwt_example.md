# Flask JWT Example

## Install Dependencies

```bash
pip install Flask flask-jwt-extended
```

---

## Example Code

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-me"  # use env var in real apps
jwt = JWTManager(app)

# Fake users (demo only)
USERS = {
    "admin@example.com": {"password": "123456", "id": 1},
    "user@example.com":  {"password": "123456", "id": 2},
}

@app.post("/login")
def login():
    data = request.get_json() or {}
    email = (data.get("email") or "").lower().strip()
    pw = data.get("password") or ""
    u = USERS.get(email)
    if not u or u["password"] != pw:
        return jsonify(error="Invalid credentials"), 401

    token = create_access_token(identity=u["id"])
    return jsonify(access_token=token)

@app.get("/me")
@jwt_required()
def me():
    user_id = get_jwt_identity()
    return jsonify(message="You are authenticated!", user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## API Endpoints

### `POST /login`
Authenticate a user and return a JWT access token.

**Request JSON Example:**
```json
{
    "email": "admin@example.com",
    "password": "123456"
}
```

**Response JSON Example:**
```json
{
    "access_token": "your.jwt.token"
}
```

### `GET /me`
Protected route that requires a valid JWT.

**Request Header Example:**
```
Authorization: Bearer your.jwt.token
```

**Response JSON Example:**
```json
{
    "message": "You are authenticated!",
    "user_id": 1
}
```

from app import app, db
from flask import request
from sqlalchemy import text


@app.get('/user/list')
def get_all():
    return get_all_user()


@app.get('/user/get-by-id/<int:user_id>')
def get_by_id(user_id):
    # assert False, user_id
    return get_user_by_id(user_id)


@app.post('/user/create')
def create_user():
    user = request.get_json()
    user_name = user.get('name')
    profile = user.get('profile')

    if not user_name:
        return {'message': 'name not found'}, 404

    sql = text("insert into user values (null, :name, :profile)")
    user = db.session.execute(
        sql,
        {
            'name': user_name,
            'profile': profile,
        }
    )
    db.session.commit()
    user_id = user.lastrowid
    return get_user_by_id(user_id)


def get_all_user():
    res = db.session.execute(text('select * from user')).fetchall()
    rows = [dict(row._mapping) for row in res]
    return rows


def get_user_by_id(user_id):
    result = db.session.execute(
        text('select * from user where id = :user_id'),
        {
            'user_id': user_id
        }
    ).fetchone()
    if not result:
        return {
            "message": "user not found"
        }
    row = dict(result._mapping)
    return row

from flask import Blueprint, render_template, request, make_response, session
from db import db
from secrets import token_hex
from functools import wraps

web = Blueprint("web", __name__)

class User(db.Model):
    user_id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pwd = db.Column(db.String(40), nullable=False)
    token = db.Column(db.String(64))

    def __str__(self):
        return f"{self.name}"

def auth(func):
    @wraps(func)
    def inner(*args):
        user_id = session.get("id")
        user_token = session.get("token")
        if user_id and user_token:
            user_tkn = db.session.query(User.token).filter(User.user_id==user_id)[0][0]
            if user_tkn == user_token:
                return func(*args)
    return inner

@web.route("/login")
def home():
    users = User.query.all()
    return render_template("index.html", user=users[0].name, users=users)

@web.route("/test", methods=["POST"])
def test():
    print(request.form)
    user_name = dict(request.form).get("name")
    user_pwd = db.session.query(User.pwd, User.user_id).filter(User.name==user_name)
    if user_pwd[0][0] == request.form["pwd"]:
        session["id"] = user_pwd[0][1]
        user_token = token_hex()
        session["token"] = user_token
        db.engine.execute(f"UPDATE user SET token='{user_token}' WHERE user_id='{user_pwd[0][1]}'")
        db.session.commit()
        return "Usuario logueado correctamente"
    else:
        return "BAD LOGIN"

@web.route("/private")
@auth
def test_cookies():
    return "cookie"

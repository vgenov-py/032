from flask import Blueprint, render_template, request
from db import db
web = Blueprint("web", __name__)

class User(db.Model):
    user_id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pwd = db.Column(db.String(40), nullable=False)
    token = db.Column(db.String(64))

    def __str__(self):
        return f"{self.name}"

@web.route("/login")
def home():
    users = User.query.all()
    return render_template("index.html", user=users[0].name, users=users)

@web.route("/test", methods=["POST"])
def test():
    print(request.form)
    return "TEST"

@web.route("/about")
def about():
    return "about page"
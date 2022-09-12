from flask import Blueprint, render_template, request, session, url_for, redirect
from views.byr.models import db, Apartment, Roomie, Invoice
from secrets import token_urlsafe
import datetime as dt
from auth import Auth

byr = Blueprint("byr", __name__)
test_auth = Auth(session, Roomie, "byr.t_login", "byr.home",  request, db) 

@byr.route("/", methods=["GET", "POST"])
@test_auth.auth
def home():
    return render_template("base.html")

@byr.route("/login", methods=["GET", "POST"])
@test_auth.check
def t_login():
    return render_template("login.html")

@byr.route("/test")
def t_test():
    print(test_auth.session)
    # to_add = Roomie.add_roomie(
    #     "test","test@email.com", "1234", dt.date.fromisoformat("2022-01-01"), dt.date.fromisoformat("2022-01-31")
    #     )
    # db.session.add(to_add)
    # db.session.commit()
    return "Testing"
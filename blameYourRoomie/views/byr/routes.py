from flask import Blueprint, render_template, request, session, redirect, url_for
from views.byr.models import db, Apartment, Roomie, Invoice
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

@byr.route("/apartment", methods=["GET", "POST"])
@test_auth.auth
def t_apartment():
    if request.method == "POST":
        form_address = request.form["address"]
        form_rooms = request.form["rooms"]
        to_add_apartment = Apartment.add_apartment(form_address, form_rooms)
        to_upd_roomie = Roomie.query.filter_by(id=session["id"]).first()
        to_upd_roomie.apartment_id = to_add_apartment.id
        db.session.add(to_add_apartment)
        db.session.add(to_upd_roomie)
        db.session.commit()
        return redirect(url_for("byr.home"))

    return render_template("apartment.html")

@byr.route("/test")
def t_test():
    print(test_auth.session)
    # to_add = Roomie.add_roomie(
    #     "test","test@email.com", "1234", dt.date.fromisoformat("2022-01-01"), dt.date.fromisoformat("2022-01-31")
    #     )
    # db.session.add(to_add)
    # db.session.commit()
    return "Testing"
from flask import Blueprint, render_template, request, session, redirect, url_for
from views.byr.models import db, Apartment, Roomie, Invoice
import datetime as dt
from auth import Auth

byr = Blueprint("byr", __name__)
test_auth = Auth(session, Roomie, "byr.t_login", "byr.home",  request, db) 

@byr.route("/", methods=["GET", "POST"])
@test_auth.auth
def home():
    if session.get("apartment_id"):
        return redirect(url_for("byr.t_apartment"))
    return render_template("base.html")

@byr.route("/login", methods=["GET", "POST"])
@test_auth.check
def t_login():
    return render_template("login.html")

@byr.route("/apartment", methods=["GET", "POST"])
@test_auth.auth
def t_apartment():
    apartment = Apartment.query.filter_by(id=session.get("apartment_id")).first()
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

    return render_template("apartment.html", apartment=apartment if apartment else None)

@byr.route("/roomies", methods=["GET", "POST"])
@test_auth.auth
def t_roomies():
    if request.method == "POST":
        form = request.form
        new_roomie = Roomie.add_roomie(
            form["name"], 
            form["email"], 
            form["email"], 
            dt.date.fromisoformat(form["date_start"]),
            dt.date.fromisoformat(form["date_end"]) if form["date_end"] else None,
            apartment_id=session["apartment_id"]
            )

        db.session.add(new_roomie)
        db.session.commit()

    apartment = Apartment.query.filter_by(id=session.get("apartment_id")).first()
    roomies = apartment.roomies
    return render_template("roomies.html", roomies=roomies)

@byr.route("/test")
def t_test():
    roomies = Roomie.query.all()
    print(roomies)
    # print(test_auth.session)
    # to_add = Roomie.add_roomie(
    #     "test3","test3@email.com", "1234", dt.date.fromisoformat("2022-01-01"), None
    #     )
    # db.session.add(to_add)
    # db.session.commit()
    return "Testing"

@byr.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('byr.t_login'))
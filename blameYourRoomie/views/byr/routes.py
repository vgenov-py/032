from flask import Blueprint, render_template, request, session, redirect, url_for, make_response
from views.byr.models import db, Apartment, Roomie, Invoice
import datetime as dt
from auth import Auth
import requests as req
from werkzeug.utils import secure_filename
import os

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
        session["apartment_id"] = to_add_apartment.id
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

    roomies = list(map(lambda roomie: roomie.public(), apartment.roomies))
    roomies_checkin = list(filter(lambda roomie: not roomie["date_end"], roomies))
    return render_template("roomies.html", elements=roomies, roomies_checkin=roomies_checkin, button_text="Pay!")

# @test_auth.auth
@byr.route("/roomies/<roomie_id>", methods=["GET", "POST"])
def t_debts(roomie_id):
    roomie = Roomie.query.filter_by(id=roomie_id).first()
    if request.method == "POST":
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        return {"success": True}
    return render_template(
        "debts.html", roomie=roomie.public(), 
        elements=list(map(lambda debt: debt.public(),roomie.debts)) if len(roomie.debts) >= 0 else None, 
        button_text="Pay!")


@byr.route("/invoices", methods=["GET", "POST"])
@test_auth.auth
def t_invoices():
    apartment = Apartment.query.filter_by(id=session["apartment_id"]).first()
    if request.method == "POST":
        form = dict(request.form)
        to_add = Invoice.add_invoice(session["apartment_id"], int(form["total"]), form["service"], dt.date.fromisoformat(form["date_start"]), dt.date.fromisoformat(form["date_end"]), form["comment"] if form.get("comment") else None)
        for roomie in apartment.roomies:
            roomie.calculate_debt(apartment.rooms, to_add)
        db.session.add(to_add)
        db.session.commit()
    invoices = list(map(lambda invoice: invoice.public(), apartment.invoices))
    return render_template("invoices.html", elements=invoices, button_text="Pay!")


@byr.route("/test")
def t_test():
    data = {"success": True}
    data = make_response(data)
    data.set_cookie("name", "test1")
    return data
    # roomies = Roomie.query.all()
    # print(roomies)
    # # print(test_auth.session)
    # to_add = Roomie.add_roomie("test4", "test4@email.com", "1234", dt.date.fromisoformat("2022-01-01"), None)
    # db.session.add(to_add)
    # db.session.commit()
    # roomie = Roomie.query.filter_by(name="test").first()
    # invoice = Invoice.query.first()
    # roomie.calculate_debt(3, invoice)
    return render_template("test.html")

@byr.route('/logout')
def logout():
    session.clear()
    res = make_response(redirect(url_for('byr.t_login')))
    res.delete_cookie("name")
    return res

@byr.route("/<e>")
def page_404(e):
    return redirect(url_for('byr.t_login'))
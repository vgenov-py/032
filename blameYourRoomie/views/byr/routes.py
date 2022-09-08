from flask import Blueprint, render_template, request
from views.byr.models import db, Apartment, Roomie, Invoice

byr = Blueprint("byr", __name__)

@byr.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
    return render_template("base.html")

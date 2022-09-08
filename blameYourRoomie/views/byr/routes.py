from flask import Blueprint, render_template, request, session, url_for, redirect
from views.byr.models import db, Apartment, Roomie, Invoice
from secrets import token_urlsafe

byr = Blueprint("byr", __name__)

@byr.route("/", methods=["GET", "POST"])
def home():
    if session.get("id") or session.get("token"):
        user = Roomie.query.filter_by(id=session["id"]).first()
        if user:
            if user.token == session["token"]:    
                return render_template("base.html")
    return redirect(url_for("byr.t_login"))

@byr.route("/login", methods=["GET", "POST"])
def t_login():
    if request.method == "POST":
        print(request.form)
        user_email = request.form["email"]
        user_pwd = request.form["pwd"]

        # comprobar credenciales
        # agregar token a la session y actualizar el token del user
        user = Roomie.query.filter_by(email=user_email).first() # TODO agregar constrain unique
        if user:
            if user.pwd == user_pwd:
                user.token = token_urlsafe()
                session["id"] = user.id
                session["token"] = user.token
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("byr.home"))

    return render_template("login.html")

@byr.route("/test")
def t_test():
    # to_update = Roomie.query.filter_by(id="1").first()
    # to_update.email = "test@email.com"
    # db.session.add(to_update)
    # db.session.commit()
    return "Testing"
from flask import redirect, url_for, make_response
from functools import wraps
from secrets import token_urlsafe
from hashlib import sha1
import werkzeug

class Auth:
    def __init__(self, session: werkzeug.local.LocalProxy, users, redirect_url, home_url,request, db) -> None:
        '''
        Session should be flask_session object
        '''
        self.session = session
        self.users = users
        self.redirect_url = redirect_url
        self.home_url = home_url
        self.request = request
        self.db = db

    def auth(self, func):
        @wraps(func)

        def inner(*args):
            session_id = self.session.get("id")
            session_token = self.session.get("token")
            if session_id or session_token:
                user = self.users.query.filter_by(id=session_id).first()
                if user:
                    if user.token == session_token:    
                        return func(*args)
            return redirect(url_for(self.redirect_url))
        return inner

    def check(self, func): # SESSION LOG OUT
        @wraps(func)
        def inner(*args):
            res = make_response(func(*args))
            if self.request.method == "POST":
                user_email = self.request.form["email"]
                user_pwd = self.request.form["pwd"]
                user = self.users.query.filter_by(email=user_email).first() 
                if user:
                    if user.pwd == user_pwd:
                        user.token = token_urlsafe()
                        self.session["id"] = user.id
                        self.session["token"] = user.token
                        self.session["apartment_id"] = user.apartment_id if user.apartment_id else None
                        self.db.session.add(user)   
                        self.db.session.commit()
                        res = make_response(redirect(url_for(self.home_url)))
                        res.set_cookie("name", user.name)
                        return res
            return res
        return inner

from flask import Flask
from views.api.routes import api
from views.web.routes import web
from db import db
import os

def create_app():
    app = Flask(__name__)
    app.config["SECRET"] = "KUGA"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(web)
    db.init_app(app)
    return app

def set_db():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    app = create_app()
    if not os.path.isfile("test.db"):
        set_db()
    app.run(debug=True)
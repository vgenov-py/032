from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/api/book")
def api_book():
    return "search book"

@api.route("/api/genre")
def api_genre():
    return "search genre"
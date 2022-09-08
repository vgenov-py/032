from db import db

class Apartment(db.Model):
    __tablename__ = "apartments"
    id = db.Column(db.String(32), primary_key=True)
    address = db.Column(db.String(100))
    rooms = db.Column(db.Integer)
    roomies = db.relationship('Roomie', backref='apartments', lazy=True)
    invoices = db.relationship('Invoice', backref='apartments', lazy=True)


class Roomie(db.Model):
    __tablename__ = "roomies"
    id = db.Column(db.String(32), primary_key=True)
    apartment_id = db.Column(db.String(32), db.ForeignKey('apartments.id'), nullable=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    pwd = db.Column(db.String(40))
    token = db.Column(db.String(43), nullable=True)
    is_keeper = db.Column(db.Boolean)
    debt = db.Column(db.Float)

class Invoice(db.Model):
    __tablename__ = "invoices"
    id = db.Column(db.String(32), primary_key=True)
    apartment_id = db.Column(db.String(32), db.ForeignKey('apartments.id'), nullable=True)
    total = db.Column(db.Float)
    service = db.Column(db.String(40))
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    comment = db.Column(db.String(200), nullable=True)





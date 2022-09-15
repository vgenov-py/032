from db import db
from uuid import uuid4


class Apartment(db.Model):
    __tablename__ = "apartments"
    id = db.Column(db.String(32), primary_key=True)
    address = db.Column(db.String(100))
    rooms = db.Column(db.Integer)
    roomies = db.relationship('Roomie', backref='apartments', lazy=True)
    invoices = db.relationship('Invoice', backref='apartments', lazy=True)

    @staticmethod
    def gen_id():
        return uuid4().hex

    def add_apartment(address: str, rooms: int):  
        return Apartment(id=Apartment.gen_id(), address=address, rooms=rooms)

class Roomie(db.Model):
    __tablename__ = "roomies"
    id = db.Column(db.String(32), primary_key=True)
    apartment_id = db.Column(db.String(32), db.ForeignKey('apartments.id'), nullable=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(40))
    token = db.Column(db.String(43), nullable=True)
    is_keeper = db.Column(db.Boolean)
    debt = db.Column(db.Float)
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)

    def add_roomie(name, email, pwd, date_start, date_end,is_keeper=False, apartment_id = None):
        '''
        debt=0
        default is_keeper=False
        '''
        user_id = uuid4().hex
        debt = 0
        return Roomie(id=user_id, name=name, apartment_id = apartment_id, email=email, pwd=pwd, is_keeper=is_keeper, debt=debt, date_start=date_start, date_end=date_end)

    def __repr__(self):
        return f"Roomie({self.name})"
    
    def __str__(self):
        return f"Roomie({self.name})"

class Invoice(db.Model):
    __tablename__ = "invoices"
    id = db.Column(db.String(32), primary_key=True)
    apartment_id = db.Column(db.String(32), db.ForeignKey('apartments.id'), nullable=True)
    total = db.Column(db.Float)
    service = db.Column(db.String(40))
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    comment = db.Column(db.String(200), nullable=True)
    is_paid = db.Column(db.Boolean)






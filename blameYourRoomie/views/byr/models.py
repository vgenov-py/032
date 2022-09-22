from ast import In
from copy import deepcopy
from db import db
from uuid import uuid4
import datetime as dt

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


class Invoice(db.Model):
    __tablename__ = "invoices"
    id = db.Column(db.String(32), primary_key=True)
    apartment_id = db.Column(db.String(32), db.ForeignKey('apartments.id'))
    total = db.Column(db.Float)
    service = db.Column(db.String(40))
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    comment = db.Column(db.String(200), nullable=True)
    is_paid = db.Column(db.Boolean)
    debts = db.relationship('Debt', backref='invoices', lazy=True)

    def add_invoice(apartment_id:str, total:float or int, service:str, date_start, date_end, comment:str=None):
        '''
        apartment_id - total - service - date_start - date_end - comment
        '''
        invoice_id = uuid4().hex
        return Invoice(id=invoice_id, apartment_id=apartment_id, total=total, service=service, date_start=date_start, date_end=date_end, comment=comment, is_paid=False)

    
    def public(self):
        invoice = {
            "service": self.service,
            "total": round(self.total, 2),
            "date_start": self.date_start,
            "date_end": self.date_end,
            "is_paid": self.is_paid,
            "comment": self.comment,
            "id": self.id
        }
        return invoice



class Debt(db.Model):
    __tablename__ = "debts"
    id = db.Column(db.String(32), primary_key=True)
    invoice_id = db.Column(db.String(32), db.ForeignKey('invoices.id'))
    roomie_id = db.Column(db.String(32), db.ForeignKey('roomies.id'))
    total = db.Column(db.Float)
    is_paid = db.Column(db.Boolean)

    @staticmethod
    def gen_id():
        return uuid4().hex

    def __init__(self, invoice_id: str, roomie_id: str,total: float):
        self.id = self.gen_id()
        self.invoice_id = invoice_id
        self.roomie_id = roomie_id
        self.total = total
        self.is_paid = False

    def add_debt(invoice_id: str, roomie_id: str,total: float):
        return Debt(id=Debt.gen_id(), invoice_id=invoice_id, roomie_id=roomie_id, total=total, is_paid=False)
    
    @property
    def invoice(self):
        return Invoice.query.filter_by(id=self.invoice_id).first()

    def public(self):
        result = {
            "service": self.invoice.service,
            "total": round(self.total, 2),
            "is_paid": self.is_paid,
            "id": self.id
        }
        return result

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
    debts = db.relationship('Debt', backref='roomies', lazy=True)

    def public(self):
        roomie = {
            "name": self.name,
            "email": self.email,
            "debt": round(self.debt, 2),
            "date_start": self.date_start,
            "date_end": self.date_end,
            "id": self.id
        }
        return roomie

    def add_roomie(name, email, pwd, date_start, date_end,is_keeper=False, apartment_id = None):
        '''
        debt=0
        default is_keeper=False
        '''
        user_id = uuid4().hex
        debt = 0
        return Roomie(id=user_id, name=name, apartment_id = apartment_id, email=email, pwd=pwd, is_keeper=is_keeper, debt=debt, date_start=date_start, date_end=date_end)

    def calculate_debt(self,rooms:int, invoice: Invoice):
        per_day = (invoice.total / rooms) / (invoice.date_end - invoice.date_start).days
        roomie_date_end = dt.datetime.now() if not self.date_end else self.date_end
        roomie_date_end = dt.date(roomie_date_end.year, roomie_date_end.month, roomie_date_end.day)
        i_l = invoice.date_start if invoice.date_start >= self.date_start else self.date_start
        s_l = invoice.date_end if invoice.date_end <= roomie_date_end else roomie_date_end
        if i_l <= s_l:
            interval = (s_l - i_l).days
            debt = Debt.add_debt(invoice.id, self.id, interval * per_day)
            db.session.add(debt)
            self.debt += debt.total
            db.session.add(self)

    def __repr__(self):
        return f"Roomie({self.name})"
    
    def __str__(self):
        return f"Roomie({self.name})"
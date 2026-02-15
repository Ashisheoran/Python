from flask_sqlalchemy import SQLAlchemy
from enum import Enum as PyEnum

db = SQLAlchemy()

class MemberType(PyEnum):
    STAFF = "Staff"
    PREMIUM = "Premium"
    REGULAR = "Regular"

class LibraryMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    member_type = db.Column(db.Enum(MemberType), nullable=False)

class LibraryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    creator = db.Column(db.String(100), nullable=False)
    copies = db.Column(db.Integer, default=1)
    item_type = db.Column(db.String(50))  # Book / Newspaper
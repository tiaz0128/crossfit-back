from datetime import datetime
from app import db


class Crossfit_box(db.Model):
    __tablename__ = 'crossfit_box'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    tel = db.Column(db.String(64))
    address = db.Column(db.Text)
    owner = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=True)
    bizno = db.Column(db.String(64))
    url = db.Column(db.String(256))
    upd_dt = db.Column(db.DateTime(), nullable=False)
    ins_dt = db.Column(db.DateTime(), nullable=False)

    # ownerShip = db.relationship("Member", backref=db.backref('owner_set'))

    def __init__(self, name, tel, address):
        self.name = name
        self.tel = tel
        self.address = address
        self.upd_dt = datetime.now()
        self.ins_dt = datetime.now()

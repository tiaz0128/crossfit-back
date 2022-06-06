from datetime import datetime
from app import db


class Box(db.Model):
    __tablename__ = "box"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    tel = db.Column(db.String(64))
    address = db.Column(db.String(500))
    owner = db.Column(db.String(128), nullable=True)
    biz_no = db.Column(db.String(64))
    url = db.Column(db.String(256))
    upd_dt = db.Column(db.DateTime(), nullable=False)
    ins_dt = db.Column(db.DateTime(), nullable=False)

    def __init__(self, name, tel, address):
        self.name = name
        self.tel = tel
        self.address = address
        self.upd_dt = datetime.now()
        self.ins_dt = datetime.now()

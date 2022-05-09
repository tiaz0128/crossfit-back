from datetime import datetime
from app import db


class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    nick_name = db.Column(db.String(64))
    info_y = db.Column(db.String(2), default='Y', nullable=False)
    ur_box = db.Column(db.Integer)
    upd_dt = db.Column(db.DateTime(), nullable=False)
    ins_dt = db.Column(db.DateTime(), nullable=False)

    my_box = db.relationship("Crossfit_box", backref=db.backref('member_set'))

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
        self.info_yn = 'Y'
        self.upd_dt = datetime.now()
        self.ins_dt = datetime.now()
    
    def __repr__(self) -> str:
        return "TEST"
    
    def get_member(self) -> dict:
        return {"id": self.id, "name": self.name}
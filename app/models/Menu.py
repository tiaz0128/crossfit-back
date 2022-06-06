from datetime import datetime
from app import db


class Menu(db.Model):
    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    menu_title = db.Column(db.String(128))
    upd_dt = db.Column(db.DateTime(), nullable=False)
    ins_dt = db.Column(db.DateTime(), nullable=False)

    def __init__(self, parent_id, menu_title):
        self.parent_id = parent_id
        self.menu_title = menu_title
        self.upd_dt = datetime.now()
        self.ins_dt = datetime.now()

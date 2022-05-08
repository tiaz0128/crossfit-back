from app import db


class Member(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    phone = db.Column(db.Text)
    info_y = db.Column(db.String(2), default='Y', nullable=False)

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
        self.info_y = 'Y'

    def __repr__(self):
        return f"test {self.name} {self.phone} {self.age}"

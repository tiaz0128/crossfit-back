# from pprint import pprint
# from flask import jsonify

from app import db
from datetime import datetime

from marshmallow import Schema, fields


class MemberSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    age = fields.Int()
    phone = fields.Str()
    nick_name = fields.Str()
    info_y = fields.Str()
    ur_box = fields.Int()
    upd_dt = fields.Str()
    ins_dt = fields.Str()


class Member(db.Model):
    __tablename__ = "member"

    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    nick_name = db.Column(db.String(64))
    info_y = db.Column(db.String(2), default="Y", nullable=False)
    ur_box = db.Column(db.Integer)
    upd_dt = db.Column(db.DateTime(), nullable=False)
    ins_dt = db.Column(db.DateTime(), nullable=False)

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
        self.info_yn = "Y"
        self.upd_dt = datetime.now()
        self.ins_dt = datetime.now()

    def get_member(id):
        member = Member.query.filter_by(id=id).first()

        schema = MemberSchema(only=("name", "age"))
        return schema.dump(member)

    def get_members(page):
        members = Member.query.order_by(Member.id)
        members = members.paginate(page, per_page=10)

        schema = MemberSchema(only=("name", "age"), many=True)
        result = schema.dump(members.items)

        return {"members": result}

    def get_filter_members(filter):
        q = Member.query

        if filter.get("name"):
            q = Member.query.filter_by(name=filter["name"])
        if filter.get("age"):
            q = q.filter(Member.age.in_(filter["age"]))

        members = q.order_by(Member.id)
        members = members.paginate(filter["page"], per_page=10)

        schema = MemberSchema(only=("name", "age"), many=True)
        result = schema.dump(members.items)

        return {"members": result}

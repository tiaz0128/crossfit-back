from flask import Blueprint, request
from app.models.Member import Member
from app import db

bp = Blueprint("member", __name__, url_prefix="/member")


@bp.route("/<id>", methods=["GET"])
def get_member(id):
    return Member.get_member(id)

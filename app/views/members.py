from flask import Blueprint, request
from app.models.Member import Member
from app import db

bp = Blueprint("members", __name__, url_prefix="/members")


@bp.route("/")
def members():
    page = request.args.get("page", 1, type=int)

    return Member.get_members(page), 200


@bp.route("/search", methods=["GET"])
def get_filter_member():
    filter = request.args.to_dict()
    filter["age"] = request.args.getlist("age")
    filter.setdefault("page", 1)

    return Member.get_filter_members(filter)

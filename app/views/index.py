from flask import Blueprint
from app import db
from app.models.Crossfit_box import Crossfit_box
from app.models.Member import Member

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'Hello Flask'


@bp.route('/boxInfo/')
def box_info():
    box = Crossfit_box.query.get(1)
    print(box)
    return {"boxName": box.name}


@bp.route("/members/")
def members():
    members = db.session.query(Member).all()

    return {"members": [m.get_member() for m in members]}

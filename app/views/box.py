from flask import Blueprint
from app.models.Box import Box

bp = Blueprint("box", __name__, url_prefix="/box")


@bp.route("/")
@bp.route("/box")
def box_info():
    box = Box.query.get(1)
    print(box)
    return {"boxName": box.name}

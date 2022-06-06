from flask import Blueprint, jsonify, request

# from app import csrf
from app.forms.text import QuestionForm
from werkzeug.datastructures import ImmutableMultiDict
from flask_wtf.csrf import generate_csrf


bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    form = QuestionForm()
    csrf_token = form.csrf_token._value()
    return jsonify({"csrf_token": csrf_token})


# @bp.route("/", methods=["POST"])
# def create():
#     reg_json = request.get_json()
#     form_input = ImmutableMultiDict(reg_json)
#     form = QuestionForm(form_input, meta={"csrf": False})

#     if request.method == "POST" and form.validate():
#         print(form.subject, form.content)
#         return {"res": "ok"}, 200

#     return {"res": "false"}, 400

# from flask import Blueprint, jsonify

# bp = Blueprint("index", __name__, url_prefix="/")


# @bp.route("/", methods=["GET"])
# def index():
#     return jsonify({"csrf_token": "test"})


# @bp.route("/", methods=["POST"])
# def create():
#     reg_json = request.get_json()
#     form_input = ImmutableMultiDict(reg_json)
#     form = QuestionForm(form_input, meta={"csrf": False})

#     if request.method == "POST" and form.validate():
#         print(form.subject, form.content)
#         return {"res": "ok"}, 200

#     return {"res": "false"}, 400

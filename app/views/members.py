from flask import request
from flask_restx import Resource, fields, Namespace
from app.models.Member import Member
from app import api

ns = Namespace("members", description="Members operations")


member_model = api.model(
    "Member",
    {
        "id": fields.String(),
        "name": fields.String(),
        "age": fields.Integer(),
    },
)


@ns.route("/")
class Members(Resource):
    @api.marshal_list_with(member_model, code=200, envelope="members")
    def get(self):
        page = request.args.get("page", 1, type=int)
        return Member.get_members(page)

    def post(self):
        pass


@ns.route("/<string:id>")
@ns.param("id", "The task identifier")
class Member_(Resource):
    def get(self, id):
        return Member.get_member(id)


@ns.route("/search")
class MemberSearch(Resource):
    def get(self):
        print(request.args.to_dict())
        filter = request.args.to_dict()
        filter["age"] = request.args.getlist("age")
        filter["page"] = int(filter.setdefault("page", 1))

        return Member.get_filter_members(filter)

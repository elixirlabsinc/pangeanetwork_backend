from flask import Blueprint
from app.models.role import RoleModel

roles_bp = Blueprint("roles", __name__, url_prefix="/roles")

@roles_bp.route("/<role_id>", methods=["GET"])
def show(role_id):
    role = RoleModel.find_by_id(role_id)
    if role:
        return role.json()
    return {'message': 'role not found'}, 400


@roles_bp.route("", methods=["GET"])
def index():
    roles = RoleModel.query.all()

    return {'roles': [role.json() for role in roles]}

from flask_restful import reqparse
from flask import Blueprint, request
from app.models.revolving_fund import RevolvingFundModel
from app.models.user import UserModel
from datetime import datetime, timedelta

members_bp = Blueprint("members", __name__, url_prefix="/members")

@members_bp.route("/<member_id>", methods=["GET"])
def show(member_id):
    member = UserModel.find_by_id(member_id)
    if member:
        return member.json()
    return {'message': 'Member not found'}, 400

@members_bp.route("", methods=["POST"])
def create():
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        type=str,
                        required=True,
                        help="The first_name field cannot be left blank")
    parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help="The last_name field cannot be left blank")
    parser.add_argument('email',
                        type=str,
                        required=False)
    parser.add_argument('phone',
                        type=str,
                        required=True,
                        help="The phone field cannot be left blank")
    parser.add_argument('password',
                        type=str,
                        required=False,
                        help="The password field cannot be left blank")
    parser.add_argument('role_id',
                        type=str,
                        required=True,
                        help="The role_id field cannot be left blank")
    parser.add_argument('co_op_id',
                        type=str,
                        required=True)
    parser.add_argument('fund_balance',
                        type=str,
                        required=False)
    data = parser.parse_args()
    user = UserModel(
      data['first_name'],
      data['last_name'],
      data['email'],
      data['phone'],
      data['password'],
      data['role_id'],
      data['co_op_id']
    )
    user.save_to_db()
    if data['fund_balance'] != '' and data['fund_balance'] != None:
        fund = RevolvingFundModel(data['fund_balance'], data['fund_balance'], datetime.now(), datetime.now() + timedelta(days = 365*5), user.id)
        fund.save_to_db()

        user.revolving_fund = fund
        user.save_to_db()
    result = { 'status': 200, 'user_id': user.id }
    # TODO: prompt loan creation if loan_id was not given
    # TODO: request email confirmation if email was given
    return result


@members_bp.route("", methods=["GET"])
def index():
    members = UserModel.query.all()

    return {'members': [member.json() for member in members]}

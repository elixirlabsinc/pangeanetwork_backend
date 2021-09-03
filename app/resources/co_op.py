from flask_restful import reqparse
from flask import Blueprint, request
from app.models.co_op import CoOpModel
from datetime import datetime, timedelta

co_ops_bp = Blueprint("co_ops", __name__, url_prefix="/co_ops")

@co_ops_bp.route("/<co_op_id>", methods=["GET"])
def show(co_op_id):
    co_op = CoOpModel.find_by_co_op_id(co_op_id)
    if co_op:
        return co_op.json()
    return {'message': 'Co-op not found'}, 400

@co_ops_bp.route("", methods=["POST"])
def create():
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="The name field cannot be left blank")
    parser.add_argument('start_date',
                        type=str,
                        required=False)
    parser.add_argument('end_date',
                        type=str,
                        required=False)
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="The location field cannot be left blank")
    parser.add_argument('initial_balance',
                        type=str,
                        required=True,
                        help="The initial_balance field cannot be left blank")
    data = parser.parse_args()
    co_op = CoOpModel(
      data['name'],
      datetime.now(),
      datetime.now() + timedelta(days = 365*5),
      data['location'],
      data['initial_balance'],
      data['initial_balance']
    )
    co_op.save_to_db()
    result = { 'status': 200, 'co_op_id': co_op.id }
    return result

@co_ops_bp.route("/<co_op_id>", methods=["PUT"])
def update(self, co_op_id):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="The name field cannot be left blank")
    parser.add_argument('start_date',
                        type=str,
                        required=False)
    parser.add_argument('end_date',
                        type=str,
                        required=False)
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="The location field cannot be left blank")
    parser.add_argument('initial_balance',
                        type=str,
                        required=True,
                        help="The initial_balance field cannot be left blank")
    data = self.parser.parse_args()
    co_op = CoOpModel.find_by_co_op_id(co_op_id)
    co_op.name = data['name']
    co_op.location = data['location']
    co_op.initial_balance = data['initial_balance']
    co_op.save_to_db()
    result = { 'status': 200, 'co_op_id': co_op.id }
    return result


@co_ops_bp.route("", methods=["GET"])
def index():
    search = request.args.get('search')

    if search:
        co_ops = CoOpModel.query.filter(CoOpModel.name.ilike(f'%{search}%')).all()
    else:
        co_ops = CoOpModel.query.all()

    return {'co_ops': [co_op.json() for co_op in co_ops]}
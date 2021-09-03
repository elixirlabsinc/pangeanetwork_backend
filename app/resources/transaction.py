from flask import Blueprint
from flask_restful import Resource
from app.models.transaction import TransactionModel

transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")

@transactions_bp.route("/<transaction_id>", methods=["GET"])
def show(transaction_id):
    transaction = TransactionModel.find_by_id(transaction_id)
    if transaction:
        return transaction.json()
    return {'message': 'Transaction not found'}, 400


@transactions_bp.route("", methods=["GET"])
def index():
    transactions = TransactionModel.query.all()

    return {'transactions': [transaction.json() for transaction in transactions]}

from flask import Blueprint
from app.models.revolving_fund import RevolvingFundModel

funds_bp = Blueprint("funds", __name__, url_prefix="/funds")

@funds_bp.route("/<fund_id>", methods=["GET"])
def show(revolving_fund_id):
    revolving_fund = RevolvingFundModel.find_by_id(revolving_fund_id)
    if revolving_fund:
        return revolving_fund.json()
    return {'message': 'Revolving Fund not found'}, 400


@funds_bp.route("", methods=["GET"])
def index():
    revolving_funds = RevolvingFundModel.query.all()

    return {'revolving_funds': [revolving_fund.json() for revolving_fund in revolving_funds]}

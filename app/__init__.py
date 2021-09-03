from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "DATABASE_URL")

    # Import models here for Alembic setup
    from app.models.co_op import CoOpModel
    from app.models.revolving_fund import RevolvingFundModel
    from app.models.role import RoleModel
    from app.models.transaction import TransactionModel
    from app.models.user import UserModel

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from app.resources.co_op import co_ops_bp
    from app.resources.member import members_bp
    from app.resources.message import sms_bp
    from app.resources.revolving_fund import funds_bp
    from app.resources.role import roles_bp
    from app.resources.transaction import transactions_bp

    app.register_blueprint(co_ops_bp)
    app.register_blueprint(members_bp)
    app.register_blueprint(sms_bp)
    app.register_blueprint(funds_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(transactions_bp)

    CORS(app)
    return app

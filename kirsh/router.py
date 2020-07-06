from flask import Blueprint
from flask_restful import Api


bp_basic = Blueprint("auth", __name__, url_prefix="/api/v1")
api_basic = Api(bp_basic)

from kirsh.view.auth import SignUp
api_basic.add_resource(SignUp, "/signup")

from kirsh.view.auth import Login
api_basic.add_resource(Login, "/login")

from kirsh.view.ranking import Ranking
api_basic.add_resource(Ranking, "/ranking")

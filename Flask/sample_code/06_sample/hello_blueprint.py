from flask import Blueprint

bp = Blueprint('first_blue', __name__, url_prefix="/blueprint")

@bp.route("/")
def hello_blueprint():
    return "Hello! Blueprint!!"
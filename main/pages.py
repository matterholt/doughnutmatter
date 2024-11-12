from flask import Blueprint


bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return "home"


@bp.route("/rng")
def main_rng():
    return "main RNG"

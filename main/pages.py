from flask import Blueprint, render_template


bp = Blueprint("pages", __name__)


@bp.route("/", methods=["GET"])
def home():
    return render_template("home/index.html")


@bp.route("/rng")
def main_rng():
    return "main RNG"

from flask import render_template
from flask import Blueprint
from manutd import app, db


routes = Blueprint('routes' ,__name__)


@app.route("/")
def home():
    return render_template("base.html")
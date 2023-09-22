from flask import Blueprint, render_template
index = Blueprint('index' ,__name__)


@index.route('/')
@index.route('/home')
def home() -> any:
    return render_template("home.html")
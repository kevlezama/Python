from flask import Blueprint, render_template, jsonify
index = Blueprint('index', __name__)


@index.route('/',methods=['GET'])
@index.route('/home', methods=['GET'])
def home() -> any:
    test = {

        'DNI': 95851445,
        'name':'kevin',
        'last_name':'lezama',
        'user_tier':'Tier 1'
    }

    return jsonify(test)


from flask import Blueprint

calculate = Blueprint('calculate', __name__)

@calculate.route("/")
def hehe():
    return "more organized routes :)"
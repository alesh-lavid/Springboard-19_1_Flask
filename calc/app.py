# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/math/<operation>")
def operate_math(operation):
    """Calculate operations based on route and query recieved

    Args:
        operation (str): Operation name

    Returns:
        str: Returns result from operation (a (+-*/) b)
    """
    operations_dic = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div
    }

    a = int(request.args["a"])
    b = int(request.args["b"])

    if operation not in operations_dic:
        return "Error, math operation not found."
    
    return str(operations_dic[operation](a, b))


# @app.route("/add")
# def calc_add_page():
#     a = int(request.args["a"])
#     b = int(request.args["b"])

#     return str(operations.add(a, b))

# @app.route("/sub")
# def calc_sub_page():
#     a = int(request.args["a"])
#     b = int(request.args["b"])

#     return str(operations.sub(a, b))

# @app.route("/mult")
# def calc_mult_page():
#     a = int(request.args["a"])
#     b = int(request.args["b"])

#     return str(operations.mult(a, b))

# @app.route("/div")
# def calc_div_page():
#     a = int(request.args["a"])
#     b = int(request.args["b"])

#     return str(operations.div(a, b))
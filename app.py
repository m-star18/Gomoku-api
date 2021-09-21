from flask import Flask, request, jsonify, make_response
import json

from src import base

app = Flask(__name__)


@app.route("/gomoku/cpu", methods=['GET'])
def get_gomoku():
    params = request.args
    # {0: 'black', 1: 'white', N}
    gomoku_json = json.loads(params["current_square_list"])
    # ランダムにNoneから
    res_x, res_y = base.run(gomoku_json)

    response = {"x": res_x, "y": res_y}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))


app.run(host="0.0.0.0", port=5000)

import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json

from src.greedy import greedy

app = Flask(__name__)

cors = CORS(app, resources={"*": {"origins": "*"}})


@app.route("/gomoku/cpu", methods=['GET'])
def get_gomoku():
    params = request.args
    # {0: 'black', 1: 'white', Null: None}
    gomoku_json = json.loads(params["current_square_list"])
    # greedy
    res_x, res_y = greedy.run(gomoku_json)

    response = {"x": res_x, "y": res_y}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))


# app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
if __name__ == '__main__':
    app.run()

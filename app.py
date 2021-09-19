from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)


@app.route("/gomoku/cpu", methods=['GET'])
def getGomoku():
    # URLパラメータ
    params = request.args
    gomoku_json = json.loads(params["current_square_list"])
    # ランダムにNoneから
    res_x, res_y = 0, 0
    flag = False
    for x, gg in enumerate(gomoku_json):
        for y, g in enumerate(gg):
            if g is None:
                res_y = y
                res_x = x
                flag = True
                break
        if flag:
            break

    response = {"x": res_x, "y": res_y}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))


app.run(host="0.0.0.0", port=5000)

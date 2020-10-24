from flask import Flask, render_template, request, jsonify, Response
from function import Function
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc', methods=['POST'])
def calc():
    try:
        data = json.loads(request.form['data'])
        func = Function(data['function'])
        res = func.calc(float(data['var']))
        tokens = ', '.join(list(map(str, func.tokens)))
        rpn = ''.join(list(map(str, func.rpn)))
        xs = list(range(data['tab']['from'], data['tab']['to'], data['tab']['step']))
        ys = []
        for i in xs:
            ys.append(func.calc(i))
        return jsonify(result=res, tokens=tokens, rpn=rpn, tab=list(zip(xs, ys)))
    except BaseException as e:
        return Response(status=400, response=str(e))


if __name__ == '__main__':
    app.run()

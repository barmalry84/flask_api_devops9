from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(message="Hello pople!!!")

@app.route('/sum', methods=['POST'])
def sum_number():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    sum = num1 + num2
    return jsonify(result=sum)

@app.route('/multiply', methods=['POST'])
def multi_number():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    multi = num1 * num2
    return jsonify(result=multi)


import requests as req
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

api_key = 'b542def189a74fa5d4b10bd9c35325026d18fedf94e1662863ddb5985c3ebb66'
url = '''https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,DASH&tsyms=BTC,USD,EUR&
api_key='''.format(api_key)


#OPÇÕES = BTC,ETH,DASH
@app.route("/")
def hello_word():
    return render_template('mainpage.html')


@app.route("/pegaeth", methods=['GET'])
def devolveth():
    dici = request.args.get('param')
    url = '''https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=BTC,USD,EUR&
api_key={}'''.format(dici,api_key)
    retorno = req.get(url).json()
    return jsonify(retorno)

if __name__ == '__main__':
            app.run(host='localhost', port=5002, debug=True)

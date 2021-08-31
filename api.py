# ### Exercício 01

# Desenvolver uma API que realize operações de
# - Somar ok
# - Subtrair ok
# - Dividir ok
# - Multiplicar ok
# - Raíz Quadrada
# - Potência ok
# - Média Aritmética
# - Média Harmônica
# - Moda

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import math
import statistics as s

from flask.wrappers import Response

app = Flask(__name__)
CORS(app)

@app.route('/')
def verificar_api():
    return "Server no ar", 200

@app.route('/api/v1/calculator/raizquadrada', methods=['GET'])
def getraiz():
    
    num = request.args['num'] 
    response = { "operacao": "raiz quadrada", "resultado": math.sqrt(int(num))}
    return response,20

@app.route('/api/v1/calculator/media', methods=['GET'])
def getMedia():
    num1 = request.args['num1']
    num2 = request.args['num2']
    num3 = request.args['num3']
    num4 = request.args['num4']
    num5 = request.args['num5']
    media = request.args['media']

    if media == 'aritmetica':
        result = s.mean([int(num1),int(num2),int(num3),int(num4),int(num5)])
    elif media == 'harmonica':
        result = s.harmonic_mean([int(num1),int(num2),int(num3),int(num4),int(num5)])
    elif media == 'moda':
        result = s.mode([int(num1),int(num2),int(num3),int(num4),int(num5)])

    response = { "media": media, "result": result }

    return response,200


@app.route('/api/v1/calculator', methods=['GET'])
def classify_get():

    num1 = request.args['num1']
    num2 = request.args['num2']
    operacao = request.args['operacao']

    if operacao == 'somar':
        result = int(num1) + int(num2) 

    elif operacao == 'subtrair':
        result = int(num1) - int(num2)

    elif operacao == 'multiplicar':
        result = int(num1) * int(num2)
   
    elif operacao == 'dividir':
        result = int(num1) / int(num2)
    
    elif operacao == 'potencia':
        result = math.pow(int(num1), int(num2))
    
    response = {"operacao":operacao, "result":result}  

    return response,200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

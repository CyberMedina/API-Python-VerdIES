import os

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS


from openaiClient import *
from models.prompts import *
from models.chatbot import *


app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación


load_dotenv()






@app.route('/api/ecochat', methods=['POST'])
def chat():

    user_message = request.json.get('message')

    try:

        result = chatbot_message(user_message)

        return result
    
    except Exception as e:
        print(e)
        return 'Error en la comunicación con el servidor. Por favor, intenta de nuevo más tarde.'
    



    



@app.route('/')
def index():
    return 'Holi'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
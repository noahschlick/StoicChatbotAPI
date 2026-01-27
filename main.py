from dotenv import load_dotenv
from flask import Flask, request, jsonify
from collections import namedtuple
import responses
import os
import json

app = Flask(__name__)
API_TOKEN = os.getenv("API_TOKEN")

def verify_token():
    auth_header = request.headers.get("Authorization", "")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        return False
    
    token = auth_header.split(" ")[1]
    return token == API_TOKEN

# Home page
@app.route('/')
def index():
    return f'<h1>Welcome to FreeWater chatbot!</h1>'
            
"""
Create an api endpoint where you can query a response.
The user input can be set in api directory. A json file 
containing the response will then be returned.
"""
@app.route('/api')
def api():
    # Check token
    if not verify_token():
        return jsonify({"error": "Unauthorized"}), 401
    
    user_input = request.args.get('input')
    history = request.args.get('history')

    conversation_history = []
    if history:
        conversation_history = json.loads(history)

    response = responses.get_response(user_input, conversation_history)
    data = {
        'input': user_input,
        'response': response,
    }
    return data
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # config_env_vars()
    # user_response = input("Please enter a question: ")
    # response = responses.get_response(user_response)
    # print("The Response is: ", response)
    
    
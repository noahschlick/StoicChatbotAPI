from dotenv import load_dotenv
from flask import Flask, request
from collections import namedtuple
import responses

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return f'<h1>Welcome to FreeWater chatbot.</h1>'
            

"""
Create an api endpoint where you can query a response.
The user input can be set in api directory. A json file 
containing the response will then be returned.
"""
@app.route('/api')
def api():
    user_input = request.args.get('input')
    response = responses.get_response(user_input)
    json = {
        'input': user_input,
        'response': response,
    }
    return json


"""
Configures the environment variables for openAI key and 
discord token. 
Note: If you have cloned from github. You will need to get
your own openAI keys and discord token.
"""
def config_env_vars():
    load_dotenv()    

if __name__ == "__main__":
    #app.run() 
    config_env_vars()
    user_response = input("Please enter a question: ")
    response = responses.get_response(user_response)
    print("The Response is: ", response)
    
    
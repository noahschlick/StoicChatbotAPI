import bot
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
Run the default bot on discord using the token in .env
Note: If you've pulled this from github, you will not 
have acces to .env file.
"""
@app.route('/demobot')
def demobot():
    bot.run_discord_bot()

"""
Run a bot on discord with a bot token. A token can be made 
on https://discord.com/developers/applications 
"""
@app.route('/createbot')
def createbot():
    token = request.args.get('token')
    bot.run_discord_bot(token)

"""
Configures the environment variables for openAI key and 
discord token. 
Note: If you have cloned from github. You will need to get
your own openAI keys and discord token.
"""
def config_env_vars():
    load_dotenv()

if __name__ == "__main__":
    config_env_vars()
    app.run()
    
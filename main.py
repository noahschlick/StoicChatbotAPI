import bot
from dotenv import load_dotenv
from flask import Flask, request
from collections import namedtuple
import responses

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return f'<h1>Home Page</h1>'

# Create an api endpoint where you can query
@app.route('/api')
def api():
    user_input = request.args.get('input')
    response = responses.get_response(user_input)
    json = {
        'input': user_input,
        'response': response,
    }

    return json

# Run the API on Discord
@app.route('/discord')
def discord():
    bot.run_discord_bot()
   
def configure():
    load_dotenv()

if __name__ == "__main__":
    configure()
    app.run()
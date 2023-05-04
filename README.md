# FreeWater Chatbot RESTAPI

The FreeWater Chatbot RESTAPI is a web application built with Python and Flask that provides responses to user queries about the FreeWater company. The application includes a Discord bot that users can interact with to get information about the company.

## Installation

To install the FreeWater Chatbot RESTAPI, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run `pip install -r requirements.txt` to install the necessary dependencies.

## Usage

To run the application, use the following command:

## main.py

This will start the Flask web server, and you will be able to access the API endpoints by navigating to `http://localhost:5000/`.

### API Endpoints

The FreeWater Chatbot RESTAPI includes the following API endpoints:

- `/`: The home page that displays a welcome message.
- `/api`: An API endpoint that accepts user input and returns a response in JSON format.
- `/demobot` and `/createbot`: API endpoints used to run a Discord bot with either the default or custom token.

#### Example Usage

To use the `/api` endpoint, make a GET request to the following URL:
https://freewaterchatbotapi.onrender.com/api?input=your_input_message_here

Replace `your_input_message_here` with the message you want to send to the chatbot. The API will return a JSON object with the input message and the response from the chatbot.

To run the Discord bot, use the `/demobot` API endpoint to run the bot with the default token, or use the `/createbot` API endpoint to run the bot with a custom token. Note that you must have a Discord bot token to run the bot.

### Dependencies

The FreeWater Chatbot RESTAPI relies on the following dependencies:

- Flask
- python-dotenv
- llama_index
- langchain
- discord.py

## Contributing

If you would like to contribute to the FreeWater Chatbot RESTAPI, please fork the repository and create a pull request. All contributions are welcome!

## License

The FreeWater Chatbot RESTAPI is released under the MIT License. See LICENSE for more details.
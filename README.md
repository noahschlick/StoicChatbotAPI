# FreeWater Chatbot RESTAPI

The FreeWater Chatbot RESTAPI is a web application built with Python and Flask that provides responses to user queries about the FreeWater company. The api can be used in a variety of applications including discord bots and wordpress

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

#### Example Usage

To use the `/api` endpoint, make a GET request to the following URL:
https://freewaterchatbotapi.onrender.com/api?input=your_input_message_here

Replace `your_input_message_here` with the message you want to send to the chatbot. The API will return a JSON object with the input message and the response from the chatbot.


### Dependencies

The FreeWater Chatbot RESTAPI relies on the following dependencies:

- Flask
- python-dotenv
- llama_index
- langchain

## Contributing

If you would like to contribute to the FreeWater Chatbot RESTAPI, please fork the repository and create a pull request. All contributions are welcome!

## License

The FreeWater Chatbot RESTAPI is released under the MIT License. See LICENSE for more details.
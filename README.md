# Stoic Chatbot RESTAPI

The FreeWater Chatbot RESTAPI is a web application built with Python and Flask that provides responses to user queries about the FreeWater company. The api can be used in a variety of applications including discord bots and wordpress

## Installation

You have two options for running this application:

### Option 1: Docker (Recommended for Python 3.12+ systems)

If you have Python 3.12+ locally and need Python 3.11 for compatibility:

1. Install [Docker](https://docs.docker.com/get-docker/) on your system
2. Clone the repository to your local machine
3. Navigate to the project directory
4. Build and run with Docker:

```bash
# Build the Docker image
.\docker-run.ps1 build

# Run in interactive mode (CLI)
.\docker-run.ps1 run

# Or run as web server
.\docker-run.ps1 web
```

### Option 2: Local Installation

If you have Python 3.11 or below locally:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run `pip install -r requirements.txt` to install the necessary dependencies.

## Usage

### Docker Usage

Use the provided PowerShell script for easy Docker management:

```powershell
# Build the image
.\docker-run.ps1 build

# Run in CLI mode (interactive)
.\docker-run.ps1 run

# Run as web server (accessible at http://localhost:5001)
.\docker-run.ps1 web

# Open a shell in the container for debugging
.\docker-run.ps1 shell

# Install new packages
.\docker-run.ps1 install -Package numpy

# View logs
.\docker-run.ps1 logs

# Stop containers
.\docker-run.ps1 stop

# Clean up Docker resources
.\docker-run.ps1 clean
```

### Local Usage

To run the application locally, use the following command:

```bash
python main.py
```

## 🎯 **Key Benefits**

✅ **Python 3.11 compatibility** - Solves your version conflict  
✅ **Isolated environment** - No conflicts with your local Python 3.13  
✅ **Consistent deployment** - Same environment everywhere  
✅ **Easy dependency management** - Install packages safely in container  
✅ **Volume mounting** - Your code changes reflect immediately  

## 📝 **Environment Variables**

Copy `.env.template` to `.env` and add your API keys:
```powershell
cp .env.template .env
# Then edit .env with your actual values
```

The Docker setup automatically handles all the Python 3.11 compatibility issues while keeping your local Python 3.13 installation intact. Your dependencies will work perfectly in the containerized Python 3.11 environment!

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

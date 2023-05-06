## Overview:
The FreeWater Chatbot REST API is a web application that utilizes Python and Flask to provide responses to userqueries about the FreeWater company. It is designed to be easily accessigble and user-freindly.

The REST API is built on top of the Flask framework, which makes it easy to develop and deploy web applicaitons. The endpoints of the REST API are defined in main.py, which include the home page and an API endpoint for user input.

The responses to user queries are generated using the GPTSimpleVectorIndex from the llama_index package, and the connection to the OpenAL API is established through the connect_AI function in responses.py

Overall, the FreeWater Chatbot REST API is versatile and easy-to-use web application that provides users with a simple way to get answers to their questions about the FreeWater company. The documentation should provide clear instauctions for setting up and running the REST API, as well as any necessary environment variables or dependencies.

## Files
### Main.py:
This file is the main entry point for the REST API. It contains three API endpointsthat canbe accessed using HTTP GET request:
 - /: The home page that displays a welcome message
 - /api: An API endpoint that accepts user input and returns a response in JSON format.


### responses.py:
This file contains the get_response and connect_AI functions. The get_response function generates a response to the user's message using the GPTSimpleVectorIndex from the llama_index package. It takes a string message as input and returns a string response.

The connect_AI function connects to the OpenAI API by setting the OPENAI_API_KEY environment variable. It enters a while loop that keeps trying to connect to the API until successful. If the API key is not found, the function prompts the user to enter a valid key.

This function, named construct_index, takes a directory path as input and constructs an index of the documents in that directory. The index is constructed using a GPT (Generative Pre-trained Transformer) model, specifically the GPTSimpleVectorIndex class, which creates a vector representation of each document based on its content.
The function sets several parameters that define how the index will be constructed, such as the maximum input size, the number of tokens that the index will return as output, the maximum number of overlapping tokens between adjacent input chunks, and the maximum number of tokens that the index will process at once.
The function then uses a PromptHelper and an LLMPredictor to assist in constructing the index. The PromptHelper helps to construct the prompts that will be used to generate the vector representations of the documents, while the LLMPredictor predicts the likelihood of a given text sequence based on a pre-trained language model.
Next, the function loads the training data from the specified directory path using a SimpleDirectoryReader.
Finally, the function constructs the index using the GPTSimpleVectorIndex class and saves it to disk as a JSON file named index.json. The constructed index is returned as the output of the function.
Overall, this function is useful for creating an index of a collection of documents that can be used for efficient search and retrieval of information.

Overall, these files work together to provide a REST API and Discord bot that respond to user queries about the FreeWater company. The documentation should provide instructions for setting up and running the application, as well as any necessary environment variables or dependencies.

### interview.txt
The training data used to train the FreeWater chatbot is stored in the "context_data/data" directory. This data contains sample questions and responses that the chatbot can use to generate appropriate answers to user queries. Specifically, the data includes questions and responses related to FreeWater's business model.

The data has been organized and formatted in a way that can be easily read and processed by the GPTSimpleVectorIndex from the llama_index package, which is used by the chatbot to generate responses.

### End Points Implementation:
The FreeWater Chatbot REST API provides three endpoints that can be accessed using HTTP GET requests. The public URL for this API is https://freewaterchatbotapi.onrender.com/.

### Home Page (/)
The home page endpoint displays a welcome message when accessed. It can be accessed by sending an HTTP GET request to the following URL:
https://freewaterchatbotapi.onrender.com/

Example usage:
```python
import requests

response = requests.get('https://freewaterchatbotapi.onrender.com/')
print(response.text)
```

Output:
```html
<h1>Welcome to FreeWater chatbot.</h1>
```

### API endpoint (/api)
The API endpoint accepts a user's input message and returns a response in JSON format. The endpoint can be used in many application from making Discord chatbots to implemtation in a Wardpress site. It can be accessed by sending an HTTP GET request to the following URL:
https://freewaterchatbotapi.onrender.com/api?input={user_input}

where {user_input} is the message input by the user.

Example usage:
```python
import requests

response = requests.get('https://freewaterchatbotapi.onrender.com/api?input=What is FreeWater?')
print(response.json())
```

Output:
```json
{
    "input": "What is FreeWater?",
    "response": "FreeWater is a company that provides clean and accessible water to people in need around the world."
}
```

## Dependencies
The following dependencies are required to run the FreeWater Chatbot REST API:
 - Python 3.8.3 or higher
 - Flask
 - python-dotenv
 - llama_index

## Setup
To set up the FreeWater Chatbot RESTAPI, follow these steps:
 1. Clone the repository to your local machine.
 2. Install the required dependencies using pip.
 3. Set up environment variables for your OpenAI API key and Discord bot token. You can do this by creating a .env file in the root directory of the project and adding the following lines:
 4. OPENAI_API_KEY=your OpenAI API key
 5. DISCORD_TOKEN=your Discord bot token
 6. Run main.py using the command "python main.py".
 7. Access the API endpoints using HTTP GET requests.


 ## Step by Step Procedure
 1. I researched how to use the OpenAI API to fine tune chat GPT with training data. I discovered that I could use two libraries to train the AI to answer question pertaining to the FreeWater information. These libraries are llama_index and langchain. 
### llama_index:
The llama_index library is a python package that provides a set of tools and utilities for building and working with text base search engines. The library includes modules for building search indexes from various sources, such as text files, directories, and web pages. It also includes modules for performing language modeling tasks, such as text classification and prediction. lamma_index includes some of the modules used in this program.
 - SimpleDirectoryReader: A module for reading text files and directories and creating a simple index of their contents.
 - GPTSimpleVectorIndex: a module for creating a search index from a list of text strings using the GPT language model and a simple vector representation.
 - LLMPredictor: a module for using a pre-trained language model to predict the next word or sequence of words in a text.
 - PromptHelper: a module for generating prompts and suggestions for text-based tasks using a pre-trained language model.
 - ServiceContext: a module for managing service context and configuration settings for the library.

 ### langchain 
 I used langchain to access and interact with OpenAI’s language models. Langchain is used to predict the likelihood of a given text sequence based on the trained language model. Langchain is used to initialize the llm parameter of the LLMPredictor class. This sets up a connection to OpenAI;s language model API and configures it with specific stetting scubas temperature, which controls the level of randomness in the generated text.

 Wrote the three function in responses.py which generates a response. The construct_index() function takes a directory path as input, loads text data from files in that directory using the SimpleDirectoryReader class from the llama_index library, and constructs a search index from the text data using the GPTSimpleVectorIndex class. The vector index is saved to a JSON file called index.json. This will help create  reference to answers of simular quations that were asked. 
 
 The connect_AI function connects the OpenAI API. the get_responses queries the users question and returns the AI generated answer to the question.

 2. I then created data used to fin tune the AI. The data is a simple txt file with a series of questions and unawares to the questions. The question is labeled as the interviewee and the answer is labeled as the interviewer. I looked through FreeWater.io website and produced as mush questions and answers as I could from the information from the website. To test is the language model worked I ran a series of question to the get_response function in responses.py
 3. After the AI was able to produce quality responses, then I used the Flask library to create a REST API to generate a JSON format of the responses.
4. I then used the hosting service render to host the program. The hosting service generated a url that could be used which is https://freewaterchatbotapi.onrender.com. You can test the URL by using the directory ./api. For example if you look up https://freewaterchatbotapi.onrender.com/api?input=What is FreeWater?, then you will get a JSON format of the prompt and response. 
5. I descided to write a separate program for the discord chatbot because the browser would time out trying to run the discord chat bot on the hosting service.


## Conclusion
In conclusion, the FreeWater Chatbot REST API is a versatile and powerful tool for users seeking information about the FreeWater company. The application provides a variety of API endpoints that allow users to easily access information through simple HTTP GET requests. The FreeWater Chatbot REST API is able to reach a wider audience and provide a more convenient and accessible experience for users. With its ease of use, flexibility, and powerful functionality, the FreeWater Chatbot REST API is an excellent example of the power of modern web technologies and the potential they offer for improving communication and engagement between businesses and their customers.

from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import os

"""
construct_index
Takes a directory path to training data as input and constructs a collection 
of documents that can be used for efficient search and retrieval of information. 
"""
def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    
    # set the maximum number of tokens that the index will return as output.
    num_outputs = 2000

    # set the maximum number of overlapping tokens between adjacent input chunks.
    max_chunk_overlap = 20

    # set the maximum number of tokens that the index will process at once.
    chunk_size_limit = 600

    # define prompt helper. 
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    # define LLM. Predict the likelihood of a given text sequence based on a trained language model (LLM)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))

    # Load the training data
    documents = SimpleDirectoryReader(directory_path).load_data()

    # Create vector representation of the documents as an index
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    # Save constructed index to json file that allows index to be loaded and used later
    # with out having to recreate from scratch
    index.save_to_disk('index.json')

    return index

"""
get_response
The functiontakes a string named message as input, repesenting a user's message
to a chatbot or similar program. The function returns a string response generated
by the program based on the input message.
"""
def get_response(message: str) -> str:    
    directory_path = "context_data/data"
    index = construct_index(directory_path)

    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(message)
    return response.response

"""
connect_AI
The purpose of this function is to connect the the OpenAI API be setting the OPEN_API_KEY 
environment variable. 
The function starts by entering a while loop that will keep trying to connect to the OpenAI
 API until successful. Inside the while loop, the function first attempts to retrieve the API key 
 from an environment variable using the os.getenv method. If the API key is not found, the 
 function prompts the user to enter a valid OpenAI API key.
"""
def connect_AI():
    # Connect to openAI API
    while True:
        try: 
            OPENAI_KEY = os.getenv("OPENAI_API_KEY")
            if OPENAI_KEY is None:
                print("Missing Open AI KEY!")
                OPENAI_KEY = input("Enter a valid open AI key: ")
            os.environ["OPENAI_API_KEY"] = OPENAI_KEY
            break
        except Exception as e:
            print(f"An error accured: {e}")
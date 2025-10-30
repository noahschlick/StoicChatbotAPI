from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
import os

"""
construct_index
Takes a directory path to training data as input and constructs a collection 
of documents that can be used for efficient search and retrieval of information. 
"""
def construct_index(directory_path):
    # Configure the LLM globally using the modern API
    Settings.llm = OpenAI(
        model="gpt-3.5-turbo-instruct",
        temperature=0.5,
        max_tokens=2000
    )
    
    # Load the training data
    documents = SimpleDirectoryReader(directory_path).load_data()

    # Create vector representation of the documents as an index
    index = VectorStoreIndex.from_documents(documents)

    # Save constructed index to disk using modern storage
    index.storage_context.persist(persist_dir="./storage")

    return index

"""
get_response
The functiontakes a string named message as input, repesenting a user's message
to a chatbot or similar program. The function returns a string response generated
by the program based on the input message.
"""
def get_response(message: str) -> str:    
    directory_path = "context_data/data"
    
    # Configure the LLM globally
    Settings.llm = OpenAI(
        model="gpt-3.5-turbo-instruct",
        temperature=0.5,
        max_tokens=2000
    )
    
    # Try to load existing index, if it doesn't exist create a new one
    try:
        # Check if storage directory exists
        if os.path.exists("./storage"):
            storage_context = StorageContext.from_defaults(persist_dir="./storage")
            index = load_index_from_storage(storage_context)
        else:
            raise FileNotFoundError("No storage directory found")
    except:
        # Create new index if loading fails
        index = construct_index(directory_path)
    
    # Query the index using modern API
    query_engine = index.as_query_engine()
    response = query_engine.query(message)
    return str(response)

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
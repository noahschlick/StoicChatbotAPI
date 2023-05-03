from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import os
from IPython.display import Markdown, display


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

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
    index.save_to_disk('index.json')

    return index

def get_response(message: str) -> str:    
    directory_path = "context_data/data"
    index = construct_index(directory_path)

    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(message)
    return response.response

    #return 'I didn\'t understand what you wrote. Try typing "!help".'

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
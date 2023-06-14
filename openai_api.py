import os
import openai
from dotenv import load_dotenv
import tiktoken
import requests

load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

NUM_KEYS = 1
KEYS = []
CURR_KEY = 0

for i in range(NUM_KEYS):
    if i == 0:
        KEYS.append(os.environ.get('OPENAI_API_KEY'))
    else:
        KEYS.append(os.environ.get(f'OPENAI_API_KEY{i+1}'))

def token_count(text:str, model='gpt-3.5-turbo'):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(text))
    return num_tokens

def embedding(text):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input = [text], model="text-embedding-ada-002")['data'][0]['embedding']
    
def chatGPT(chat_history, system='You are a helpful assistant.', engine = "gpt-3.5-turbo", stream=False):
    global CURR_KEY
    # system = "You are a helpful assistant. You can answer questions soley based on the information given below. If the question can't be answered with the information given by the user, tell the user that you were unable to find the answer from the given information and ask the user if you should answer the question on you own, without referring to the given information."
    messages = [
        {"role": "system", "content": system},
    ]
    
    messages = messages + [{"role":"user", "content":chat_history}]
    
    
    response = openai.ChatCompletion.create(
        model = engine,
        messages = messages,
        stream = stream
    )
    
    if stream is False:
        answer = response.choices[0].message.content
        return answer
    
def chatGPT_function(chat_history, system="You are a helpful assistant", model="gpt-3.5-turbo-0613", functions=[]):
    messages = [
        {"role": "system", "content": system},
    ]
    
    messages = messages + [{"role":"user", "content":chat_history}]

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key,
    }
    json_data = {"model": model, "messages": messages}
    if functions is not None:
        json_data.update({"functions": functions})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

    # response = openai.Completion.create(
    #     model=model,
    #     messages = messages,
    #     functions=functions
    # )
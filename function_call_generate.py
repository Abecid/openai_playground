import json
import openai_api
from datetime import datetime

example = '{"name":"get_current_weather", "description":"Get the current weather in a given location", "parameters":{"type":"object", "properties":{"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"}, "unit":{"type":"string", "enum":["celsius", "fahrenheit"]}}, "required":["location"]}}'
gpt3_5_16k = 'gpt-3.5-turbo-16k'

def generate_function_call(engine='gpt-3.5-turbo'):
    start_time = datetime.now()
    prompt = "Generate as many function calls as possible in json format similar to the following example. Each example should be in json format and be separated with a newline. Make realistic sounding fictional functions that could be used in everyday life (for example, sports, school, work, etc. Be sure to add other original cases other than the ones that are mentioned).\n\n" + example + "\n\n---\n\n"
    response = openai_api.chatGPT(prompt, engine=engine)
    end_time = datetime.now()
    time_difference = end_time - start_time
    print(f"{engine}: Responded in {time_difference.total_seconds()} seconds.")
    
    response = response.split('\n')
    with open(f'out/function_calls_examples/function_call_generate_{engine}.jsonl', 'a') as f:
        for line in response:
            if '}' in line:
                f.write(line + '\n')
            else:
                print(f'skipping line: {line}')

def main():
    generate_function_call()
    generate_function_call(gpt3_5_16k)

if __name__ == '__main__':
    main()
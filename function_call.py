import openai_api

def call_query(query, engine='gpt-3.5-turbo-0613', functions=[]):
    prompt = f"{query}"
    response = openai_api.chatGPT_function(prompt, model=engine, functions=functions)
    # print(f"{engine}: {response}")
    with open(f'out/function_calls_output/function_call_generate_{engine}.jsonl', 'a') as f:
        f.write(f'{query}:{response}' + '\n')

def read_functions():
    functions = []
    with open('out/function_calls_examples/function_call_generate_gpt-3.5-turbo.jsonl', 'r') as f:
        for line in f:
            functions.append(line)
    
    with open('out/function_calls_examples/function_call_generate_gpt-3.5-turbo-16k.jsonl', 'r') as f:
        for line in f:
            functions.append(line)

    return functions

def read_queries():
    queries = []
    with open('function_test_queries.txt', 'r') as f:
        for line in f:
            queries.append(line)
    return queries

def main():
    functions = read_functions()
    test_queries = read_queries()

    for test_query in test_queries:
        call_query(test_query, functions=functions)

if __name__ == '__main__':
    main()
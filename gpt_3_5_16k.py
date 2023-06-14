from datetime import datetime

import openai_api

test_prompts = []

def call_test(test, engine='gpt-3.5-turbo', check_json=False):
    start_time = datetime.now()
    prompt = f"{test}"
    response = openai_api.chatGPT(prompt, engine=engine)
    end_time = datetime.now()
    time_difference = end_time - start_time
    print(f"{engine}: Responded in {time_difference.total_seconds()} seconds.")
    
    response = response.split('\n')
    with open(f'function_call_generate_{engine}.jsonl', 'w') as f:
        for line in response:
            if check_json:
                if '}' in line:
                    f.write(line + '\n')
                else:
                    print(f'skipping line: {line}')
            else:
                f.write(line + '\n')

def get_query():
    query = ''
    with open('3_5_test_query.txt', 'r') as f:
        for line in f:
            query += line
    return query

def get_queries():
    queries = []
    with open('3_5_test_queries.txt', 'r') as f:
        for line in f:
            queries.append(line)
    return queries

def test_queries():
    test_prompts = get_queries()
    
    for test_prompt in test_prompts:
        call_test(test_prompt)
        call_test(test_prompt, 'gpt-3.5-turbo-16k')

def test_query():
    test_query = get_query()
    
    call_test(test_query)
    call_test(test_query, 'gpt-3.5-turbo-16k')

def main():
    test_query()

if __name__ == '__main__':
    main()
from datetime import datetime

import openai_api

test_prompts = []

def call_test(test, engine='gpt-3.5-turbo'):
    start_time = datetime.now()
    prompt = f"{test}"
    response = openai_api.chatGPT(prompt, engine=engine)
    end_time = datetime.now()
    time_difference = end_time - start_time
    print(f"{engine}: Responded in {time_difference.total_seconds()} seconds.")
    
    response = response.split('\n')
    with open(f'function_call_generate_{engine}.jsonl', 'w') as f:
        for line in response:
            if '}' in line:
                f.write(line + '\n')
            else:
                print(f'skipping line: {line}')

def main():
    for test_prompt in test_prompts:
        call_test(test_prompt)
        call_test(test_prompt, 'gpt-3.5-turbo-16k')

if __name__ == '__main__':
    main()
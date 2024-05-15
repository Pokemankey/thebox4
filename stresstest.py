import requests
import json
import concurrent.futures

# change for your host
VLLM_HOST = "http://localhost:8000"
url = f"{VLLM_HOST}/v1/completions"

headers = {"Content-Type": "application/json"}

def send_request(prompt):
    data = {
        "model": "meta-llama/Meta-Llama-3-8B",
        "prompt": prompt,
        "temperature": 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["choices"][0]["text"]

# Function to send multiple requests concurrently
def stress_test(num_requests):
    prompts = ["JupySQL is"] * num_requests
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Map each prompt to the send_request function and execute them concurrently
        results = list(executor.map(send_request, prompts))
    return results

# Define the number of concurrent requests
num_requests = 100  # Change this to the desired number of requests

# Execute stress test and print the responses
responses = stress_test(num_requests)
for i, response in enumerate(responses):
    print(f"Response {i+1}: {response}")

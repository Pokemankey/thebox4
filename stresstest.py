import requests
import json
import concurrent.futures
import random
import time
import csv

# Change for your host
VLLM_HOST = "https://cgqjwus9a4fqzl-8000.proxy.runpod.net"
url = f"{VLLM_HOST}/v1/completions"

headers = {"Content-Type": "application/json"}

# List of prompts
prompts = [
    "How to bake a cake",
    "The benefits of exercise",
    "The future of artificial intelligence",
    "Exploring space exploration",
    "The importance of education",
    "The impact of climate change",
    "The history of ancient civilizations",
    "The art of storytelling",
    "The evolution of technology",
    "The psychology of happiness"
]

def send_request(prompt):
    data = {
        "model": "meta-llama/Meta-Llama-3-70B",
        "prompt": prompt,
        "max_tokens": 300
    }
    stime = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    etime = time.time()
    ctime = round(etime - stime, ndigits=3)
    total_time = etime - stime
    tokens = response.json()["usage"]["completion_tokens"]
    tokens_per_second = tokens / ctime
    return [total_time, tokens_per_second, tokens]

# Function to pick a random prompt from the list
def pick_random_prompt():
    return random.choice(prompts)

# Function to send multiple requests concurrently
def stress_test(num_requests):
    # Pick random prompts for each request
    prompts = [pick_random_prompt() for _ in range(num_requests)]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Map each prompt to the send_request function and execute them concurrently
        results = list(executor.map(send_request, prompts))
    return results

# Define the number of concurrent requests
num_requests = 50  # Change this to the desired number of requests

# Execute stress test and store the responses
responses = stress_test(num_requests)

# Generate CSV file with the responses
csv_filename = "stress_test_results.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Sr No.", "Total Time (s)", "Tokens per Second", "Generated Tokens"])
    # Write the data
    for i, response in enumerate(responses):
        writer.writerow([i + 1] + response)

print(f"Results have been written to {csv_filename}")
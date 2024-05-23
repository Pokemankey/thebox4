import requests
import json
import requests
import json
import concurrent.futures
import random
import time
import csv

# change for your host
VLLM_HOST = "http://localhost:8000"
url = f"{VLLM_HOST}/v1/completions"

headers = {"Content-Type": "application/json"}
data = {
    "model": "meta-llama/CodeLlama-34b-hf",
    "prompt": "How to bake a cake",
    "max_tokens": 300,
    "min_tokens": 280,
    "temperature": 0
}
stime = time.time()
response = requests.post(url, headers=headers, data=json.dumps(data))
etime = time.time()
ctime = round(etime - stime, ndigits=3)
total_time = etime - stime
tokens = response.json()["usage"]["completion_tokens"]
tokens_per_second = tokens / ctime
print(f'Latency = {total_time}  TokensPerSec = {tokens_per_second}')
print(response.json()['choices'][0])

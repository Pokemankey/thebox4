import requests
import json

# change for your host
VLLM_HOST = "http://localhost:8000"
url = f"{VLLM_HOST}/v1/completions"

headers = {"Content-Type": "application/json"}
data = {
    "model": "meta-llama/Meta-Llama-3-8B",
    "prompt": "JupySQL is",
    "max_tokens": 100,
    "temperature": 0
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json()['choices'][0]['text'])
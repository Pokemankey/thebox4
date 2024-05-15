from vllm import LLM, SamplingParams

modelname = "meta-llama/Meta-Llama-3-8B"

# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams()

# Create an LLM.
llm = LLM(model=modelname)
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(output.metrics)
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")


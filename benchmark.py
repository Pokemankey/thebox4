from vllm import LLM, SamplingParams

modelname = "meta-llama/Meta-Llama-3-8B"

# Sample prompts.
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
]*10
# Create a sampling params object.
sampling_params = SamplingParams(max_tokens=300)

# Create an LLM.
llm = LLM(model=modelname)
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    metrics = output.metrics
    tokens = len(output.outputs[0].text.split(" "))
    total_time = metrics.finished_time - metrics.first_token_time
    time_to_first_token = metrics.first_token_time - metrics.arrival_time
    tokens_per_second = tokens/total_time
    print(f"total_time: {total_time}, time to first token: {time_to_first_token}, tokens_per_second: {tokens_per_second}")
    # print(metrics)
    # print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")



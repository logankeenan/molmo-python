import time
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from PIL import Image
import os
import torch

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
torch.cuda.empty_cache()

print(f"Is CUDA available: {torch.cuda.is_available()}")
print(f"CUDA device name: {torch.cuda.get_device_name(0)}")
print(f"Current device: {torch.cuda.current_device()}")

# Timing starts before loading the processor
start_time = time.time()

# Load the processor
processor = AutoProcessor.from_pretrained(
    'allenai/Molmo-7B-D-0924',
    trust_remote_code=True,
    torch_dtype='auto',
    device_map='cpu'
)

# Measure the time taken to load the processor
processor_load_time = time.time()
print(f"Processor load time: {processor_load_time - start_time:.2f} ms")

# Load the model
model = AutoModelForCausalLM.from_pretrained(
    'allenai/Molmo-7B-D-0924',
    trust_remote_code=True,
    torch_dtype='auto',
    device_map='cpu'
)

# Measure the time taken to load the model
model_load_time = time.time()
print(f"Model load time: {model_load_time - processor_load_time:.2f} ms")

# Process the image and text
prompt = "What is the point coordinate of the sign up button. Only include the json response in the output {x, y}"

# Start timing for input processing
input_start_time = time.time()

inputs = processor.process(
    images=[Image.open("img.png")],
    text=prompt
)

# Move inputs to the correct device and make a batch of size 1
inputs = {k: v.to(model.device).unsqueeze(0) for k, v in inputs.items()}

# Measure the time taken to process inputs
input_process_time = time.time()
print(f"Input processing time: {input_process_time - input_start_time:.2f} ms")

# Start timing for generation
generation_start_time = time.time()

# Generate output; maximum 200 new tokens; stop generation when <|endoftext|> is generated
output = model.generate_from_batch(
    inputs,
    GenerationConfig(max_new_tokens=200, stop_strings="<|endoftext|>"),
    tokenizer=processor.tokenizer
)

# Measure the time taken for generation
generation_time = time.time()
print(f"Generation time: {generation_time - generation_start_time:.2f} ms")

# Only get generated tokens; decode them to text
generated_tokens = output[0, inputs['input_ids'].size(1):]
generated_text = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

# Measure the time taken for decoding
decoding_time = time.time()
print(f"Decoding time: {decoding_time - generation_time:.2f} ms")

# Print the generated text
print("prompt: ", prompt)
print("Generated Text:", generated_text)

# Print total time
total_time = decoding_time - start_time
print(f"Total execution time: {total_time:.2f} ms")

print("#####################")

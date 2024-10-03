from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig, BitsAndBytesConfig
from PIL import Image
import torch
import os

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

print(f"Is CUDA available: {torch.cuda.is_available()}")
print(f"CUDA device name: {torch.cuda.get_device_name(0)}")
print(f"Current device: {torch.cuda.current_device()}")

torch.cuda.empty_cache()

# load the processor
processor = AutoProcessor.from_pretrained(
    'allenai/Molmo-7B-O-0924',
    trust_remote_code=True,
    torch_dtype='auto',
    device_map='cuda'
)

arguments = {"device_map": "cuda", "torch_dtype": "auto", "trust_remote_code": True}
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="fp4",
    bnb_4bit_use_double_quant=False,
)
arguments["quantization_config"] = quantization_config


# load the model
model = AutoModelForCausalLM.from_pretrained("allenai/Molmo-7B-O-0924", **arguments)

# process the image and text
inputs = processor.process(
    images=[Image.open("img.png")],
    text="what is the point coordinate of the sign up button. Only include the json response in the output {x, y}"
)

# move inputs to the correct device and make a batch of size 1
inputs = {k: v.to(model.device).unsqueeze(0) for k, v in inputs.items()}

# generate output; maximum 200 new tokens; stop generation when <|endoftext|> is generated
output = model.generate_from_batch(
    inputs,
    GenerationConfig(max_new_tokens=200, stop_strings="<|endoftext|>"),
    tokenizer=processor.tokenizer
)

# only get generated tokens; decode them to text
generated_tokens = output[0,inputs['input_ids'].size(1):]
generated_text = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

# print the generated text
print(generated_text)

# >>>  This image features an adorable black Labrador puppy, captured from a top-down
#      perspective. The puppy is sitting on a wooden deck, which is composed ...

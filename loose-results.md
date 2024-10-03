Processor load time: 1.69 ms
Model load time: 1.73 ms
Input processing time: 0.08 ms
Generation time: 116.34 ms
Decoding time: 0.00 ms
prompt: What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 119.84 ms
#####################


4090 with bitsAndbytes
(venv) root@6c6c69c0d97a:/workspace/molmo-python# python main.py 
Is CUDA available: True
CUDA device name: NVIDIA GeForce RTX 4090
Current device: 0
Processor load time: 2.32 ms
Model load time: 6.80 ms
Input processing time: 0.08 ms
Generation time: 1.75 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 10.96 ms
#####################

4090
17258MiB /  24564MiB

```
model.to(dtype=torch.bfloat16)
inputs["images"] = inputs["images"].to(torch.bfloat16)
torch_dtype=torch.bfloat16,
```
no bits and bytes settings

Is CUDA available: True
CUDA device name: NVIDIA GeForce RTX 4090
Current device: 0
Processor load time: 2.69 ms
Model load time: 6.50 ms
Input processing time: 0.08 ms
Generation time: 1.54 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 10.82 ms
#####################
Same settings as last run

Is CUDA available: True
CUDA device name: NVIDIA GeForce RTX 4090
Current device: 0
Processor load time: 2.56 ms
Model load time: 5.85 ms
Input processing time: 0.09 ms
Generation time: 1.32 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 9.81 ms
#####################

4090 with bits and bytes
11448MiB /  24564MiB

Is CUDA available: True
CUDA device name: NVIDIA GeForce RTX 4090
Current device: 0
Processor load time: 2.09 ms
Model load time: 7.07 ms
Input processing time: 0.10 ms
Generation time: 1.66 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 10.92 ms
#####################

11448MiB /  24564MiB 
Is CUDA available: True
CUDA device name: NVIDIA GeForce RTX 4090
Current device: 0
torch_dtype:  auto
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.75 ms
Model load time: 6.89 ms
Input processing time: 0.08 ms
Generation time: 1.72 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 11.45 ms

#######################

11692MiB /  24564MiB
Is CUDA available: True
CUDA device name: NVIDIA GeForce RTX 4090
Current device: 0
torch_dtype:  auto
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.24 ms
Model load time: 7.32 ms
Input processing time: 0.09 ms
Generation time: 1.32 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {10.6, 41.8}
Total execution time: 10.96 ms

#####################

Is CUDA available: True
CUDA device name: NVIDIA GeForce RTX 4090
Current device: 0
torch_dtype:  auto
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.32 ms
Model load time: 6.09 ms
Input processing time: 0.08 ms
Generation time: 1.31 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {10.6, 41.8}
Total execution time: 9.81 ms
#####################

tried the smallest model
6560MiB /  24564MiB
torch_dtype:  auto
model name:  allenai/MolmoE-1B-0924
The tokenizer class you load from this checkpoint is not the same type as the class this function is called from. It may result in unexpected tokenization. 
The tokenizer class you load from this checkpoint is 'GPTNeoXTokenizer'. 
The class this function is called from is 'GPT2TokenizerFast'.
Processor load time: 2.43 ms
Model load time: 11.53 ms
Input processing time: 0.12 ms
Generation time: 4.55 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 8,
  "y": 15
}
Total execution time: 18.63 ms
#####################
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.35 ms
Model load time: 6.92 ms
Input processing time: 0.08 ms
Generation time: 0.91 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {8.6, 41.8}
Total execution time: 10.26 ms
#####################

torch_dtype:  torch.float32
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.75 ms
crashed and ran out of memory

## allenai/Molmo-7B-O-0924 with torch.bfloat16
17238MiB /  24564MiB

torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.14 ms
Model load time: 6.54 ms
Input processing time: 0.09 ms
Generation time: 0.91 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {8.6, 41.8}
Total execution time: 9.69 ms
#####################

torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-O-0924
Processor load time: 1.94 ms
Model load time: 6.20 ms
Input processing time: 0.09 ms
Generation time: 0.94 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {8.6, 41.8}
Total execution time: 9.17 ms
#####################

torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.59 ms
Model load time: 6.18 ms
Input processing time: 0.09 ms
Generation time: 0.90 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {8.6, 41.8}
Total execution time: 9.76 ms

#####################
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.67 ms
Model load time: 6.17 ms
Input processing time: 0.09 ms
Generation time: 0.93 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {8.6, 41.8}
Total execution time: 9.87 ms

#####################
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.56 ms
Model load time: 6.22 ms
Input processing time: 0.09 ms
Generation time: 0.90 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {8.6, 41.8}
Total execution time: 9.77 ms
#####################

# allenai/Molmo-7B-O-0924 torch_dtype:  'auto' bits&bytes
torch_dtype:  auto
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.86 ms
Model load time: 8.41 ms
Input processing time: 0.09 ms
Generation time: 1.31 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {10.6, 41.8}
Total execution time: 12.67 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.35 ms
Model load time: 6.65 ms
Input processing time: 0.09 ms
Generation time: 1.33 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {10.6, 41.8}
Total execution time: 10.42 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.13 ms
Model load time: 6.53 ms
Input processing time: 0.10 ms
Generation time: 1.31 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {10.6, 41.8}
Total execution time: 10.07 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-O-0924
Processor load time: 1.78 ms
Model load time: 6.65 ms
Input processing time: 0.10 ms
Generation time: 1.32 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {10.6, 41.8}
Total execution time: 9.85 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-O-0924
Processor load time: 2.12 ms
Model load time: 6.69 ms
Input processing time: 0.09 ms
Generation time: 1.30 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {10.6, 41.8}
Total execution time: 10.21 ms
#####################

# allenai/Molmo-7B-D-0924 torch_dtype:  'auto' bits&bytes
11448MiB /  24564MiB
torch_dtype:  auto
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.19 ms
Model load time: 7.48 ms
Input processing time: 0.09 ms
Generation time: 1.64 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 11.41 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.53 ms
Model load time: 6.61 ms
Input processing time: 0.09 ms
Generation time: 1.71 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 10.95 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.43 ms
Model load time: 6.66 ms
Input processing time: 0.11 ms
Generation time: 1.65 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 10.85 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-D-0924
Processor load time: 1.95 ms
Model load time: 6.48 ms
Input processing time: 0.09 ms
Generation time: 1.68 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 10.20 ms
#####################
torch_dtype:  auto
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.59 ms
Model load time: 6.55 ms
Input processing time: 0.09 ms
Generation time: 1.65 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.2,
  "y": 41.8
}
Total execution time: 10.88 ms
#####################

## allenai/Molmo-7B-O-0924 with torch.bfloat16
17258MiB /  24564MiB 
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.76 ms
Model load time: 5.93 ms
Input processing time: 0.09 ms
Generation time: 1.33 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 10.11 ms
#####################
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.31 ms
Model load time: 5.82 ms
Input processing time: 0.08 ms
Generation time: 1.31 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 9.52 ms
#####################
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-D-0924
Processor load time: 1.93 ms
Model load time: 5.99 ms
Input processing time: 0.08 ms
Generation time: 1.38 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 9.38 ms
#####################
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.71 ms
Model load time: 5.84 ms
Input processing time: 0.09 ms
Generation time: 1.33 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 9.98 ms
#####################
torch_dtype:  torch.bfloat16
model name:  allenai/Molmo-7B-D-0924
Processor load time: 2.95 ms
Model load time: 6.04 ms
Input processing time: 0.09 ms
Generation time: 1.33 ms
Decoding time: 0.00 ms
prompt:  What is the point coordinate of the sign up button. Only include the json response in the output {x, y}
Generated Text:  {
  "x": 10.0,
  "y": 41.5
}
Total execution time: 10.42 ms
#####################
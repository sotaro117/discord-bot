from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from diffusers import DiffusionPipeline
import torch

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
model_id = "google/gemma-2-2b-it"
client = InferenceClient(provider="hf-inference", api_key=HF_TOKEN)


def chat_completion(prompt: str):
    messages = [{"role": "user", "content": prompt}]

    output = client.chat.completions.create(
        model=model_id, messages=messages, max_tokens=500, stream=False
    )
    res = output.choices[0].message.content
    return res
    # # 1024
    # for chunk in output:
    #     print(f"Response: {chunk.choices[0]}")
    #     return chunk.choices[0].delta.content


def generate_image(prompt: str):
    pipe = DiffusionPipeline.from_pretrained(
        "stable-diffusion-v1-5/stable-diffusion-v1-5"
    )
    pipe = pipe.to("mps")

    # Recommended if your computer has < 64 GB of RAM
    pipe.enable_attention_slicing()
    # prompt -> a photo of an astronaut riding a horse on mars
    image = pipe(prompt).images[0]
    return image

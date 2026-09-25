import os
from huggingface_hub import InferenceClient

# ⚠️ PASTE YOUR FINE-GRAINED TOKEN HERE (must have 'Make calls to Inference Providers' enabled)
HF_API_KEY = "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"

# Initialize client specifying the partner provider explicitly
client = InferenceClient(provider="fal-ai", api_key=HF_API_KEY)
MODEL = "black-forest-labs/FLUX.1-schnell"


def generate_image(prompt):
  print("Generating image via partner provider (takes ~10 seconds)...")
  try:
    image = client.text_to_image(prompt, model=MODEL)
    output_filename = "generated_image.png"
    image.save(output_filename)
    print(f"✅ Success! Image saved as '{output_filename}'\n")
  except Exception as e:
    print(f"❌ Error: {e}\n")


def main():
  print(f"Primary model: {MODEL}")
  print("Type 'quit' to exit\n")

  while True:
    prompt = input("Enter prompt: ").strip()
    if prompt.lower() == "quit":
      break
    if not prompt:
      continue
    generate_image(prompt)


if __name__ == "__main__":
  main()
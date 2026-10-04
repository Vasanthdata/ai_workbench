import os
import sys
from dotenv import load_dotenv
from openai import OpenAI,AuthenticationError, APIConnectionError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY is not set in the environment variables.")
    print("Copy .env.example to .env and set your OpenAI API key.")
    sys.exit(1)

# print("OPENAI_API_KEY is successfully loaded.")

client = OpenAI(api_key=api_key)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

print('Sending prompt: "What is generative AI in once sentence"')

try:
    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Be concise"},
            {"role": "user", "content": "What is generative AI in once sentence"}
        ],
        temperature = 0.7,
        max_tokens = 100,
    )

# response + errors:

    print(f"Response: {response.choices[0].message.content}")
    print(f"Tokens used: {response.usage.total_tokens}")

except AuthenticationError:
    print("Error: Invalid API Key. Check your .env file")
except APIConnectionError:
    print("Error: Cannot connect. Check your internet connection.")
except Exception as e:
    print(f"Unexpected error occurred: {e}")


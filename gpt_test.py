import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model = 'gpt-4',
    prompt = "Hi",
    temperature = 0.45,
)

print(response)
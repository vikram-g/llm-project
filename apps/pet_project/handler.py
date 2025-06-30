import os
from openai import OpenAI
from utilities.env import load_env


load_env()

client = OpenAI(
  api_key=os.getenv("CHATGPT-API-KEY")
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);

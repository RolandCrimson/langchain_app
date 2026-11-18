from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  temperature=0.9,
  messages=[
    {"role": "system", "content": "다음 예시를 보고 대답해 줘."},
    {"role": "user", "content": "사람의 새끼는?"},
    {"role": "assistant", "content": "아기"},
    {"role": "user", "content": "개의 새끼는?"},
  ]
)

print(response)

print('_'*80)
print(response.choices[0].message.content) 
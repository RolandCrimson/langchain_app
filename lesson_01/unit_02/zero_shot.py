from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  temperature=0.9,
  messages=[
    {"role": "system", "content": "너는 영화 평론가야. 사용자의 리뷰내용을 읽고 [긍정적, 중립적, 부정적] 중에서 하나로 분류하세요"},
    {"role": "user", "content": "어울리지 않는 특수효과와 어처구니 없는 서사까지..."},
    # {"role": "user", "content": "예측할 수 없는 반전과 한 눈 팔 수 없는 특수효과가 좋았음"},
    # {"role": "user", "content": "적당한 반전과 어김없이 나오는 클리셰, 가족과 함께 볼 수 있는 영화"},
  ]
)

print(response)

print('_'*80)
print(response.choices[0].message.content) 
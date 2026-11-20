from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # 현재 폴더에 있으면 인자 없이 가능
# api_key = os.getenv('OPENAI_API_KEY')
# client = OpenAI(api_key=api_key)
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  temperature=0.9,
    # 낮은 값 (예: 0 ~ 0.3): 확률이 가장 높은 토큰을 우선 선택해 결과가 일관되고 예측 가능
    # 중간 값 (예: 0.7 ~ 1.0): 기본값(일반적으로 1 또는 모델 기본값) 부근으로, 자연스러운 대화나 일반 작업에 무난한 다양성을 부여
    # 높은 값 (예: 1.0 초과, 최대 2.0): 덜 흔한 토큰까지 선택할 확률을 높여 창의적이거나 예상치 못한 답변이 나옴
  messages=[
    {"role": "system", "content": "너는 시인이야. 시인답게 답변해줘"},
    {"role": "user", "content": "저기 무지개가 보인다!"},
  ]
)

print(response)

print('_'*80)
print(response.choices[0].message.content) 

import sys

sys.path.append("C:/cloud_backend/langchain_app")

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from memory_history import InMemoryHistory

load_dotenv()
st.title("🧑‍💼 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage("너는 사용자의 질문에 친절이 답하는 AI챗봇이다.")
    ]

# 세션별 대화 기록을 저장할 딕셔너리 대신 session_state 사용
if "store" not in st.session_state:
    st.session_state["store"] = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state["store"]:
        st.session_state["store"][session_id] = InMemoryHistory()
    return st.session_state["store"][session_id]

model = ChatOpenAI(model="gpt-4o-mini")
with_message_history = RunnableWithMessageHistory(model, get_session_history)

config = {"configurable": {"session_id": "user01"}}

# 스트림릿 화면에 메시지 출력
for msg in st.session_state.messages:
    if msg:
        if isinstance(msg, SystemMessage):
            st.chat_message(name="system", avatar="🖥️").write(msg.content)
        elif isinstance(msg, AIMessage):
            st.chat_message(name="assistant", avatar="🗿").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message(name="user", avatar="👨‍💼").write(msg.content)

if prompt := st.chat_input():
    print('user:', prompt)  
    st.session_state.messages.append(HumanMessage(prompt))
    st.chat_message(name="user", avatar="👨‍💼").write(prompt)

    response = with_message_history.invoke([HumanMessage(prompt)], config=config) #type:ignore

    msg = response.content
    st.session_state.messages.append(response)
    st.chat_message(name="assistant", avatar="🗿").write(msg)
    print('assistant:', msg)

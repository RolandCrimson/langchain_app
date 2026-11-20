from langchain_core.chat_history import BaseChatMessageHistory  # 메모리에 대화 기록을 저장하는 클래스
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage
from collections.abc import Sequence

class InMemoryHistory(BaseChatMessageHistory, BaseModel):
    """In memory implementation of chat message history."""

    messages: list[BaseMessage] = Field(default_factory=list)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        """Add a list of messages to the store"""
        self.messages.extend(messages)

    def clear(self) -> None:
        self.messages = []

# 세션별 대화 기록을 저장할 딕셔너리
store = {}

# 세션 ID에 따라 대화 기록을 가져오는 함수
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    # 만약 해당 세션 ID가 store에 없으면, 새로 생성해 추가함
    if session_id not in store:
        store[session_id] = InMemoryHistory()  # 메모리에 대화 기록을 저장하는 객체 생성
    return store[session_id]  # 해당 세션의 대화 기록을 반환

def reset_session_history(session_id: str, messages: BaseChatMessageHistory) -> None:
    store[session_id] = InMemoryHistory()  # 메모리에 대화 기록을 저장하는 객체 생성
    store[session_id].add_messages(messages)
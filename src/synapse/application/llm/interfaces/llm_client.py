from abc import ABC, abstractmethod

from synapse.application.llm.llm_dtos import ChatResponse


class LLMClient(ABC):

    @abstractmethod
    async def chat(self, message: str) -> ChatResponse:
        pass
from synapse.application.llm.interfaces.llm_client import LLMClient
from synapse.application.llm.llm_dtos import ChatResponse


class LLMService:

    def __init__(self, client: LLMClient):
        self._client = client

    async def chat(self, message: str) -> ChatResponse:
        return await self._client.chat(message)
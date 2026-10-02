from synapse.application.llm.interfaces.llm_client import LLMClient


class LLMService:

    def __init__(self, client: LLMClient):
        self._client = client

    async def chat(self, message: str) -> str:
        return await self._client.chat(message)
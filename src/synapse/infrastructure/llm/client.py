from langchain_core.language_models import BaseChatModel

from synapse.application.llm.interfaces.llm_client import LLMClient


class LangChainLLMClient(LLMClient):

    def __init__(self, llm: BaseChatModel):
        self._llm = llm

    async def chat(self, message: str) -> str:
        response = await self._llm.ainvoke(message)

        return response.content
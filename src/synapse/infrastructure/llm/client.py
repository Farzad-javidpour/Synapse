from langchain_core.language_models import BaseChatModel
from langchain_core.messages import (SystemMessage, HumanMessage)
from synapse.application.llm.interfaces.llm_client import LLMClient
from synapse.application.llm.llm_dtos import ChatResponse, TokenUsage


class LangChainLLMClient(LLMClient):
    #--------------------------------------------------
    def __init__(self, llm: BaseChatModel):
        self._llm = llm
    #--------------------------------------------------
    async def chat(self, message: str) -> ChatResponse:

        messages = [
        SystemMessage(
            "You are a helpful AI assitant. answer very short"
        ),
        HumanMessage(
            message
        ),
        ]

        response = await self._llm.ainvoke(messages)

        result = ChatResponse(
            question= message,
            response= response.content,
            provider= "shahr_bank",
            model= response.response_metadata.get("model"),
            remain_token= 0,
            token_usage= TokenUsage(
                input_token= response.usage_metadata.get("input_tokens", 0),
                output_token= response.usage_metadata.get("output_tokens", 0),
                total_token= response.usage_metadata.get("total_tokens", 0),
            )
        )

        return result
    #--------------------------------------------------
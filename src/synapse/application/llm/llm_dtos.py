from pydantic import BaseModel

class TokenUsage(BaseModel):
    input_token: int
    output_token: int
    total_token: int

class ChatResponse(BaseModel):
    question: str
    response: str
    provider: str
    model: str
    remain_token: int
    token_usage: TokenUsage
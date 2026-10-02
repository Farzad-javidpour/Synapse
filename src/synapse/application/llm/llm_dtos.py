from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        description="User message",
        examples=["سلام، خودت را معرفی کن"],
    )


class ChatResponse(BaseModel):
    response: str
    model: str
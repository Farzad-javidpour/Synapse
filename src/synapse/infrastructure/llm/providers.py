from enum import Enum

class LLMProvider(str, Enum):
    OLLAMA = "ollama"
    OPENROUTER = "openrouter"
    GROQ = "groq"
    GEMINI = "gemini"
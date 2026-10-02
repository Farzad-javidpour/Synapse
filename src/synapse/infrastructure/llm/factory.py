from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_openrouter import ChatOpenRouter

from synapse.core.config import app_setting

from .providers import LLMProvider


def get_llm(provider: LLMProvider):

    # -----------------------------
    # Ollama
    # -----------------------------

    if provider == LLMProvider.OLLAMA:

        return ChatOllama(
            model=app_setting.ollama_model,
            base_url=app_setting.ollama_base_url,
            temperature=0,
        )

    # -----------------------------
    # Gemini
    # -----------------------------

    if provider == LLMProvider.GEMINI:

        return ChatGoogleGenerativeAI(
            model=app_setting.gemini_model,
            google_api_key=app_setting.google_api_key,
            temperature=0,
            max_retries=2,
        )

    # -----------------------------
    # Groq
    # -----------------------------

    if provider == LLMProvider.GROQ:

        return ChatGroq(
            model=app_setting.groq_model,
            api_key=app_setting.groq_api_key,
            temperature=0,
            max_retries=2,
        )

    # -----------------------------
    # OpenRouter
    # -----------------------------

    if provider == LLMProvider.OPENROUTER:

        return ChatOpenRouter(
            model=app_setting.openrouter_model,
            api_key=app_setting.openrouter_api_key,
            temperature=0,
            max_retries=2,
        )

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from synapse.api.exceptions.exceptions import AppException
from synapse.api.exceptions.handlers import (
    app_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)
from synapse.api.middleware.request import request_context_middleware
from synapse.api.router import api_router


app = FastAPI(
    title="Synapse API",
    description="""
## Synapse AI Platform

Enterprise API for organizational knowledge retrieval,
RAG and Agentic AI.
""",
    version="0.1.0",
)


app.middleware("http")(
    request_context_middleware
)


app.add_exception_handler(
    AppException,
    app_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    unhandled_exception_handler,
)


app.include_router(api_router)
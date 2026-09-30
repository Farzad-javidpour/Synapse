import time
from uuid import uuid4

from fastapi import Request


async def request_context_middleware(
    request: Request,
    call_next,
):
    request_id = str(uuid4())

    request.state.request_id = request_id
    request.state.start_time = time.perf_counter()

    response = await call_next(request)

    duration_ms = (
        time.perf_counter() - request.state.start_time
    ) * 1000

    response.headers["X-Request-ID"] = request_id
    response.headers["X-Response-Time"] = f"{duration_ms:.2f}ms"

    return response
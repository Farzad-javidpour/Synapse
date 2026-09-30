from datetime import datetime, timezone
from time import perf_counter
from typing import Generic, TypeVar

from fastapi import Request
from pydantic import BaseModel


T = TypeVar("T")


class ApiError(BaseModel):
    code: str
    message: str
    details: object | None = None


class ApiMeta(BaseModel):
    request_id: str
    timestamp: datetime
    duration_ms: float


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: T | None = None
    error: ApiError | None = None
    meta: ApiMeta


def _create_meta(request: Request) -> ApiMeta:
    duration_ms = (
        perf_counter() - request.state.start_time
    ) * 1000

    return ApiMeta(
        request_id=request.state.request_id,
        timestamp=datetime.now(timezone.utc),
        duration_ms=round(duration_ms, 2),
    )


def success_response(
    request: Request,
    data: T,
) -> ApiResponse[T]:
    return ApiResponse(
        success=True,
        data=data,
        error=None,
        meta=_create_meta(request),
    )


def error_response(
    request: Request,
    error: ApiError,
) -> ApiResponse[None]:
    return ApiResponse(
        success=False,
        data=None,
        error=error,
        meta=_create_meta(request),
    )
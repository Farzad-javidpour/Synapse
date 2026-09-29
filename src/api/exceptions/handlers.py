from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.exceptions.exceptions import AppException
from api.schemas.response import ApiError, error_response


async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    response = error_response(
        request=request,
        error=ApiError(
            code=exc.code,
            message=exc.message,
            details=exc.details,
        ),
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(mode="json"),
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    response = error_response(
        request=request,
        error=ApiError(
            code="VALIDATION_ERROR",
            message="Request validation failed.",
            details=exc.errors(),
        ),
    )

    return JSONResponse(
        status_code=422,
        content=response.model_dump(mode="json"),
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    response = error_response(
        request=request,
        error=ApiError(
            code="INTERNAL_ERROR",
            message="An unexpected error occurred.",
        ),
    )

    return JSONResponse(
        status_code=500,
        content=response.model_dump(mode="json"),
    )
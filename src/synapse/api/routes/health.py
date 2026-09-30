from fastapi import APIRouter, Request
from pydantic import BaseModel

from synapse.api.exceptions.exceptions import AppException
from synapse.api.schemas.response import ApiResponse, success_response
from synapse.application.health.service import HealthService


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


health_service = HealthService()


class HealthResponse(BaseModel):
    status: str


class DependencyHealth(BaseModel):
    name: str
    status: str


class ReadinessResponse(BaseModel):
    status: str
    dependencies: list[DependencyHealth]


@router.get(
    "/live",
    response_model=ApiResponse[HealthResponse],
)
def liveness(
    request: Request,
) -> ApiResponse[HealthResponse]:

    is_alive = health_service.check_liveness()

    return success_response(
        request=request,
        data=HealthResponse(
            status="ok" if is_alive else "unhealthy",
        ),
    )


@router.get(
    "/ready",
    response_model=ApiResponse[ReadinessResponse],
)
def readiness(
    request: Request,
) -> ApiResponse[ReadinessResponse]:

    result = health_service.check_readiness()

    return success_response(
        request=request,
        data=ReadinessResponse(
            status=result.status,
            dependencies=[
                DependencyHealth(
                    name=dependency.name,
                    status=dependency.status,
                )
                for dependency in result.dependencies
            ],
        ),
    )


@router.get(
    "/error",
    response_model=ApiResponse[None],
    responses={
        400: {
            "model": ApiResponse[None],
            "description": "Bad request.",
        },
    },
)
def test_error(
    request: Request,
) -> ApiResponse[None]:

    raise AppException(
        code="TEST_ERROR",
        message="This is a test error.",
        status_code=400,
    )
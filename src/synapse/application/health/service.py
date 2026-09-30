from dataclasses import dataclass


@dataclass
class DependencyStatus:
    name: str
    status: str


@dataclass
class ReadinessResult:
    status: str
    dependencies: list[DependencyStatus]


class HealthService:

    def check_liveness(self) -> bool:
        return True

    def check_readiness(self) -> ReadinessResult:

        dependencies = [
            DependencyStatus(
                name="sqlserver",
                status="ok",
            ),
            DependencyStatus(
                name="qdrant",
                status="ok",
            ),
        ]

        return ReadinessResult(
            status="ok",
            dependencies=dependencies,
        )
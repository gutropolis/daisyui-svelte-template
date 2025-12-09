"""GraphQL types for plan features."""
import strawberry
from datetime import datetime
from typing import Optional


@strawberry.type
class PlanFeatureType:
    """Plan Feature type for GraphQL."""
    id: int
    key_name: str
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime


@strawberry.input
class CreatePlanFeatureInput:
    """Input for creating a plan feature."""
    key_name: str
    name: str
    description: Optional[str] = None


@strawberry.input
class UpdatePlanFeatureInput:
    """Input for updating a plan feature."""
    name: Optional[str] = None
    description: Optional[str] = None


@strawberry.type
class PlanFeatureResponse:
    """Response type for plan feature operations."""
    success: bool
    message: str
    data: Optional[PlanFeatureType] = None


@strawberry.type
class PlanFeaturesListResponse:
    """Response type for list of plan features."""
    success: bool
    message: str
    data: list[PlanFeatureType]

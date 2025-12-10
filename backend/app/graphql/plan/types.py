"""GraphQL types for Plan."""
import strawberry
from typing import Optional, List
from app.graphql.permission.types import PaginationInfo


@strawberry.type
class PlanType:
    """Plan GraphQL type."""
    id: int
    slug: str
    name: str
    price: str
    duration_days: int
    max_users: Optional[int]
    max_studies: Optional[int]
    max_storage_gb: Optional[int]
    features: Optional[List[int]]
    created_at: str
    updated_at: str


@strawberry.input
class CreatePlanInput:
    """Input for creating a plan."""
    slug: str
    name: str
    price: str
    duration_days: int
    max_users: Optional[int] = None
    max_studies: Optional[int] = None
    max_storage_gb: Optional[int] = None
    features: Optional[List[int]] = None


@strawberry.input
class UpdatePlanInput:
    """Input for updating a plan."""
    name: Optional[str] = None
    price: Optional[str] = None
    duration_days: Optional[int] = None
    max_users: Optional[int] = None
    max_studies: Optional[int] = None
    max_storage_gb: Optional[int] = None
    features: Optional[List[int]] = None


@strawberry.input
class FilterPlansInput:
    """Input for filtering plans."""
    search: Optional[str] = None


@strawberry.type
class PlanResponse:
    """Response for single plan operation."""
    success: bool
    message: str
    data: Optional[PlanType]


@strawberry.type
class PlanListResponse:
    """Response for plan list operation."""
    success: bool
    message: str
    data: List[PlanType]
    pagination: PaginationInfo

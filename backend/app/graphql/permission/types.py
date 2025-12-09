import strawberry
from typing import List
from datetime import datetime


@strawberry.type
class PermissionType:
    """Permission type for GraphQL responses"""
    id: int
    key_name: str
    name: str
    description: str | None
    icon: str | None
    feature_id: int
    created_at: str
    updated_at: str


@strawberry.type
class PaginationInfo:
    """Pagination metadata"""
    page: int
    limit: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool


@strawberry.input
class CreatePermissionInput:
    """Input for creating a permission"""
    key_name: str
    name: str
    feature_id: int
    description: str | None = None
    icon: str | None = None


@strawberry.input
class UpdatePermissionInput:
    """Input for updating a permission"""
    name: str | None = None
    description: str | None = None
    icon: str | None = None


@strawberry.input
class FilterPermissionsInput:
    """Input for filtering permissions"""
    feature_id: int | None = None
    search: str | None = None  # Search in name and key_name


@strawberry.type
class PermissionResponse:
    """Single permission response wrapper"""
    success: bool
    message: str
    data: PermissionType | None = None


@strawberry.type
class PermissionListResponse:
    """Multiple permissions response wrapper with pagination"""
    success: bool
    message: str
    data: List[PermissionType]
    pagination: PaginationInfo

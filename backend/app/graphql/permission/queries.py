import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.permission import Permission
from app.graphql.permission.types import (
    PermissionType,
    PermissionListResponse,
    PermissionResponse,
    FilterPermissionsInput,
    PaginationInfo,
)


def format_permission(permission: Permission) -> PermissionType:
    """Convert Permission model to PermissionType"""
    return PermissionType(
        id=permission.id,
        key_name=permission.key_name,
        name=permission.name,
        description=permission.description,
        icon=permission.icon,
        feature_id=permission.feature_id,
        created_at=permission.created_at.isoformat(),
        updated_at=permission.updated_at.isoformat(),
    )


@strawberry.type
class PermissionQuery:
    @strawberry.field
    def permissions(
        self,
        info,
        page: int = 1,
        limit: int = 10,
        filter_input: Optional[FilterPermissionsInput] = None,
    ) -> PermissionListResponse:
        """Get all permissions with pagination and optional filtering"""
        try:
            db = info.context["db"]
            # Validate pagination params
            if page < 1:
                page = 1
            if limit < 1 or limit > 100:
                limit = 10

            # Build query
            query = db.query(Permission)

            # Apply filters if provided
            if filter_input:
                if filter_input.feature_id:
                    query = query.filter(Permission.feature_id == filter_input.feature_id)
                if filter_input.search:
                    search_term = f"%{filter_input.search}%"
                    query = query.filter(
                        (Permission.name.ilike(search_term)) |
                        (Permission.key_name.ilike(search_term))
                    )

            # Get total count before pagination
            total = query.count()
            total_pages = (total + limit - 1) // limit

            # Apply pagination
            offset = (page - 1) * limit
            permissions = query.offset(offset).limit(limit).all()

            # Format permissions
            permission_list = [format_permission(p) for p in permissions]

            # Create pagination info
            pagination = PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                total_pages=total_pages,
                has_next=page < total_pages,
                has_prev=page > 1,
            )

            return PermissionListResponse(
                success=True,
                message=f"Found {total} permissions",
                data=permission_list,
                pagination=pagination,
            )
        except Exception as e:
            return PermissionListResponse(
                success=False,
                message=f"Failed to fetch permissions: {str(e)}",
                data=[],
                pagination=PaginationInfo(page=page, limit=limit, total=0, total_pages=0, has_next=False, has_prev=False),
            )

    @strawberry.field
    def permission(self, info, id: int) -> PermissionResponse:
        """Get a single permission by ID"""
        try:
            db = info.context["db"]
            permission = db.query(Permission).filter(Permission.id == id).first()
            if not permission:
                return PermissionResponse(
                    success=False,
                    message=f"Permission with ID {id} not found",
                    data=None,
                )
            return PermissionResponse(
                success=True,
                message="Permission found",
                data=format_permission(permission),
            )
        except Exception as e:
            return PermissionResponse(
                success=False,
                message=f"Failed to fetch permission: {str(e)}",
                data=None,
            )

    @strawberry.field
    def permission_by_key(self, info, key_name: str) -> PermissionResponse:
        """Get a permission by its unique key_name"""
        try:
            db = info.context["db"]
            permission = db.query(Permission).filter(Permission.key_name == key_name).first()
            if not permission:
                return PermissionResponse(
                    success=False,
                    message=f"Permission with key '{key_name}' not found",
                    data=None,
                )
            return PermissionResponse(
                success=True,
                message="Permission found",
                data=format_permission(permission),
            )
        except Exception as e:
            return PermissionResponse(
                success=False,
                message=f"Failed to fetch permission: {str(e)}",
                data=None,
            )

    @strawberry.field
    def permissions_by_feature(
        self,
        info,
        feature_id: int,
        page: int = 1,
        limit: int = 10,
    ) -> PermissionListResponse:
        """Get all permissions for a specific feature with pagination"""
        try:
            db = info.context["db"]
            # Validate pagination params
            if page < 1:
                page = 1
            if limit < 1 or limit > 100:
                limit = 10

            # Query permissions by feature
            query = db.query(Permission).filter(Permission.feature_id == feature_id)
            total = query.count()
            total_pages = (total + limit - 1) // limit

            # Apply pagination
            offset = (page - 1) * limit
            permissions = query.offset(offset).limit(limit).all()

            # Format permissions
            permission_list = [format_permission(p) for p in permissions]

            # Create pagination info
            pagination = PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                total_pages=total_pages,
                has_next=page < total_pages,
                has_prev=page > 1,
            )

            return PermissionListResponse(
                success=True,
                message=f"Found {total} permissions for feature {feature_id}",
                data=permission_list,
                pagination=pagination,
            )
        except Exception as e:
            return PermissionListResponse(
                success=False,
                message=f"Failed to fetch permissions: {str(e)}",
                data=[],
                pagination=PaginationInfo(page=page, limit=limit, total=0, total_pages=0, has_next=False, has_prev=False),
            )

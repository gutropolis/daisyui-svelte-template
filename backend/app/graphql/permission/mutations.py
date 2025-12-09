import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from app.models.permission import Permission
from app.models.plan_feature import PlanFeature
from app.graphql.permission.types import (
    PermissionType,
    PermissionResponse,
    CreatePermissionInput,
    UpdatePermissionInput,
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
class PermissionMutation:
    @strawberry.mutation
    def create_permission(
        self,
        info,
        input: CreatePermissionInput,
    ) -> PermissionResponse:
        """Create a new permission"""
        try:
            db = info.context["db"]
            # Validate input
            if not input.key_name or not input.key_name.strip():
                return PermissionResponse(
                    success=False,
                    message="Key name cannot be empty",
                    data=None,
                )
            if not input.name or not input.name.strip():
                return PermissionResponse(
                    success=False,
                    message="Name cannot be empty",
                    data=None,
                )

            # Check if key_name already exists
            existing = db.query(Permission).filter(Permission.key_name == input.key_name).first()
            if existing:
                return PermissionResponse(
                    success=False,
                    message=f"Permission with key '{input.key_name}' already exists",
                    data=None,
                )

            # Verify feature exists
            feature = db.query(PlanFeature).filter(PlanFeature.id == input.feature_id).first()
            if not feature:
                return PermissionResponse(
                    success=False,
                    message=f"Feature with ID {input.feature_id} not found",
                    data=None,
                )

            # Create permission
            permission = Permission(
                key_name=input.key_name,
                name=input.name,
                description=input.description,
                icon=input.icon,
                feature_id=input.feature_id,
            )
            db.add(permission)
            db.commit()
            db.refresh(permission)

            return PermissionResponse(
                success=True,
                message="Permission created successfully",
                data=format_permission(permission),
            )
        except Exception as e:
            db.rollback()
            return PermissionResponse(
                success=False,
                message=f"Failed to create permission: {str(e)}",
                data=None,
            )

    @strawberry.mutation
    def update_permission(
        self,
        info,
        id: int,
        input: UpdatePermissionInput,
    ) -> PermissionResponse:
        """Update an existing permission"""
        try:
            db = info.context["db"]
            # Find permission
            permission = db.query(Permission).filter(Permission.id == id).first()
            if not permission:
                return PermissionResponse(
                    success=False,
                    message=f"Permission with ID {id} not found",
                    data=None,
                )

            # Update fields if provided
            if input.name is not None and input.name.strip():
                permission.name = input.name
            if input.description is not None:
                permission.description = input.description
            if input.icon is not None:
                permission.icon = input.icon

            db.commit()
            db.refresh(permission)

            return PermissionResponse(
                success=True,
                message="Permission updated successfully",
                data=format_permission(permission),
            )
        except Exception as e:
            db.rollback()
            return PermissionResponse(
                success=False,
                message=f"Failed to update permission: {str(e)}",
                data=None,
            )

    @strawberry.mutation
    def delete_permission(self, info, id: int) -> PermissionResponse:
        """Delete a permission"""
        try:
            db = info.context["db"]
            # Find permission
            permission = db.query(Permission).filter(Permission.id == id).first()
            if not permission:
                return PermissionResponse(
                    success=False,
                    message=f"Permission with ID {id} not found",
                    data=None,
                )

            db.delete(permission)
            db.commit()

            return PermissionResponse(
                success=True,
                message="Permission deleted successfully",
                data=None,
            )
        except Exception as e:
            db.rollback()
            return PermissionResponse(
                success=False,
                message=f"Failed to delete permission: {str(e)}",
                data=None,
            )

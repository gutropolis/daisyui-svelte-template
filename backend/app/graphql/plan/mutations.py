"""GraphQL mutations for Plan."""
import strawberry
from typing import Optional
import json
from sqlalchemy.orm import Session
from app.models.plan import Plan
from app.graphql.plan.types import (
    PlanType,
    PlanResponse,
    CreatePlanInput,
    UpdatePlanInput,
)


def format_plan(plan: Plan) -> PlanType:
    """Convert Plan model to PlanType"""
    features = []
    if plan.features:
        try:
            features = json.loads(plan.features)
        except:
            features = []
    
    return PlanType(
        id=plan.id,
        slug=plan.slug,
        name=plan.name,
        price=str(plan.price),
        duration_days=plan.duration_days,
        max_users=plan.max_users,
        max_studies=plan.max_studies,
        max_storage_gb=plan.max_storage_gb,
        features=features,
        created_at=plan.created_at.isoformat(),
        updated_at=plan.updated_at.isoformat(),
    )


@strawberry.type
class PlanMutation:
    @strawberry.mutation
    def create_plan(
        self,
        info,
        input: CreatePlanInput,
    ) -> PlanResponse:
        """Create a new plan"""
        try:
            db = info.context["db"]
            # Validate input
            if not input.slug or not input.slug.strip():
                return PlanResponse(
                    success=False,
                    message="Slug cannot be empty",
                    data=None,
                )
            if not input.name or not input.name.strip():
                return PlanResponse(
                    success=False,
                    message="Name cannot be empty",
                    data=None,
                )
            if input.duration_days < 1:
                return PlanResponse(
                    success=False,
                    message="Duration days must be at least 1",
                    data=None,
                )

            # Check if slug already exists
            existing = db.query(Plan).filter(Plan.slug == input.slug).first()
            if existing:
                return PlanResponse(
                    success=False,
                    message=f"Plan with slug '{input.slug}' already exists",
                    data=None,
                )

            # Create plan
            features_json = json.dumps(input.features) if input.features else None
            plan = Plan(
                slug=input.slug,
                name=input.name,
                price=input.price,
                duration_days=input.duration_days,
                max_users=input.max_users,
                max_studies=input.max_studies,
                max_storage_gb=input.max_storage_gb,
                features=features_json,
            )
            db.add(plan)
            db.commit()
            db.refresh(plan)

            return PlanResponse(
                success=True,
                message="Plan created successfully",
                data=format_plan(plan),
            )
        except Exception as e:
            db.rollback()
            return PlanResponse(
                success=False,
                message=f"Failed to create plan: {str(e)}",
                data=None,
            )

    @strawberry.mutation
    def update_plan(
        self,
        info,
        id: int,
        input: UpdatePlanInput,
    ) -> PlanResponse:
        """Update an existing plan"""
        try:
            db = info.context["db"]
            # Find plan
            plan = db.query(Plan).filter(Plan.id == id).first()
            if not plan:
                return PlanResponse(
                    success=False,
                    message=f"Plan with ID {id} not found",
                    data=None,
                )

            # Update fields if provided
            if input.name is not None and input.name.strip():
                plan.name = input.name
            if input.price is not None:
                plan.price = input.price
            if input.duration_days is not None and input.duration_days > 0:
                plan.duration_days = input.duration_days
            if input.max_users is not None:
                plan.max_users = input.max_users
            if input.max_studies is not None:
                plan.max_studies = input.max_studies
            if input.max_storage_gb is not None:
                plan.max_storage_gb = input.max_storage_gb
            if input.features is not None:
                plan.features = json.dumps(input.features)

            db.commit()
            db.refresh(plan)

            return PlanResponse(
                success=True,
                message="Plan updated successfully",
                data=format_plan(plan),
            )
        except Exception as e:
            db.rollback()
            return PlanResponse(
                success=False,
                message=f"Failed to update plan: {str(e)}",
                data=None,
            )

    @strawberry.mutation
    def delete_plan(self, info, id: int) -> PlanResponse:
        """Delete a plan"""
        try:
            db = info.context["db"]
            # Find plan
            plan = db.query(Plan).filter(Plan.id == id).first()
            if not plan:
                return PlanResponse(
                    success=False,
                    message=f"Plan with ID {id} not found",
                    data=None,
                )

            db.delete(plan)
            db.commit()

            return PlanResponse(
                success=True,
                message="Plan deleted successfully",
                data=None,
            )
        except Exception as e:
            db.rollback()
            return PlanResponse(
                success=False,
                message=f"Failed to delete plan: {str(e)}",
                data=None,
            )

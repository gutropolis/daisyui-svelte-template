"""GraphQL mutations for plan features."""
import strawberry
from sqlalchemy.orm import Session
from app.models.plan_feature import PlanFeature
from .types import (
    PlanFeatureType,
    PlanFeatureResponse,
    CreatePlanFeatureInput,
    UpdatePlanFeatureInput,
)


@strawberry.type
class PlanFeatureMutation:
    """Mutations for plan features."""

    @strawberry.mutation
    def create_plan_feature(
        self, info, input: CreatePlanFeatureInput
    ) -> PlanFeatureResponse:
        """Create a new plan feature."""
        db: Session = info.context.get("db")
        try:
            # Check if key_name already exists
            existing = db.query(PlanFeature).filter(
                PlanFeature.key_name == input.key_name
            ).first()
            if existing:
                return PlanFeatureResponse(
                    success=False,
                    message=f"Plan feature with key_name '{input.key_name}' already exists",
                )

            feature = PlanFeature(
                key_name=input.key_name,
                name=input.name,
                description=input.description,
            )
            db.add(feature)
            db.commit()
            db.refresh(feature)

            return PlanFeatureResponse(
                success=True,
                message="Plan feature created successfully",
                data=PlanFeatureType(
                    id=feature.id,
                    key_name=feature.key_name,
                    name=feature.name,
                    description=feature.description,
                    created_at=feature.created_at,
                    updated_at=feature.updated_at,
                ),
            )
        except Exception as e:
            db.rollback()
            return PlanFeatureResponse(
                success=False,
                message=f"Error creating plan feature: {str(e)}",
            )

    @strawberry.mutation
    def update_plan_feature(
        self, info, id: int, input: UpdatePlanFeatureInput
    ) -> PlanFeatureResponse:
        """Update an existing plan feature."""
        db: Session = info.context.get("db")
        try:
            feature = db.query(PlanFeature).filter(PlanFeature.id == id).first()
            if not feature:
                return PlanFeatureResponse(
                    success=False,
                    message=f"Plan feature with id {id} not found",
                )

            if input.name is not None:
                feature.name = input.name
            if input.description is not None:
                feature.description = input.description

            db.commit()
            db.refresh(feature)

            return PlanFeatureResponse(
                success=True,
                message="Plan feature updated successfully",
                data=PlanFeatureType(
                    id=feature.id,
                    key_name=feature.key_name,
                    name=feature.name,
                    description=feature.description,
                    created_at=feature.created_at,
                    updated_at=feature.updated_at,
                ),
            )
        except Exception as e:
            db.rollback()
            return PlanFeatureResponse(
                success=False,
                message=f"Error updating plan feature: {str(e)}",
            )

    @strawberry.mutation
    def delete_plan_feature(self, info, id: int) -> PlanFeatureResponse:
        """Delete a plan feature."""
        db: Session = info.context.get("db")
        try:
            feature = db.query(PlanFeature).filter(PlanFeature.id == id).first()
            if not feature:
                return PlanFeatureResponse(
                    success=False,
                    message=f"Plan feature with id {id} not found",
                )

            db.delete(feature)
            db.commit()

            return PlanFeatureResponse(
                success=True,
                message="Plan feature deleted successfully",
                data=PlanFeatureType(
                    id=feature.id,
                    key_name=feature.key_name,
                    name=feature.name,
                    description=feature.description,
                    created_at=feature.created_at,
                    updated_at=feature.updated_at,
                ),
            )
        except Exception as e:
            db.rollback()
            return PlanFeatureResponse(
                success=False,
                message=f"Error deleting plan feature: {str(e)}",
            )

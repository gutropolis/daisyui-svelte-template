"""GraphQL queries for plan features."""
import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.plan_feature import PlanFeature
from .types import PlanFeatureType, PlanFeaturesListResponse


@strawberry.type
class PlanFeatureQuery:
    """Queries for plan features."""

    @strawberry.field
    def plan_features(self, info) -> PlanFeaturesListResponse:
        """Get all plan features."""
        db: Session = info.context.get("db")
        try:
            features = db.query(PlanFeature).all()
            return PlanFeaturesListResponse(
                success=True,
                message="Plan features retrieved successfully",
                data=[
                    PlanFeatureType(
                        id=f.id,
                        key_name=f.key_name,
                        name=f.name,
                        description=f.description,
                        created_at=f.created_at,
                        updated_at=f.updated_at,
                    )
                    for f in features
                ],
            )
        except Exception as e:
            return PlanFeaturesListResponse(
                success=False,
                message=f"Error retrieving plan features: {str(e)}",
                data=[],
            )

    @strawberry.field
    def plan_feature(self, info, id: int) -> Optional[PlanFeatureType]:
        """Get a specific plan feature by ID."""
        db: Session = info.context.get("db")
        try:
            feature = db.query(PlanFeature).filter(PlanFeature.id == id).first()
            if not feature:
                return None
            return PlanFeatureType(
                id=feature.id,
                key_name=feature.key_name,
                name=feature.name,
                description=feature.description,
                created_at=feature.created_at,
                updated_at=feature.updated_at,
            )
        except Exception as e:
            print(f"Error retrieving plan feature: {str(e)}")
            return None

    @strawberry.field
    def plan_feature_by_key(self, info, key_name: str) -> Optional[PlanFeatureType]:
        """Get a specific plan feature by key name."""
        db: Session = info.context.get("db")
        try:
            feature = db.query(PlanFeature).filter(PlanFeature.key_name == key_name).first()
            if not feature:
                return None
            return PlanFeatureType(
                id=feature.id,
                key_name=feature.key_name,
                name=feature.name,
                description=feature.description,
                created_at=feature.created_at,
                updated_at=feature.updated_at,
            )
        except Exception as e:
            print(f"Error retrieving plan feature: {str(e)}")
            return None

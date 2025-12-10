"""GraphQL queries for Plan."""
import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.plan import Plan
from app.graphql.plan.types import (
    PlanType,
    PlanListResponse,
    PlanResponse,
    FilterPlansInput,
)
from app.graphql.permission.types import PaginationInfo


def format_plan(plan: Plan) -> PlanType:
    """Convert Plan model to PlanType."""
    features = []
    if plan.features:
        try:
            import json
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
class PlanQuery:
    @strawberry.field
    def plans(
        self,
        info,
        page: int = 1,
        limit: int = 10,
        filter_input: Optional[FilterPlansInput] = None,
    ) -> PlanListResponse:
        """Get all plans with pagination and optional filtering"""
        try:
            db = info.context["db"]
            # Validate pagination params
            if page < 1:
                page = 1
            if limit < 1 or limit > 100:
                limit = 10

            # Build query
            query = db.query(Plan)

            # Apply filters if provided
            if filter_input:
                if filter_input.search:
                    search_term = f"%{filter_input.search}%"
                    query = query.filter(
                        (Plan.name.ilike(search_term)) |
                        (Plan.slug.ilike(search_term))
                    )

            # Get total count before pagination
            total = query.count()
            total_pages = (total + limit - 1) // limit

            # Apply pagination
            offset = (page - 1) * limit
            plans = query.offset(offset).limit(limit).all()

            # Format plans
            plan_list = [format_plan(p) for p in plans]

            # Create pagination info
            pagination = PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                total_pages=total_pages,
                has_next=page < total_pages,
                has_prev=page > 1,
            )

            return PlanListResponse(
                success=True,
                message=f"Found {total} plans",
                data=plan_list,
                pagination=pagination,
            )
        except Exception as e:
            return PlanListResponse(
                success=False,
                message=f"Failed to fetch plans: {str(e)}",
                data=[],
                pagination=PaginationInfo(page=page, limit=limit, total=0, total_pages=0, has_next=False, has_prev=False),
            )

    @strawberry.field
    def plan(self, info, id: int) -> PlanResponse:
        """Get a single plan by ID"""
        try:
            db = info.context["db"]
            plan = db.query(Plan).filter(Plan.id == id).first()
            if not plan:
                return PlanResponse(
                    success=False,
                    message=f"Plan with ID {id} not found",
                    data=None,
                )
            return PlanResponse(
                success=True,
                message="Plan found",
                data=format_plan(plan),
            )
        except Exception as e:
            return PlanResponse(
                success=False,
                message=f"Failed to fetch plan: {str(e)}",
                data=None,
            )

    @strawberry.field
    def plan_by_slug(self, info, slug: str) -> PlanResponse:
        """Get a plan by its unique slug"""
        try:
            db = info.context["db"]
            plan = db.query(Plan).filter(Plan.slug == slug).first()
            if not plan:
                return PlanResponse(
                    success=False,
                    message=f"Plan with slug '{slug}' not found",
                    data=None,
                )
            return PlanResponse(
                success=True,
                message="Plan found",
                data=format_plan(plan),
            )
        except Exception as e:
            return PlanResponse(
                success=False,
                message=f"Failed to fetch plan: {str(e)}",
                data=None,
            )

"""GraphQL queries for user."""
import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.graphql.user.types import UserType
from app.core.security import verify_token


@strawberry.type
class UserQuery:
    """User queries."""

    @strawberry.field
    def get_user(self, user_id: int, info: Optional[object] = None) -> Optional[UserType]:
        """Get user by ID."""
        db: Session = info.context["db"]
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        return UserType(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            contact_number=user.contact_number,
            bio=user.bio,
            role=user.role.value if user.role else "user",
            is_active=user.is_active,
            is_verified=user.is_verified,
            created_at=user.created_at,
            updated_at=user.updated_at,
            last_login=user.last_login,
        )

    @strawberry.field
    def get_current_user(self, token: str, info: Optional[object] = None) -> Optional[UserType]:
        """Get current authenticated user."""
        db: Session = info.context["db"]
        payload = verify_token(token)
        if not payload:
            return None
        
        user_id = int(payload["sub"])
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        return UserType(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            contact_number=user.contact_number,
            bio=user.bio,
            role=user.role.value if user.role else "user",
            is_active=user.is_active,
            is_verified=user.is_verified,
            created_at=user.created_at,
            updated_at=user.updated_at,
            last_login=user.last_login,
        )

    @strawberry.field
    def search_users(self, query: str, limit: int = 10, info: Optional[object] = None) -> list[UserType]:
        """Search users by email."""
        db: Session = info.context["db"]
        users = db.query(User).filter(
            User.email.ilike(f"%{query}%")
        ).limit(limit).all()
        
        return [
            UserType(
                id=user.id,
                email=user.email,
                full_name=user.full_name,
                contact_number=user.contact_number,
                bio=user.bio,
                role=user.role.value if user.role else "user",
                is_active=user.is_active,
                is_verified=user.is_verified,
                created_at=user.created_at,
                updated_at=user.updated_at,
                last_login=user.last_login,
            )
            for user in users
        ]

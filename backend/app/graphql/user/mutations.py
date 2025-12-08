"""GraphQL mutations for user."""
import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.graphql.user.types import UserType
from app.core.security import verify_token, hash_password, verify_password


@strawberry.type
class UserMutation:
    """User mutations."""

    @strawberry.mutation
    def update_profile(
        self,
        token: str,
        full_name: Optional[str] = None,
        bio: Optional[str] = None,
        info: Optional[object] = None,
    ) -> Optional[UserType]:
        """Update user profile."""
        db: Session = info.context["db"]
        payload = verify_token(token)
        if not payload:
            return None
        
        user_id = int(payload["sub"])
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        if full_name:
            user.full_name = full_name
        if bio is not None:
            user.bio = bio
        
        db.commit()
        db.refresh(user)
        
        return UserType(
            id=user.id,
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            bio=user.bio,
            is_active=user.is_active,
            is_verified=user.is_verified,
            created_at=user.created_at,
            updated_at=user.updated_at,
            last_login=user.last_login,
        )

    @strawberry.mutation
    def change_password(
        self,
        token: str,
        old_password: str,
        new_password: str,
        info: Optional[object] = None,
    ) -> bool:
        """Change user password."""
        db: Session = info.context["db"]
        payload = verify_token(token)
        if not payload:
            return False
        
        user_id = int(payload["sub"])
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        
        if not verify_password(old_password, user.hashed_password):
            return False
        
        user.hashed_password = hash_password(new_password)
        db.commit()
        return True
        
        if not verify_password(old_password, user.hashed_password):
            return False
        
        user.hashed_password = hash_password(new_password)
        db.commit()
        return True

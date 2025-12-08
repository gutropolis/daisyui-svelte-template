"""GraphQL mutations for authentication."""
import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token
from app.graphql.auth.types import TokenResponse, AuthPayload


@strawberry.type
class AuthMutation:
    """Authentication mutations."""

    @strawberry.mutation
    def register(
        self,
        email: str,
        password: str,
        full_name: Optional[str] = None,
        contact_number: Optional[str] = None,
        info: Optional[object] = None,
    ) -> AuthPayload:
        """Register a new user."""
        try:
            db: Session = info.context["db"]
            
            # Check if user already exists
            existing_user = db.query(User).filter(User.email == email).first()
            if existing_user:
                return AuthPayload(
                    success=False,
                    message="User with this email already exists"
                )

            # Create new user
            hashed_password_val = hash_password(password)
            new_user = User(
                email=email,
                hashed_password=hashed_password_val,
                full_name=full_name,
                contact_number=contact_number,
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            # Generate tokens
            access_token = create_access_token({"sub": str(new_user.id), "email": email})
            refresh_token = create_refresh_token({"sub": str(new_user.id), "email": email})

            return AuthPayload(
                success=True,
                message="User registered successfully",
                token=TokenResponse(access_token=access_token, refresh_token=refresh_token)
            )
        except Exception as e:
            return AuthPayload(success=False, message=f"Registration failed: {str(e)}")

    @strawberry.mutation
    def login(
        self,
        email: str,
        password: str,
        info: Optional[object] = None,
    ) -> AuthPayload:
        """Login user with email and password."""
        try:
            db: Session = info.context["db"]
            
            user = db.query(User).filter(User.email == email).first()
            if not user or not verify_password(password, user.hashed_password):
                return AuthPayload(success=False, message="Invalid email or password")

            if not user.is_active:
                return AuthPayload(success=False, message="User account is inactive")

            # Generate tokens
            access_token = create_access_token({"sub": str(user.id), "email": email})
            refresh_token = create_refresh_token({"sub": str(user.id), "email": email})

            return AuthPayload(
                success=True,
                message="Login successful",
                token=TokenResponse(access_token=access_token, refresh_token=refresh_token)
            )
        except Exception as e:
            return AuthPayload(success=False, message=f"Login failed: {str(e)}")

    @strawberry.mutation
    def refresh_access_token(self, refresh_token: str, info: Optional[object] = None) -> AuthPayload:
        """Generate a new access token from refresh token."""
        try:
            from app.core.security import verify_token
            db: Session = info.context["db"]
            
            payload = verify_token(refresh_token, token_type="refresh")
            if not payload:
                return AuthPayload(success=False, message="Invalid or expired refresh token")

            user_id = int(payload["sub"])
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return AuthPayload(success=False, message="User not found")

            access_token = create_access_token({"sub": str(user.id), "email": user.email})
            return AuthPayload(
                success=True,
                message="Token refreshed successfully",
                token=TokenResponse(access_token=access_token, refresh_token=refresh_token)
            )
        except Exception as e:
            return AuthPayload(success=False, message=f"Token refresh failed: {str(e)}")

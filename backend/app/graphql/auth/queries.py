"""GraphQL queries for authentication."""
import strawberry
from typing import Optional
from app.core.security import verify_token


@strawberry.type
class AuthQuery:
    """Authentication queries."""

    @strawberry.field
    def verify_token(self, token: str) -> bool:
        """Verify if a token is valid."""
        payload = verify_token(token)
        return payload is not None

    @strawberry.field
    def current_user_id(self, token: str) -> Optional[str]:
        """Get current user ID from token."""
        payload = verify_token(token)
        if payload:
            return payload.get("sub")
        return None

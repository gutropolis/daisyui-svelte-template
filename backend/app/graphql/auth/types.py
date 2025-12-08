"""GraphQL types for authentication."""
import strawberry
from datetime import datetime
from typing import Optional


@strawberry.type
class TokenResponse:
    """Response containing access and refresh tokens."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


@strawberry.type
class AuthPayload:
    """Response after authentication."""
    success: bool
    message: str
    token: Optional[TokenResponse] = None

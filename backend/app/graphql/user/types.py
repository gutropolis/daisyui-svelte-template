"""GraphQL types for user."""
import strawberry
from datetime import datetime
from typing import Optional


@strawberry.type
class UserType:
    """User type for GraphQL."""
    id: int
    email: str
    full_name: Optional[str] = None
    contact_number: Optional[str] = None
    bio: Optional[str] = None
    role: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

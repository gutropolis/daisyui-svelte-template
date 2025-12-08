"""GraphQL types for projects."""
import strawberry
from datetime import datetime
from enum import Enum


@strawberry.enum
class ProjectStatus(str, Enum):
    """Project status enumeration."""
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"


@strawberry.type
class ProjectType:
    """Project type for GraphQL."""
    id: int
    code: str
    title: str
    description: str | None = None
    status: ProjectStatus
    owner_id: int
    created_at: datetime
    updated_at: datetime

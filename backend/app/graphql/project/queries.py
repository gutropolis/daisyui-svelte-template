"""GraphQL queries for projects."""
import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from app.graphql.project.types import ProjectType, ProjectStatus


@strawberry.type
class ProjectQuery:
    """Project queries."""

    @strawberry.field
    def get_project(self, project_id: int, info: Optional[object] = None) -> Optional[ProjectType]:
        """Get project by ID."""
        # Placeholder - will implement with actual Project model
        return None

    @strawberry.field
    def list_projects(self, skip: int = 0, limit: int = 10, info: Optional[object] = None) -> list[ProjectType]:
        """List all projects with pagination."""
        # Placeholder - will implement with actual Project model
        return []

    @strawberry.field
    def search_projects(self, query: str, info: Optional[object] = None) -> list[ProjectType]:
        """Search projects by title or code."""
        # Placeholder - will implement with actual Project model
        return []

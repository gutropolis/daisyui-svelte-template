"""Project GraphQL module."""
from app.graphql.project.types import ProjectType, ProjectStatus
from app.graphql.project.queries import ProjectQuery
from app.graphql.project.mutations import ProjectMutation

__all__ = ["ProjectType", "ProjectStatus", "ProjectQuery", "ProjectMutation"]

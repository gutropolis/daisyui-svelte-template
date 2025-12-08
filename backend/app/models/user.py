"""User model definition."""
from enum import Enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum
from sqlalchemy.sql import func
from app.core.database import Base


class UserRole(str, Enum):
    """User role enumeration."""
    SUPERADMIN = "superadmin"
    ADMIN = "admin"
    USER = "user"


class User(Base):
    """User model for authentication and profile management."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    contact_number = Column(String(20), nullable=True)
    bio = Column(Text, nullable=True)
    role = Column(SQLEnum(UserRole), default=UserRole.USER, nullable=False)
    
    # Account status
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    last_login = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"
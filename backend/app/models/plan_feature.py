"""Plan Feature model definition."""
from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class PlanFeature(Base):
    """Plan Feature model for managing features unlocked by plans."""

    __tablename__ = "plan_features"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    key_name = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f"<PlanFeature(id={self.id}, key_name={self.key_name}, name={self.name})>"

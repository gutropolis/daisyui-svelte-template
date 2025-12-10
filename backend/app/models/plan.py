"""Plan model for subscription plans."""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime, BigInteger
from app.core.database import Base


class Plan(Base):
    """Plan model representing subscription plans."""
    __tablename__ = "plans"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False, default=0)
    duration_days = Column(Integer, nullable=False)  # 30, 365, etc.
    max_users = Column(Integer, nullable=True)
    max_studies = Column(Integer, nullable=True)
    max_storage_gb = Column(Integer, nullable=True)
    features = Column(String(500), nullable=True)  # JSON string of feature IDs
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Plan(id={self.id}, slug='{self.slug}', name='{self.name}')>"

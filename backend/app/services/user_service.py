"""User service for business logic."""
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password


class UserService:
    """User service for user-related operations."""

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User | None:
        """Get user by ID."""
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        """Get user by email."""`
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> User | None:
        """Get user by username."""
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def create_user(
        db: Session,
        email: str,
        username: str,
        password: str,
        full_name: str | None = None,
    ) -> User:
        """Create a new user."""
        user = User(
            email=email,
            username=username,
            hashed_password=hash_password(password),
            full_name=full_name,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update_user(
        db: Session,
        user: User,
        **kwargs,
    ) -> User:
        """Update user fields."""
        for key, value in kwargs.items():
            if hasattr(user, key) and value is not None:
                setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def verify_user_password(user: User, password: str) -> bool:
        """Verify user password."""
        return verify_password(password, user.hashed_password)

    @staticmethod
    def list_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
        """List users with pagination."""
        return db.query(User).offset(skip).limit(limit).all()

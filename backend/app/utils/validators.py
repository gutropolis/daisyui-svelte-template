"""Validation utilities."""
import re
from typing import Optional


def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_username(username: str) -> tuple[bool, Optional[str]]:
    """Validate username format."""
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    if len(username) > 50:
        return False, "Username must be at most 50 characters long"
    if not re.match(r"^[a-zA-Z0-9_-]+$", username):
        return False, "Username can only contain alphanumeric characters, underscores, and hyphens"
    return True, None


def validate_password(password: str) -> tuple[bool, Optional[str]]:
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit"
    return True, None

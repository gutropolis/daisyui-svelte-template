"""DaisyUI Healthcare Backend - Project Structure Guide"""

# Project Structure

## Directory Layout

```
backend/
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Application settings and configuration
│   │   ├── database.py        # Database connection and session management
│   │   └── security.py        # JWT tokens, password hashing
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py            # User database model
│   ├── graphql/
│   │   ├── __init__.py
│   │   ├── schema.py          # Combined GraphQL schema
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── types.py       # Auth-related GraphQL types
│   │   │   ├── queries.py     # Auth queries
│   │   │   └── mutations.py   # Auth mutations (register, login, refresh)
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   ├── types.py       # User GraphQL type
│   │   │   ├── queries.py     # User queries (get_user, search_users)
│   │   │   └── mutations.py   # User mutations (update_profile, change_password)
│   │   └── project/
│   │       ├── __init__.py
│   │       ├── types.py       # Project GraphQL types
│   │       ├── queries.py     # Project queries
│   │       └── mutations.py   # Project mutations
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py    # User business logic
│   ├── routers/
│   │   ├── __init__.py
│   │   └── health.py          # Health check REST endpoint
│   └── utils/
│       ├── __init__.py
│       ├── validators.py      # Email, username, password validation
│       └── logger.py          # Logging utilities
├── alembic/
│   ├── versions/
│   │   └── 91f4b6a33fb5_create_users_table.py
│   ├── env.py
│   └── alembic.ini
├── .env                       # Development environment variables
├── .env.production            # Production environment variables
├── .env.example               # Example template
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── README.md                  # Setup and development guide
└── pytest.ini                 # Pytest configuration
```

## Module Responsibilities

### `core/`

- **config.py**: Pydantic settings with environment variable support (dev/prod)
- **database.py**: SQLAlchemy engine, session management, Base for ORM models
- **security.py**: JWT token creation/verification, password hashing with bcrypt

### `models/`

- ORM models using SQLAlchemy
- Currently: User model with email, username, hashed_password, timestamps
- Future: Project, Team, Enrollment models

### `graphql/`

Modular GraphQL structure with separate folders for each domain:

**auth/** - Authentication

- `types.py`: TokenResponse, AuthPayload
- `queries.py`: verify_token, current_user_id
- `mutations.py`: register, login, refresh_access_token

**user/** - User Management

- `types.py`: UserType
- `queries.py`: get_user, get_current_user, search_users
- `mutations.py`: update_profile, change_password

**project/** - Project Management (placeholder)

- `types.py`: ProjectType with status enum
- `queries.py`: get_project, list_projects, search_projects
- `mutations.py`: create_project, update_project, delete_project

**schema.py**: Combines all modules into root Query and Mutation types

### `services/`

Business logic layer:

- `user_service.py`: User CRUD, authentication helpers

### `routers/`

REST API endpoints (optional, for non-GraphQL clients):

- `health.py`: GET /api/health for status checks

### `utils/`

Utility functions:

- `validators.py`: Email, username, password validation
- `logger.py`: Logging configuration

## Configuration Management

### Environment Variables

Defined in `config.py` with pydantic-settings:

```python
APP_NAME, APP_VERSION, ENVIRONMENT, DEBUG
DATABASE_URL
SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
CORS_ORIGINS, CORS_CREDENTIALS, CORS_METHODS, CORS_HEADERS
REDIS_URL, USE_REDIS
LOG_LEVEL
```

### Environment Files

- `.env` - Development settings
- `.env.production` - Production settings
- `.env.example` - Template for team members

Load with: `settings = Settings()` from `app.core.config`

## Database & ORM

### Technology

- **ORM**: SQLAlchemy 2.0+ (synchronous)
- **Driver**: pymysql for MySQL
- **Migrations**: Alembic with auto-generate support
- **Database**: MySQL (daisyui_db)

### Creating Models

1. Define SQLAlchemy model in `app/models/`
2. Run: `python -m alembic revision --autogenerate -m "description"`
3. Review migration file in `alembic/versions/`
4. Run: `python -m alembic upgrade head`

## Authentication Flow

### Registration

```
User inputs (email, username, password)
  ↓
Validation + Password hashing
  ↓
Create User in database
  ↓
Generate JWT tokens (access + refresh)
  ↓
Return tokens to client
```

### Login

```
User inputs (email, password)
  ↓
Validate credentials
  ↓
Generate JWT tokens
  ↓
Return tokens + set in localStorage
```

### Token Refresh

```
Client sends refresh_token
  ↓
Verify refresh token signature
  ↓
Generate new access_token
  ↓
Return new access_token
```

## GraphQL API Examples

### Register

```graphql
mutation {
  register(
    email: "user@example.com"
    username: "john_doe"
    password: "SecurePass123"
    fullName: "John Doe"
  ) {
    success
    message
    token {
      accessToken
      refreshToken
      tokenType
    }
  }
}
```

### Login

```graphql
mutation {
  login(email: "user@example.com", password: "SecurePass123") {
    success
    message
    token {
      accessToken
      refreshToken
    }
  }
}
```

### Get Current User

```graphql
{
  getCurrentUser(token: "access_token_here") {
    id
    email
    username
    fullName
    isActive
    createdAt
  }
}
```

## Dependencies

### Core

- fastapi: Web framework
- uvicorn: ASGI server
- strawberry-graphql: GraphQL implementation
- sqlalchemy: ORM
- alembic: Database migrations

### Authentication

- passlib: Password hashing
- python-jose: JWT tokens
- cryptography: Encryption

### Configuration

- pydantic: Data validation
- pydantic-settings: Environment variables
- python-dotenv: .env file loading

### Optional

- redis: Caching and task queue (not yet integrated)

Install all: `pip install -r requirements.txt`

## Development Workflow

1. **Start Dev Server**

   ```bash
   python -m uvicorn main:app --reload
   ```

   API available at `http://localhost:8000`
   GraphQL at `http://localhost:8000/graphql`

2. **Create Database Migration**

   ```bash
   python -m alembic revision --autogenerate -m "add user field"
   python -m alembic upgrade head
   ```

3. **Add New GraphQL Module**

   - Create folder: `app/graphql/module_name/`
   - Add `types.py`, `queries.py`, `mutations.py`, `__init__.py`
   - Import in `app/graphql/schema.py`
   - Add to root Query/Mutation classes

4. **Test GraphQL**
   - Visit `http://localhost:8000/graphql`
   - Use Playground to test queries and mutations
   - Check schema in Docs tab

## Security Best Practices

✅ **Implemented**

- Passwords hashed with bcrypt
- JWT tokens with expiration
- CORS configured by environment

❌ **To Implement**

- Rate limiting
- Input validation/sanitization
- HTTPS in production
- API key authentication option
- Refresh token rotation
- CSRF protection

## Next Steps

1. Create Project model and GraphQL module
2. Wire frontend to GraphQL API
3. Add Redis caching for frequently queried data
4. Implement rate limiting with slowapi
5. Add comprehensive error handling
6. Setup automated testing with pytest
7. Configure production deployment

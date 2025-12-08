# Backend Project Structure - Visual Overview

## Complete Directory Tree

```
backend/
│
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py              # Exports settings, database, security
│   │   ├── config.py                # Pydantic Settings (development/production)
│   │   ├── database.py              # SQLAlchemy engine, SessionLocal, Base
│   │   └── security.py              # JWT tokens, password hashing
│   │
│   ├── models/
│   │   ├── __init__.py              # Exports User model
│   │   └── user.py                  # User ORM model with all fields
│   │
│   ├── graphql/                     # MODULAR GRAPHQL STRUCTURE
│   │   ├── __init__.py              # Exports schema
│   │   ├── schema.py                # Root Query & Mutation combining modules
│   │   │
│   │   ├── auth/                    # Authentication Module
│   │   │   ├── __init__.py
│   │   │   ├── types.py             # TokenResponse, AuthPayload
│   │   │   ├── queries.py           # verify_token, current_user_id
│   │   │   └── mutations.py         # register, login, refresh_access_token
│   │   │
│   │   ├── user/                    # User Management Module
│   │   │   ├── __init__.py
│   │   │   ├── types.py             # UserType
│   │   │   ├── queries.py           # get_user, get_current_user, search_users
│   │   │   └── mutations.py         # update_profile, change_password
│   │   │
│   │   └── project/                 # Project Management Module (Extensible)
│   │       ├── __init__.py
│   │       ├── types.py             # ProjectType, ProjectStatus enum
│   │       ├── queries.py           # get_project, list_projects, search_projects
│   │       └── mutations.py         # create_project, update_project, delete_project
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py          # User CRUD, business logic
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── health.py                # Health check endpoint
│   │
│   └── utils/
│       ├── __init__.py
│       ├── validators.py            # Email, username, password validation
│       └── logger.py                # Logging configuration
│
├── alembic/                         # Database Migrations
│   ├── versions/
│   │   └── 91f4b6a33fb5_create_users_table.py
│   ├── env.py                       # Alembic environment (reads DATABASE_URL)
│   ├── alembic.ini                  # Alembic configuration
│   └── script.py.mako               # Migration template
│
├── main.py                          # FastAPI application entry point
│
├── .env                             # Development environment variables
├── .env.production                  # Production environment variables
├── .env.example                     # Template for team members
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Quick start & detailed setup guide
├── PROJECT_STRUCTURE.md             # Detailed structure documentation
├── SETUP_COMPLETE.md                # Setup summary
│
└── pytest.ini                       # Pytest configuration (optional)
```

## Module Breakdown

### 1. Core (`app/core/`)

Handles application configuration, database, and security:

```python
# config.py - Settings Management
settings = Settings()  # Loaded from .env

# database.py - ORM Setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# security.py - Authentication
jwt_token = create_access_token({"sub": user_id})
hashed = hash_password(plain_password)
verify_password(plain, hashed)  # -> bool
```

### 2. Models (`app/models/`)

SQLAlchemy ORM models:

```python
class User(Base):
    __tablename__ = "users"

    # Primary
    id: int (primary key)
    email: str (unique)
    username: str (unique)
    hashed_password: str

    # Profile
    full_name: str | None
    bio: str | None

    # Status
    is_active: bool
    is_verified: bool

    # Timestamps
    created_at: datetime
    updated_at: datetime
    last_login: datetime | None
```

### 3. GraphQL API (Modular)

Each feature has its own folder with types, queries, and mutations:

#### Auth Module (`graphql/auth/`)

```
Types:
  - TokenResponse(access_token, refresh_token, token_type)
  - AuthPayload(success, message, token)

Queries:
  - verify_token(token: str) -> bool
  - current_user_id(token: str) -> str | None

Mutations:
  - register(email, username, password, full_name) -> AuthPayload
  - login(email, password) -> AuthPayload
  - refresh_access_token(refresh_token) -> AuthPayload
```

#### User Module (`graphql/user/`)

```
Types:
  - UserType(id, email, username, full_name, bio, is_active, is_verified, created_at, updated_at, last_login)

Queries:
  - get_user(user_id) -> UserType | None
  - get_current_user(token) -> UserType | None
  - search_users(query, limit) -> [UserType]

Mutations:
  - update_profile(token, full_name, bio) -> UserType | None
  - change_password(token, old_password, new_password) -> bool
```

#### Project Module (`graphql/project/`)

```
Types:
  - ProjectStatus (enum): DRAFT, IN_PROGRESS, COMPLETED, ON_HOLD
  - ProjectType(id, code, title, description, status, owner_id, created_at, updated_at)

Queries:
  - get_project(project_id) -> ProjectType | None
  - list_projects(skip, limit) -> [ProjectType]
  - search_projects(query) -> [ProjectType]

Mutations:
  - create_project(title, code, description) -> ProjectType | None
  - update_project(project_id, title, description, status) -> ProjectType | None
  - delete_project(project_id) -> bool
```

### 4. Services (`app/services/`)

Business logic layer:

```python
class UserService:
    @staticmethod
    def get_user_by_id(db, user_id) -> User | None
    @staticmethod
    def get_user_by_email(db, email) -> User | None
    @staticmethod
    def create_user(db, email, username, password, full_name) -> User
    @staticmethod
    def update_user(db, user, **kwargs) -> User
    @staticmethod
    def list_users(db, skip, limit) -> [User]
```

### 5. Routers (`app/routers/`)

REST API endpoints (optional):

```python
# health.py
GET /api/health -> {"status": "ok", "message": "API is running"}
```

### 6. Utils (`app/utils/`)

Utility functions:

```python
# validators.py
validate_email(email) -> bool
validate_username(username) -> (bool, error_msg | None)
validate_password(password) -> (bool, error_msg | None)

# logger.py
get_logger(name) -> Logger
```

## API Endpoints

### REST Endpoints

- `GET /` - Root endpoint with API info
- `GET /api/health` - Health check
- `GET /docs` - Swagger documentation
- `GET /redoc` - ReDoc documentation

### GraphQL Endpoint

- `POST /graphql` - GraphQL queries and mutations
- `GET /graphql` - GraphQL Playground (dev mode)

## Database Schema

### Users Table

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    bio TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login DATETIME,
    INDEX (email),
    INDEX (username)
);
```

## Configuration Files

### `.env` (Development)

```env
ENV=development
DEBUG=true
DATABASE_URL=mysql+pymysql://root:root@localhost:3306/daisyui_db
SECRET_KEY=dev-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
LOG_LEVEL=INFO
```

### `.env.production` (Production)

```env
ENV=production
DEBUG=false
DATABASE_URL=mysql+pymysql://produser:prodpass@prod-db:3306/daisyui_db_prod
SECRET_KEY=<long-random-key>
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=14
LOG_LEVEL=WARNING
```

## Execution Flow

### Request Flow

```
Client Request
    ↓
FastAPI Router (main.py)
    ↓
CORS Middleware
    ↓
GraphQL Router (strawberry)
    ↓
Query/Mutation Handler
    ↓
GraphQL Context (db session injected)
    ↓
Service Layer (UserService, etc.)
    ↓
Database (SQLAlchemy ORM)
    ↓
MySQL
    ↓
Response → Client
```

### Authentication Flow

```
Register/Login
    ↓
Password Validation
    ↓
Generate Tokens (access + refresh)
    ↓
Return to Client
    ↓
Client Stores Token (localStorage)
    ↓
Subsequent Requests Include Token
    ↓
verify_token() checks JWT signature
    ↓
Extract user_id from payload
    ↓
Fetch User from DB
    ↓
Proceed with Request
```

## Modular GraphQL Design

Each GraphQL module (auth, user, project) can be developed independently:

1. **Create Module Folder**

   ```
   app/graphql/feature_name/
   ├── __init__.py
   ├── types.py
   ├── queries.py
   └── mutations.py
   ```

2. **Define Types**

   ```python
   # types.py
   @strawberry.type
   class FeatureType:
       id: int
       name: str
   ```

3. **Create Queries**

   ```python
   # queries.py
   @strawberry.type
   class FeatureQuery:
       @strawberry.field
       def get_feature(self, id: int) -> Optional[FeatureType]:
           ...
   ```

4. **Create Mutations**

   ```python
   # mutations.py
   @strawberry.type
   class FeatureMutation:
       @strawberry.mutation
       def create_feature(self, name: str) -> FeatureType:
           ...
   ```

5. **Add to Root Schema**

   ```python
   # app/graphql/schema.py
   @strawberry.type
   class Query(FeatureQuery, ...):
       pass

   @strawberry.type
   class Mutation(FeatureMutation, ...):
       pass

   schema = strawberry.Schema(query=Query, mutation=Mutation)
   ```

## Key Technologies

| Layer         | Technology        | Purpose                              |
| ------------- | ----------------- | ------------------------------------ |
| API Framework | FastAPI           | Web framework with async support     |
| GraphQL       | Strawberry        | Type-safe GraphQL implementation     |
| Database      | MySQL             | Primary data store                   |
| ORM           | SQLAlchemy 2.0    | Object-relational mapping            |
| Migrations    | Alembic           | Database version control             |
| Auth          | PyJWT             | JSON Web Token creation/verification |
| Hashing       | Passlib + bcrypt  | Password hashing                     |
| Config        | Pydantic-Settings | Environment-based configuration      |
| Server        | Uvicorn           | ASGI application server              |

## Development Workflow

1. **Create Model** → `app/models/`
2. **Generate Migration** → `alembic revision --autogenerate`
3. **Run Migration** → `alembic upgrade head`
4. **Create Service** → `app/services/`
5. **Create GraphQL Module** → `app/graphql/feature/`
6. **Add to Schema** → Update `app/graphql/schema.py`
7. **Test in GraphQL IDE** → Visit `/graphql`

---

**Project Setup Complete** ✅
Ready for development and deployment!

# Quick Reference Guide

## 🚀 Start Server

```powershell
cd backend
venv\Scripts\python -m uvicorn main:app --reload
```

**Access:**

- API: http://localhost:8000
- GraphQL: http://localhost:8000/graphql
- Docs: http://localhost:8000/docs

---

## 📁 Add New GraphQL Feature

### Step 1: Create Module Folder

```powershell
mkdir app\graphql\feature_name
```

### Step 2: Create Files

```
app/graphql/feature_name/
├── __init__.py
├── types.py      # Define data types
├── queries.py    # Define read operations
└── mutations.py  # Define write operations
```

### Step 3: Define Type

```python
# types.py
import strawberry

@strawberry.type
class FeatureType:
    id: int
    name: str
```

### Step 4: Define Queries

```python
# queries.py
import strawberry
from typing import Optional

@strawberry.type
class FeatureQuery:
    @strawberry.field
    def get_feature(self, id: int) -> Optional[FeatureType]:
        db = info.context["db"]
        # Query database
        return FeatureType(id=1, name="example")
```

### Step 5: Define Mutations

```python
# mutations.py
import strawberry

@strawberry.type
class FeatureMutation:
    @strawberry.mutation
    def create_feature(self, name: str) -> FeatureType:
        db = info.context["db"]
        # Write to database
        return FeatureType(id=1, name=name)
```

### Step 6: Add to Schema

```python
# app/graphql/schema.py
from app.graphql.feature_name import FeatureQuery, FeatureMutation

@strawberry.type
class Query(FeatureQuery, AuthQuery, UserQuery, ProjectQuery):
    pass

@strawberry.type
class Mutation(FeatureMutation, AuthMutation, UserMutation, ProjectMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
```

---

## 🗄️ Database Operations

### Create Migration After Model Change

```powershell
venv\Scripts\python -m alembic revision --autogenerate -m "add feature field"
```

### Apply Migrations

```powershell
venv\Scripts\python -m alembic upgrade head
```

### Rollback Last Migration

```powershell
venv\Scripts\python -m alembic downgrade -1
```

### View Migration History

```powershell
venv\Scripts\python -m alembic history
```

---

## 🔐 Authentication Flow

### User Registration

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

### User Login

```graphql
mutation {
  login(email: "user@example.com", password: "SecurePass123") {
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

### Get Current User

```graphql
{
  getCurrentUser(token: "your_access_token") {
    id
    email
    username
    fullName
    isActive
    createdAt
  }
}
```

### Refresh Token

```graphql
mutation {
  refreshAccessToken(refreshToken: "your_refresh_token") {
    success
    message
    token {
      accessToken
      refreshToken
    }
  }
}
```

---

## 📊 Common GraphQL Queries

### Search Users

```graphql
{
  searchUsers(query: "john", limit: 10) {
    id
    email
    username
    fullName
  }
}
```

### Update User Profile

```graphql
mutation {
  updateProfile(
    token: "access_token"
    fullName: "Jane Doe"
    bio: "Software Engineer"
  ) {
    id
    email
    fullName
    bio
  }
}
```

### Change Password

```graphql
mutation {
  changePassword(
    token: "access_token"
    oldPassword: "OldPass123"
    newPassword: "NewPass456"
  )
}
```

---

## 🛠️ Environment Variables

### Development (.env)

```env
ENV=development
DEBUG=true
DATABASE_URL=mysql+pymysql://root:root@localhost:3306/daisyui_db
SECRET_KEY=your-dev-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Production (.env.production)

```env
ENV=production
DEBUG=false
DATABASE_URL=mysql+pymysql://user:password@prod-db:3306/daisyui_db_prod
SECRET_KEY=long-random-production-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 📦 Installation & Setup

### First Time Setup

```powershell
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env from .env.example
copy .env.example .env

# Create database
mysql -u root -p -e "CREATE DATABASE daisyui_db;"

# Run migrations
venv\Scripts\python -m alembic upgrade head

# Start server
venv\Scripts\python -m uvicorn main:app --reload
```

---

## 🔍 Troubleshooting

### Server Won't Start

```powershell
# Check Python version (3.9+)
python --version

# Verify dependencies
pip list | findstr "fastapi strawberry sqlalchemy"

# Check .env file exists
type .env
```

### Database Connection Error

```powershell
# Verify MySQL is running
mysql -u root -p -e "SELECT 1;"

# Check DATABASE_URL in .env
type .env | findstr "DATABASE_URL"

# Verify database exists
mysql -u root -p -e "SHOW DATABASES;"
```

### GraphQL Schema Error

```powershell
# Check for import errors
venv\Scripts\python -c "from app.graphql.schema import schema; print('Schema OK')"

# Verify all modules import
venv\Scripts\python -c "from app.graphql import auth, user, project; print('Modules OK')"
```

---

## 📚 File Structure Quick Reference

```
backend/
├── app/core/              → Database, config, security
├── app/models/            → ORM models
├── app/graphql/           → GraphQL API (modular)
│   ├── auth/              → Authentication
│   ├── user/              → User management
│   └── project/           → Projects
├── app/services/          → Business logic
├── app/routers/           → REST endpoints
├── app/utils/             → Helpers
├── alembic/               → Migrations
├── .env                   → Config (git ignored)
├── main.py                → FastAPI app
└── requirements.txt       → Dependencies
```

---

## ⚡ Performance Tips

1. **Use DB Sessions Properly**

   - Always close sessions in finally blocks
   - Use context managers when possible

2. **GraphQL Query Optimization**

   - Use `limit` parameter for list queries
   - Avoid N+1 queries with eager loading

3. **Caching (Optional)**

   - Redis integration ready in config
   - Implement caching for frequently accessed data

4. **Database Indexing**
   - User model has indexes on email and username
   - Add indexes to frequently filtered columns

---

## 🧪 Testing

### Run Tests

```powershell
venv\Scripts\pytest tests/
```

### Test with Coverage

```powershell
venv\Scripts\pytest --cov=app tests/
```

### Test GraphQL Query

```powershell
# Using GraphQL IDE at http://localhost:8000/graphql
# Or use curl
curl -X POST http://localhost:8000/graphql `
  -H "Content-Type: application/json" `
  -d '{"query":"{ hello }"}'
```

---

## 📖 Documentation Files

- `README.md` - Setup and running guide
- `PROJECT_STRUCTURE.md` - Detailed project structure
- `STRUCTURE_VISUAL.md` - Visual structure overview
- `SETUP_COMPLETE.md` - Setup completion summary
- `QUICK_REFERENCE.md` - This file!

---

## 🚀 Deployment Checklist

- [ ] Update SECRET_KEY in production
- [ ] Set DEBUG=false in production
- [ ] Update DATABASE_URL to production database
- [ ] Update CORS_ORIGINS with production domain
- [ ] Set up HTTPS/SSL certificate
- [ ] Configure reverse proxy (Nginx)
- [ ] Set up logging and monitoring
- [ ] Enable rate limiting
- [ ] Backup database regularly

---

## 💡 Pro Tips

1. **Database Transactions**

   ```python
   db.begin()
   try:
       # Multiple operations
       db.commit()
   except:
       db.rollback()
   ```

2. **Error Handling**

   ```python
   try:
       # Operation
   except SQLAlchemyError as e:
       return {"success": False, "message": str(e)}
   ```

3. **Async Operations**
   FastAPI supports async - use for I/O bound tasks

   ```python
   @app.get("/async-endpoint")
   async def async_endpoint():
       # Async code here
       return result
   ```

4. **Type Hints**
   Always use type hints for better IDE support
   ```python
   def get_user(user_id: int, db: Session) -> User | None:
       return db.query(User).filter(User.id == user_id).first()
   ```

---

**Last Updated**: December 8, 2025
**Status**: ✅ Ready for Production

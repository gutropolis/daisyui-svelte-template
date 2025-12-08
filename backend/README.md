# Backend Setup & Running Guide (Windows)

## Prerequisites

- Python 3.9+
- MySQL Server running
- pip (Python package manager)
- Virtual Environment (venv)

## Quick Start (5 minutes)

### 1. Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` to `.env` and update database credentials if needed.

### 4. Run Migrations

```powershell
.\venv\Scripts\python -m alembic upgrade head
```

### 5. Start Server

```powershell
.\venv\Scripts\python -m uvicorn main:app --reload
```

Access:

- API: `http://localhost:8000`
- GraphQL Playground: `http://localhost:8000/graphql`
- Docs: `http://localhost:8000/docs`

---

## Detailed Setup Guide

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Virtual Environment (venv)
- MySQL Server

## Initial Setup

### 1. Create Virtual Environment

```powershell
python -m venv venv
```

### 2. Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

Or install individual packages:

```powershell
pip install fastapi uvicorn sqlalchemy strawberry-graphql alembic passlib python-jose pydantic-settings cryptography pymysql
```

## Database Setup

### 1. MySQL Database

Ensure MySQL is running and create the database:

```sql
CREATE DATABASE IF NOT EXISTS daisyui_db;
```

### 2. Configure Database Connection

Edit `.env` file:

```env
DATABASE_URL=mysql+pymysql://root:root@localhost:3306/daisyui_db
```

Replace `root:root` with your MySQL credentials.

### 3. Create Database Migrations

First time only:

```powershell
.\venv\Scripts\python -m alembic init alembic
```

After model changes:

```powershell
.\venv\Scripts\python -m alembic revision --autogenerate -m "description of change"
```

### 4. Run Migrations

Apply all pending migrations:

```powershell
.\venv\Scripts\python -m alembic history
.\venv\Scripts\python -m alembic upgrade head
```

Rollback last migration:

```powershell
.\venv\Scripts\python -m alembic downgrade -1
```

Verify tables created:

```powershell
.\venv\Scripts\python -c "from sqlalchemy import text; from app.core.database import engine; conn = engine.connect(); result = conn.execute(text('SHOW TABLES')); print([row[0] for row in result]); conn.close()"
```

## Environment Configuration

### Development (`.env`)

```env
ENV=development
DEBUG=true
DATABASE_URL=mysql+pymysql://root:root@localhost:3306/daisyui_db
SECRET_KEY=dev-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

### Production (`.env.production`)

```env
ENV=production
DEBUG=false
DATABASE_URL=mysql+pymysql://produser:prodpass@prod-db:3306/daisyui_db_prod
SECRET_KEY=<long-random-secret-key>
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=14
```

## Running the Application

### Development Server (with auto-reload)

```powershell
.\venv\Scripts\python -m uvicorn main:app --reload
```

### Production Server

```powershell
.\venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Or using the main.py script:

```powershell
.\venv\Scripts\python main.py
```

## Accessing the API

Once running:

- **API Root**: `http://localhost:8000`
- **GraphQL Endpoint**: `http://localhost:8000/graphql`
- **Auto Docs (Swagger)**: `http://localhost:8000/docs`
- **Alternative Docs (ReDoc)**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/api/health`

## Project Structure

See `PROJECT_STRUCTURE.md` for detailed information about:

- Directory layout
- Module responsibilities
- Database & ORM setup
- Authentication flow
- GraphQL API examples
- Development workflow

## GraphQL Examples

### Register User

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
  getCurrentUser(token: "your_access_token_here") {
    id
    email
    username
    fullName
    isActive
    createdAt
  }
}
```

## Troubleshooting

### "No module named 'app'"

- Ensure you're running from the `backend/` directory
- Verify virtual environment is activated
- Check `PYTHONPATH` includes project root

### "sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) ..."

- Verify MySQL is running
- Check DATABASE_URL in `.env`
- Verify database exists: `mysql -u root -p -e "SHOW DATABASES;"`

### "ModuleNotFoundError: No module named 'pydantic_settings'"

- Run: `pip install pydantic-settings`

### Alembic still using SQLite

- Check `.env` DATABASE_URL is set correctly
- Verify `alembic/env.py` reads from `.env`
- Run migration with: `.\venv\Scripts\python -m alembic upgrade head`

### "Context impl SQLiteImpl"

- This means Alembic is using SQLite instead of MySQL
- Verify `alembic.ini` has correct database URL
- Check `DATABASE_URL` environment variable is set
- See Alembic Configuration section below

## Alembic Configuration

### Configuration File (`alembic.ini`)

Key settings:

```ini
sqlalchemy.url = mysql+pymysql://root:root@localhost:3306/daisyui_db
```

### Environment Setup (`alembic/env.py`)

The env.py file reads the DATABASE_URL from:

1. Environment variable `DATABASE_URL`
2. Falls back to `alembic.ini` sqlalchemy.url

Make sure your `.env` file has DATABASE_URL set.

## Dependencies

### Core Framework

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `strawberry-graphql` - GraphQL

### Database

- `sqlalchemy` - ORM
- `alembic` - Migrations
- `pymysql` - MySQL driver

### Authentication

- `passlib` - Password hashing
- `python-jose` - JWT tokens
- `cryptography` - Encryption

### Configuration

- `pydantic` - Data validation
- `pydantic-settings` - Environment config
- `python-dotenv` - .env file support

## Common Commands

```powershell
# Activate environment
.\venv\Scripts\Activate.ps1

# Deactivate environment
deactivate

# Install requirements
pip install -r requirements.txt

# Add new package
pip install package_name

# Generate requirements file
pip freeze > requirements.txt

# Run migrations
.\venv\Scripts\python -m alembic upgrade head

# Create new migration
.\venv\Scripts\python -m alembic revision --autogenerate -m "message"

# Start development server
.\venv\Scripts\python -m uvicorn main:app --reload

# Check code style (if using pylint)
.\venv\Scripts\pylint app/

# Run tests (if using pytest)
.\venv\Scripts\pytest tests/
```

## Production Deployment

1. **Set environment to production**

   ```powershell
   # In .env.production
   ENV=production
   DEBUG=false
   ```

2. **Use production settings**

   ```powershell
   $env:ENV = "production"
   ```

3. **Run with production server**

   ```powershell
   .\venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

4. **Use a reverse proxy** (Nginx/Apache)
   - Forward requests to FastAPI running on 127.0.0.1:8000
   - Handle SSL/TLS certificates

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Strawberry GraphQL Docs](https://strawberry.rocks/)
- [SQLAlchemy ORM Docs](https://docs.sqlalchemy.org/)
- [Alembic Docs](https://alembic.sqlalchemy.org/)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

## Support & Debugging

For detailed project structure and development workflow:

- See `PROJECT_STRUCTURE.md`

For specific errors or issues:

- Check logs in console output
- Verify all dependencies installed
- Ensure MySQL service is running
- Check `.env` file configurationAfter modifying models, generate a migration:

```powershell
.\venv\Scripts\python -m alembic revision --autogenerate -m "describe your changes"
```

Example:

```powershell
.\venv\Scripts\python -m alembic revision --autogenerate -m "create users table"
```

### 3. Apply Migrations

```powershell
.\venv\Scripts\python -m alembic upgrade head
```

To rollback the last migration:

```powershell
.\venv\Scripts\python -m alembic downgrade -1
```

## Running the Backend

### Start Development Server

```powershell
.\venv\Scripts\python -m uvicorn main:app --reload
```

The server will start at: `http://localhost:8000`

### Access GraphQL Playground

Navigate to: `http://localhost:8000/graphql`

### View API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── main.py                 # FastAPI app entry point
├── alembic/               # Database migrations
│   ├── versions/          # Migration files
│   └── env.py            # Alembic configuration
├── app/
│   ├── core/
│   │   └── database.py    # SQLAlchemy setup
│   ├── models/
│   │   └── user.py        # User model
│   ├── graphql/
│   │   ├── schema.py      # GraphQL schema
│   │   └── __init__.py
│   └── __init__.py
├── venv/                  # Virtual environment
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Common Commands Reference

### Package Management

```powershell
# Install a package
pip install package-name

# Install from requirements
pip install -r requirements.txt

# Freeze current packages
pip freeze > requirements.txt

# List installed packages
pip list
```

### Database Operations

```powershell
# View current migration version
.\venv\Scripts\python -m alembic current

# View migration history
.\venv\Scripts\python -m alembic history

# Create migration script
.\venv\Scripts\python -m alembic revision -m "migration name"

# Apply all pending migrations
.\venv\Scripts\python -m alembic upgrade head

# Revert one migration
.\venv\Scripts\python -m alembic downgrade -1

# Revert to specific revision
.\venv\Scripts\python -m alembic downgrade <revision_id>
```

### Development Server

```powershell
# Start with auto-reload
.\venv\Scripts\python -m uvicorn main:app --reload

# Start on custom port
.\venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8001

# Run without reload (production-like)
.\venv\Scripts\python -m uvicorn main:app
```

## Troubleshooting

### Virtual Environment Issues

**Error: "venv not activated"**

```powershell
# Make sure to activate it:
.\venv\Scripts\Activate.ps1
```

**Error: "Python not found"**

- Ensure Python is installed and in PATH
- Use `python --version` to check

### Database Issues

**Error: "No migrations applied"**

```powershell
# Check migration status
.\venv\Scripts\python -m alembic current

# Apply migrations
.\venv\Scripts\python -m alembic upgrade head
```

**Error: "Could not find alembic"**

```powershell
# Reinstall in virtual environment
.\venv\Scripts\pip install alembic sqlalchemy
```

### Port Already in Use

If port 8000 is already in use:

```powershell
# Use a different port
.\venv\Scripts\python -m uvicorn main:app --port 8001 --reload
```

## Environment Variables

Create a `.env` file in the backend folder for configuration:

```
DATABASE_URL=sqlite:///./test.db
DEBUG=True
```

Load variables using `python-dotenv`:

```powershell
pip install python-dotenv
```

Then in your Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_URL")
```

## Next Steps

1. ✅ Backend server running
2. ⏳ Connect frontend to GraphQL API
3. ⏳ Add authentication & authorization
4. ⏳ Deploy to production

## Notes

- Always activate the virtual environment before running commands
- Use `pip freeze > requirements.txt` to update dependencies
- Keep migrations under version control
- Never commit `venv/` folder to git

# MySQL Database Migration Guide

## Current Status

✅ **Tables Created:**

- `alembic_version` - Alembic metadata table
- `users` - User authentication and profile table

## Migration Commands

### 1. View Migration History

```powershell
venv\Scripts\python -m alembic history
```

Shows all migrations applied and their status.

### 2. View Current Database Revision

```powershell
venv\Scripts\python -m alembic current
```

Shows which migration is currently applied.

### 3. Generate New Migration (After Model Changes)

```powershell
venv\Scripts\python -m alembic revision --autogenerate -m "description of change"
```

Example:

```powershell
venv\Scripts\python -m alembic revision --autogenerate -m "add phone field to users"
```

### 4. Apply All Pending Migrations (Most Common)

```powershell
venv\Scripts\python -m alembic upgrade head
```

Applies all migrations up to the latest version.

### 5. Apply Specific Number of Migrations

```powershell
venv\Scripts\python -m alembic upgrade +1
```

Applies next 1 migration.

### 6. Rollback Last Migration

```powershell
venv\Scripts\python -m alembic downgrade -1
```

Reverts the last applied migration.

### 7. Rollback Multiple Migrations

```powershell
venv\Scripts\python -m alembic downgrade -2
```

Reverts last 2 migrations.

### 8. Downgrade to Specific Revision

```powershell
venv\Scripts\python -m alembic downgrade 91f4b6a33fb5
```

Reverts to a specific migration version.

## Workflow: Add New Table/Field

### Step 1: Create SQLAlchemy Model

```python
# app/models/project.py
from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    code = Column(String(50), unique=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
```

### Step 2: Generate Migration

```powershell
venv\Scripts\python -m alembic revision --autogenerate -m "add projects table"
```

### Step 3: Review Migration File

Check `alembic/versions/` for the generated file and verify it looks correct.

### Step 4: Apply Migration

```powershell
venv\Scripts\python -m alembic upgrade head
```

### Step 5: Verify Table Created

```powershell
venv\Scripts\python -c "from sqlalchemy import text; from app.core.database import engine; conn = engine.connect(); result = conn.execute(text('SHOW TABLES')); print([row[0] for row in result]); conn.close()"
```

## Complete Migration Checklist

### Before Running Migrations

- [ ] MySQL server is running
- [ ] Database exists (`daisyui_db`)
- [ ] `.env` file has correct DATABASE_URL
- [ ] All models are defined in `app/models/`
- [ ] Virtual environment is activated

### Running Migrations

- [ ] Generate auto-migration: `alembic revision --autogenerate -m "..."`
- [ ] Review migration file in `alembic/versions/`
- [ ] Run migration: `alembic upgrade head`
- [ ] Verify tables created: `SHOW TABLES`
- [ ] Check table structure: `DESCRIBE table_name`

### After Migrations

- [ ] Restart FastAPI server
- [ ] Test GraphQL queries/mutations
- [ ] Verify data integrity

## MySQL Commands for Verification

### Check All Tables

```sql
SHOW TABLES;
```

### Check Table Structure

```sql
DESCRIBE users;
```

Or:

```sql
SHOW CREATE TABLE users;
```

### Check Indexes

```sql
SHOW INDEXES FROM users;
```

### Check Current Database

```sql
SELECT DATABASE();
```

### Check Alembic Version

```sql
SELECT * FROM alembic_version;
```

## Troubleshooting

### Migration Not Applied

```powershell
# Check current status
venv\Scripts\python -m alembic current

# Force upgrade
venv\Scripts\python -m alembic upgrade head
```

### Table Not Found After Migration

```powershell
# Verify migration was applied
venv\Scripts\python -m alembic current

# Check database
mysql -u root -p daisyui_db -e "SHOW TABLES;"
```

### Rollback Everything and Start Fresh

```powershell
# Downgrade to base
venv\Scripts\python -m alembic downgrade base

# Delete database
mysql -u root -p -e "DROP DATABASE daisyui_db; CREATE DATABASE daisyui_db;"

# Run all migrations again
venv\Scripts\python -m alembic upgrade head
```

## Best Practices

1. **Always review migration files** before applying them
2. **Test migrations in development first** before production
3. **Keep one model per file** for clarity
4. **Use descriptive migration messages**
5. **Never manually edit migration files** in production
6. **Backup database** before major migrations

## Quick Command Reference

| Task                 | Command                                    |
| -------------------- | ------------------------------------------ |
| View history         | `alembic history`                          |
| View current         | `alembic current`                          |
| Create migration     | `alembic revision --autogenerate -m "msg"` |
| Apply all            | `alembic upgrade head`                     |
| Apply one            | `alembic upgrade +1`                       |
| Rollback one         | `alembic downgrade -1`                     |
| Rollback to base     | `alembic downgrade base`                   |
| Show table structure | `DESCRIBE table_name`                      |
| Show all tables      | `SHOW TABLES`                              |

## Current Database Schema

### Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    bio TEXT,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    is_verified BOOLEAN NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login DATETIME,
    INDEX ix_users_email (email),
    INDEX ix_users_id (id)
);
```

## Next Steps

### To Add More Tables:

1. Create model in `app/models/`
2. Import in `app/models/__init__.py`
3. Run: `venv\Scripts\python -m alembic revision --autogenerate -m "add table name"`
4. Run: `venv\Scripts\python -m alembic upgrade head`

### Example Models to Add:

- Project model
- Team model
- Enrollment model
- Audit log model

---

**Status**: ✅ All migrations applied successfully
**Current Database**: daisyui_db
**Tables**: alembic_version, users

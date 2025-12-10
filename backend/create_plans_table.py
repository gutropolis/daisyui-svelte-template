"""Create plans table in database."""
import sys
sys.path.insert(0, '/E:/project/daisyui-svelte-template/backend')

from app.core.database import engine, Base
from app.models.plan import Plan

# Create the table
Base.metadata.create_all(bind=engine)

print("✅ Plans table created successfully!")
print(f"   Table name: {Plan.__tablename__}")
print(f"   Columns: {len(Plan.__table__.columns)}")
print("\n   Columns:")
for col in Plan.__table__.columns:
    print(f"   - {col.name}: {col.type}")

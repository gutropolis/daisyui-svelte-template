"""Add sample plans data."""
import sys
import json
sys.path.insert(0, '/E:/project/daisyui-svelte-template/backend')

from app.core.database import SessionLocal
from app.models.plan import Plan

db = SessionLocal()

# Sample plans
sample_plans = [
    {
        "slug": "free",
        "name": "Free Plan",
        "price": 0,
        "duration_days": 30,
        "max_users": 1,
        "max_studies": 5,
        "max_storage_gb": 1,
        "features": [1, 2],  # Basic features
    },
    {
        "slug": "pro",
        "name": "Pro Plan",
        "price": 29.99,
        "duration_days": 30,
        "max_users": 5,
        "max_studies": 50,
        "max_storage_gb": 100,
        "features": [1, 2, 3, 4],  # All features
    },
    {
        "slug": "enterprise",
        "name": "Enterprise Plan",
        "price": 99.99,
        "duration_days": 365,
        "max_users": None,  # Unlimited
        "max_studies": None,  # Unlimited
        "max_storage_gb": None,  # Unlimited
        "features": [1, 2, 3, 4, 5],  # All features
    },
]

try:
    for plan_data in sample_plans:
        # Check if plan exists
        existing = db.query(Plan).filter(Plan.slug == plan_data["slug"]).first()
        if not existing:
            features_json = json.dumps(plan_data["features"]) if plan_data["features"] else None
            plan = Plan(
                slug=plan_data["slug"],
                name=plan_data["name"],
                price=plan_data["price"],
                duration_days=plan_data["duration_days"],
                max_users=plan_data["max_users"],
                max_studies=plan_data["max_studies"],
                max_storage_gb=plan_data["max_storage_gb"],
                features=features_json,
            )
            db.add(plan)
            print(f"✅ Added plan: {plan_data['name']}")
        else:
            print(f"⚠️  Plan already exists: {plan_data['name']}")
    
    db.commit()
    print("\n✅ Sample plans added successfully!")
    
    # Display all plans
    all_plans = db.query(Plan).all()
    print(f"\n📊 Total plans in database: {len(all_plans)}")
    for plan in all_plans:
        print(f"   - {plan.name} (${plan.price}/month, {plan.duration_days} days)")

except Exception as e:
    db.rollback()
    print(f"❌ Error: {str(e)}")
finally:
    db.close()

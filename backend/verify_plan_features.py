"""Verify plan_features table exists and test GraphQL"""

import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="2026_fastdb"
)

cursor = connection.cursor()

# Show all tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("✅ All tables in database:")
for table in tables:
    print(f"  ✓ {table[0]}")

# Check plan_features specifically
cursor.execute("SELECT COUNT(*) FROM plan_features")
count = cursor.fetchone()
print(f"\n✅ plan_features table exists with {count[0]} rows")

# Show structure
cursor.execute("DESCRIBE plan_features")
columns = cursor.fetchall()
print("\n📋 Table Structure:")
print("─" * 80)
for col in columns:
    col_name, col_type, nullable, key, default, extra = col
    print(f"  {col_name:20} {col_type:25} nullable={str(nullable):5} key={str(key):3}")

cursor.close()
connection.close()

print("\n🎉 Ready to use! You can now:")
print("  1. Start backend: python -m uvicorn main:app --reload --port 8000")
print("  2. Visit: http://localhost:8000/graphql")
print("  3. Create a feature with GraphQL mutations")

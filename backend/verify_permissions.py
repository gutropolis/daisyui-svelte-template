#!/usr/bin/env python3
"""Verify permissions table and add sample data"""

import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
DB_NAME = os.getenv('DB_NAME', '2026_fastdb')

print("=" * 70)
print("PERMISSIONS TABLE VERIFICATION & SETUP")
print("=" * 70)

try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    with connection.cursor() as cursor:
        # 1. Check tables exist
        print("\n📋 CHECKING TABLES...")
        cursor.execute("SHOW TABLES")
        tables = [t[list(t.keys())[0]] for t in cursor.fetchall()]
        
        required_tables = ['plan_features', 'permissions']
        for table in required_tables:
            if table in tables:
                print(f"  ✅ {table}")
            else:
                print(f"  ❌ {table} - NOT FOUND")
        
        # 2. Check permissions table structure
        print("\n📊 PERMISSIONS TABLE STRUCTURE...")
        cursor.execute("DESCRIBE permissions")
        columns = cursor.fetchall()
        for col in columns:
            null_str = 'NOT NULL' if col['Null'] == 'NO' else 'NULL'
            key_str = f"[{col['Key']}]" if col['Key'] else ""
            print(f"  {col['Field']:<20} {col['Type']:<25} {null_str:<10} {key_str}")
        
        # 3. Check plan_features count
        print("\n📈 DATA COUNTS...")
        cursor.execute("SELECT COUNT(*) as count FROM plan_features")
        pf_count = cursor.fetchone()['count']
        print(f"  plan_features: {pf_count} rows")
        
        cursor.execute("SELECT COUNT(*) as count FROM permissions")
        perm_count = cursor.fetchone()['count']
        print(f"  permissions: {perm_count} rows")
        
        # 4. If no permissions, add sample data
        if pf_count > 0 and perm_count == 0:
            print("\n➕ ADDING SAMPLE PERMISSIONS...")
            
            # Get first plan feature
            cursor.execute("SELECT id FROM plan_features LIMIT 1")
            feature = cursor.fetchone()
            if feature:
                feature_id = feature['id']
                
                sample_permissions = [
                    ('permission.create', 'Create Permission', '➕', feature_id),
                    ('permission.read', 'Read Permission', '👁️', feature_id),
                    ('permission.update', 'Update Permission', '✏️', feature_id),
                    ('permission.delete', 'Delete Permission', '🗑️', feature_id),
                ]
                
                for key_name, name, icon, fid in sample_permissions:
                    try:
                        cursor.execute(
                            """INSERT INTO permissions (key_name, name, icon, feature_id, description)
                               VALUES (%s, %s, %s, %s, %s)""",
                            (key_name, name, icon, fid, f"Permission to {name.lower()}")
                        )
                        print(f"  ✅ Added: {key_name}")
                    except pymysql.Error as e:
                        if 'Duplicate' in str(e):
                            print(f"  ⏭️  Skipped (exists): {key_name}")
                        else:
                            print(f"  ❌ Error: {key_name} - {e}")
                
                connection.commit()
                print("\n✅ Sample data added successfully!")
        
        # 5. Display existing permissions
        print("\n📋 EXISTING PERMISSIONS:")
        cursor.execute("""
            SELECT p.id, p.key_name, p.name, p.icon, p.feature_id, 
                   pf.name as feature_name, p.created_at
            FROM permissions p
            LEFT JOIN plan_features pf ON p.feature_id = pf.id
            ORDER BY p.created_at DESC
            LIMIT 10
        """)
        
        permissions = cursor.fetchall()
        if permissions:
            print(f"\n  {'ID':<5} {'Key Name':<25} {'Name':<25} {'Icon':<5} {'Feature':<15}")
            print("  " + "-" * 75)
            for perm in permissions:
                print(f"  {perm['id']:<5} {perm['key_name']:<25} {perm['name']:<25} {perm['icon']:<5} {perm['feature_name']:<15}")
        else:
            print("  (No permissions yet)")
        
        print("\n" + "=" * 70)
        print("✅ VERIFICATION COMPLETE - BACKEND READY FOR GRAPHQL")
        print("=" * 70)
        
except pymysql.Error as e:
    print(f"\n❌ Database Error: {e}")
    exit(1)
finally:
    connection.close()

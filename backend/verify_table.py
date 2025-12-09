#!/usr/bin/env python
"""Quick test to verify plan_features table exists."""
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Get database config
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "2026_fastdb")

try:
    # Connect to database
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    
    # Check if plan_features table exists
    cursor.execute("""
        SELECT TABLE_NAME 
        FROM information_schema.TABLES 
        WHERE TABLE_SCHEMA = %s 
        AND TABLE_NAME = 'plan_features'
    """, (DB_NAME,))
    
    result = cursor.fetchone()
    
    if result:
        print("✅ SUCCESS! plan_features table EXISTS in database")
        
        # Get table structure
        cursor.execute("DESCRIBE plan_features")
        columns = cursor.fetchall()
        
        print("\nTable Structure:")
        print("─" * 60)
        for col in columns:
            col_name, col_type, nullable, key, default, extra = col
            print(f"  {col_name:20} {col_type:20} {nullable:8} {key or '':8}")
        
        # Get all tables
        cursor.execute("SHOW TABLES")
        all_tables = cursor.fetchall()
        print(f"\nTotal tables in database: {len(all_tables)}")
        
    else:
        print("❌ ERROR! plan_features table NOT FOUND in database")
        print(f"\nDatabase: {DB_NAME}")
        print(f"Host: {DB_HOST}")
        
        # Show all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"\nTables found ({len(tables)}):")
        for table in tables:
            print(f"  - {table[0]}")
    
    cursor.close()
    conn.close()

except Exception as e:
    print(f"❌ Connection Error: {e}")
    print("\nMake sure:")
    print("  1. MySQL is running")
    print("  2. Database credentials in .env are correct")
    print("  3. Database exists")


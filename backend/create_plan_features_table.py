"""Create plan_features table manually

This is a workaround for the migration that didn't actually create the table.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Use these hardcoded values based on .env
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"  # From DATABASE_URL in .env
DB_NAME = "2026_fastdb"

# Create connection using pymysql
import pymysql

connection = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = connection.cursor()

# SQL to create the table
sql = """
CREATE TABLE IF NOT EXISTS plan_features (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    key_name VARCHAR(100) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX ix_plan_features_id (id),
    INDEX ix_plan_features_key_name (key_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

try:
    cursor.execute(sql)
    connection.commit()
    print("✅ SUCCESS! plan_features table created")
    
    # Verify the table exists
    cursor.execute("DESCRIBE plan_features")
    columns = cursor.fetchall()
    print("\nTable Structure:")
    for col in columns:
        print(f"  {col[0]:20} {col[1]:30}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()

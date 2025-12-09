import pymysql
from pymysql import cursors

# Database configuration
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': '2026_fastdb',
}

try:
    # Connect to database
    connection = pymysql.connect(**config)
    cursor = connection.cursor()

    # Create permissions table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS permissions (
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        key_name VARCHAR(150) UNIQUE NOT NULL,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        icon VARCHAR(100),
        feature_id BIGINT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (feature_id) REFERENCES plan_features(id),
        INDEX ix_permissions_key_name (key_name),
        INDEX ix_permissions_feature_id (feature_id)
    );
    """

    cursor.execute(create_table_sql)
    connection.commit()
    print("✅ Permissions table created successfully!")

    # Verify table creation
    cursor.execute("SHOW TABLES LIKE 'permissions'")
    result = cursor.fetchone()
    if result:
        print("✅ Table verified in database")

        # Get table structure
        cursor.execute("DESCRIBE permissions")
        columns = cursor.fetchall()
        print("\n📋 Table Structure:")
        print(f"{'Column':<20} {'Type':<25} {'Null':<8} {'Key':<10}")
        print("-" * 63)
        for col in columns:
            print(f"{col[0]:<20} {col[1]:<25} {col[2]:<8} {col[3]:<10}")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()

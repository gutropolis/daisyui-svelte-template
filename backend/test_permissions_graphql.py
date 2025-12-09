#!/usr/bin/env python3
"""Test Permissions GraphQL API"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

GRAPHQL_URL = os.getenv('GRAPHQL_URL', 'http://localhost:8000/graphql')

print("=" * 70)
print("TESTING PERMISSIONS GRAPHQL API")
print("=" * 70)
print(f"API URL: {GRAPHQL_URL}\n")

# Test 1: Get all permissions with pagination
print("TEST 1: Get all permissions with pagination")
print("-" * 70)

query_all = """
query {
  permissions(page: 1, limit: 10) {
    success
    message
    data {
      id
      keyName
      name
      icon
      featureId
      description
      createdAt
      updatedAt
    }
    pagination {
      page
      limit
      total
      totalPages
      hasNext
      hasPrev
    }
  }
}
"""

try:
    response = requests.post(
        GRAPHQL_URL,
        json={"query": query_all},
        headers={"Content-Type": "application/json"},
        timeout=5
    )
    
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            print(f"❌ GraphQL Error: {data['errors']}")
        else:
            result = data.get('data', {}).get('permissions', {})
            print(f"✅ Success: {result.get('message')}")
            print(f"   Total: {result.get('pagination', {}).get('total')} permissions")
            print(f"   Page: {result.get('pagination', {}).get('page')}/{result.get('pagination', {}).get('totalPages')}")
            if result.get('data'):
                print("\n   Permissions found:")
                for perm in result['data']:
                    print(f"     - {perm['id']}: {perm['keyName']} ({perm['name']}) {perm.get('icon', '')}")
    else:
        print(f"❌ HTTP Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"❌ Request Error: {e}")

# Test 2: Get permissions by feature
print("\n\nTEST 2: Get permissions by feature")
print("-" * 70)

query_by_feature = """
query {
  permissionsByFeature(featureId: 1, page: 1, limit: 10) {
    success
    message
    data {
      id
      keyName
      name
      icon
      featureId
    }
    pagination {
      page
      limit
      total
      totalPages
    }
  }
}
"""

try:
    response = requests.post(
        GRAPHQL_URL,
        json={"query": query_by_feature},
        headers={"Content-Type": "application/json"},
        timeout=5
    )
    
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            print(f"❌ GraphQL Error: {data['errors']}")
        else:
            result = data.get('data', {}).get('permissionsByFeature', {})
            print(f"✅ Success: {result.get('message')}")
            print(f"   Total: {result.get('pagination', {}).get('total')} permissions")
    else:
        print(f"❌ HTTP Error {response.status_code}")
except Exception as e:
    print(f"❌ Request Error: {e}")

# Test 3: Get permission by key
print("\n\nTEST 3: Get permission by key name")
print("-" * 70)

query_by_key = """
query {
  permissionByKey(keyName: "permission.create") {
    success
    message
    data {
      id
      keyName
      name
      icon
      description
    }
  }
}
"""

try:
    response = requests.post(
        GRAPHQL_URL,
        json={"query": query_by_key},
        headers={"Content-Type": "application/json"},
        timeout=5
    )
    
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            print(f"❌ GraphQL Error: {data['errors']}")
        else:
            result = data.get('data', {}).get('permissionByKey', {})
            if result.get('success'):
                perm = result.get('data', {})
                print(f"✅ Found permission: {perm.get('name')} ({perm.get('icon')})")
            else:
                print(f"⚠️  {result.get('message')}")
    else:
        print(f"❌ HTTP Error {response.status_code}")
except Exception as e:
    print(f"❌ Request Error: {e}")

print("\n" + "=" * 70)
print("✅ GRAPHQL API TESTING COMPLETE")
print("=" * 70)

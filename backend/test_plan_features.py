"""Test Plan Feature CRUD operations via GraphQL."""
import asyncio
import httpx
from typing import Any

# GraphQL endpoint
GRAPHQL_URL = "http://localhost:8000/graphql"

# GraphQL Queries and Mutations
QUERY_ALL_PLAN_FEATURES = """
query {
    planFeatures {
        success
        message
        data {
            id
            keyName
            name
            description
            createdAt
            updatedAt
        }
    }
}
"""

QUERY_PLAN_FEATURE_BY_ID = """
query GetPlanFeature($id: Int!) {
    planFeature(id: $id) {
        id
        keyName
        name
        description
        createdAt
        updatedAt
    }
}
"""

QUERY_PLAN_FEATURE_BY_KEY = """
query GetPlanFeatureByKey($keyName: String!) {
    planFeatureByKey(keyName: $keyName) {
        id
        keyName
        name
        description
        createdAt
        updatedAt
    }
}
"""

MUTATION_CREATE_PLAN_FEATURE = """
mutation CreatePlanFeature($input: CreatePlanFeatureInput!) {
    createPlanFeature(input: $input) {
        success
        message
        data {
            id
            keyName
            name
            description
            createdAt
            updatedAt
        }
    }
}
"""

MUTATION_UPDATE_PLAN_FEATURE = """
mutation UpdatePlanFeature($id: Int!, $input: UpdatePlanFeatureInput!) {
    updatePlanFeature(id: $id, input: $input) {
        success
        message
        data {
            id
            keyName
            name
            description
            createdAt
            updatedAt
        }
    }
}
"""

MUTATION_DELETE_PLAN_FEATURE = """
mutation DeletePlanFeature($id: Int!) {
    deletePlanFeature(id: $id) {
        success
        message
        data {
            id
            keyName
            name
            description
        }
    }
}
"""


async def execute_graphql(query: str, variables: dict = None) -> dict[str, Any]:
    """Execute a GraphQL query."""
    payload = {
        "query": query,
        "variables": variables or {}
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(GRAPHQL_URL, json=payload)
        return response.json()


async def main():
    """Run all CRUD tests."""
    print("=" * 60)
    print("Testing Plan Feature CRUD Operations")
    print("=" * 60)
    
    # 1. CREATE
    print("\n1. CREATE Plan Feature")
    print("-" * 60)
    create_data = {
        "input": {
            "keyName": "trial_management",
            "name": "Trial Management",
            "description": "Ability to manage clinical trials"
        }
    }
    response = await execute_graphql(MUTATION_CREATE_PLAN_FEATURE, create_data)
    print(f"Response: {response}")
    created_id = None
    if response.get("data", {}).get("createPlanFeature", {}).get("data"):
        created_id = response["data"]["createPlanFeature"]["data"]["id"]
        print(f"✓ Created plan feature with ID: {created_id}")
    
    # 2. READ ALL
    print("\n2. READ All Plan Features")
    print("-" * 60)
    response = await execute_graphql(QUERY_ALL_PLAN_FEATURES)
    print(f"Response: {response}")
    if response.get("data", {}).get("planFeatures", {}).get("data"):
        print(f"✓ Found {len(response['data']['planFeatures']['data'])} plan features")
    
    # 3. READ BY ID
    if created_id:
        print(f"\n3. READ Plan Feature by ID ({created_id})")
        print("-" * 60)
        response = await execute_graphql(
            QUERY_PLAN_FEATURE_BY_ID,
            {"id": created_id}
        )
        print(f"Response: {response}")
        if response.get("data", {}).get("planFeature"):
            print(f"✓ Found plan feature: {response['data']['planFeature']['name']}")
    
    # 4. READ BY KEY
    print("\n4. READ Plan Feature by Key (trial_management)")
    print("-" * 60)
    response = await execute_graphql(
        QUERY_PLAN_FEATURE_BY_KEY,
        {"keyName": "trial_management"}
    )
    print(f"Response: {response}")
    if response.get("data", {}).get("planFeatureByKey"):
        print(f"✓ Found plan feature by key: {response['data']['planFeatureByKey']['name']}")
    
    # 5. UPDATE
    if created_id:
        print(f"\n5. UPDATE Plan Feature ({created_id})")
        print("-" * 60)
        update_data = {
            "id": created_id,
            "input": {
                "name": "Advanced Trial Management",
                "description": "Ability to manage complex clinical trials with advanced features"
            }
        }
        response = await execute_graphql(MUTATION_UPDATE_PLAN_FEATURE, update_data)
        print(f"Response: {response}")
        if response.get("data", {}).get("updatePlanFeature", {}).get("success"):
            print(f"✓ Updated plan feature successfully")
    
    # 6. DELETE
    if created_id:
        print(f"\n6. DELETE Plan Feature ({created_id})")
        print("-" * 60)
        response = await execute_graphql(
            MUTATION_DELETE_PLAN_FEATURE,
            {"id": created_id}
        )
        print(f"Response: {response}")
        if response.get("data", {}).get("deletePlanFeature", {}).get("success"):
            print(f"✓ Deleted plan feature successfully")
    
    print("\n" + "=" * 60)
    print("Test Completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

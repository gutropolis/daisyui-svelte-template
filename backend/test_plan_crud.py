"""
Plan CRUD Examples using Python and graphql-request

This script demonstrates how to interact with the Plan CRUD API
using Python's graphql-request library.

Run this file to see all CRUD operations in action:
    python test_plan_crud.py
"""

import json
import sys
sys.path.insert(0, '/E:/project/daisyui-svelte-template/backend')

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# ============================================================================
# SETUP
# ============================================================================

# GraphQL endpoint
GRAPHQL_URL = "http://localhost:8000/graphql"

# Create GraphQL client
transport = RequestsHTTPTransport(url=GRAPHQL_URL)
client = Client(transport=transport, fetch_schema_from_transport=True)


# ============================================================================
# QUERY EXAMPLES
# ============================================================================

def test_get_all_plans():
    """Example 1: Get all plans with pagination"""
    print("\n" + "="*80)
    print("TEST 1: GET ALL PLANS WITH PAGINATION")
    print("="*80)
    
    query = gql("""
        query {
            plans(page: 1, limit: 10) {
                success
                message
                data {
                    id
                    slug
                    name
                    price
                    durationDays
                    maxUsers
                    maxStudies
                    maxStorageGb
                    features
                }
                pagination {
                    page
                    total
                    totalPages
                    hasNext
                    hasPrev
                }
            }
        }
    """)
    
    try:
        result = client.execute(query)
        plans_data = result["plans"]
        
        print(f"\n✅ Success: {plans_data['message']}")
        print(f"📊 Total plans: {plans_data['pagination']['total']}")
        print(f"📄 Page: {plans_data['pagination']['page']}/{plans_data['pagination']['totalPages']}")
        
        print("\n📋 Plans:")
        for plan in plans_data["data"]:
            print(f"  - [{plan['id']}] {plan['name']} (${plan['price']}/{plan['durationDays']}d)")
            print(f"    Slug: {plan['slug']}")
            print(f"    Features: {plan['features']}")
            print()
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def test_get_plan_by_id():
    """Example 2: Get a specific plan by ID"""
    print("\n" + "="*80)
    print("TEST 2: GET PLAN BY ID")
    print("="*80)
    
    query = gql("""
        query {
            plan(id: 1) {
                success
                message
                data {
                    id
                    slug
                    name
                    price
                    durationDays
                    maxUsers
                    maxStudies
                    maxStorageGb
                    features
                    createdAt
                }
            }
        }
    """)
    
    try:
        result = client.execute(query)
        plan_data = result["plan"]
        
        if plan_data["success"]:
            plan = plan_data["data"]
            print(f"\n✅ {plan_data['message']}")
            print(f"\nPlan Details:")
            print(f"  ID: {plan['id']}")
            print(f"  Slug: {plan['slug']}")
            print(f"  Name: {plan['name']}")
            print(f"  Price: ${plan['price']}")
            print(f"  Duration: {plan['durationDays']} days")
            print(f"  Max Users: {plan['maxUsers']}")
            print(f"  Max Studies: {plan['maxStudies']}")
            print(f"  Max Storage: {plan['maxStorageGb']}GB")
            print(f"  Features: {plan['features']}")
            print(f"  Created: {plan['createdAt']}")
        else:
            print(f"❌ {plan_data['message']}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def test_get_plan_by_slug():
    """Example 3: Get plan by unique slug"""
    print("\n" + "="*80)
    print("TEST 3: GET PLAN BY SLUG")
    print("="*80)
    
    query = gql("""
        query {
            planBySlug(slug: "pro") {
                success
                message
                data {
                    id
                    slug
                    name
                    price
                }
            }
        }
    """)
    
    try:
        result = client.execute(query)
        plan_data = result["planBySlug"]
        
        if plan_data["success"]:
            plan = plan_data["data"]
            print(f"\n✅ {plan_data['message']}")
            print(f"  Slug: {plan['slug']}")
            print(f"  Name: {plan['name']}")
            print(f"  Price: ${plan['price']}")
        else:
            print(f"❌ {plan_data['message']}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def test_search_plans():
    """Example 4: Search plans by name/slug"""
    print("\n" + "="*80)
    print("TEST 4: SEARCH PLANS")
    print("="*80)
    
    query = gql("""
        query {
            plans(
                page: 1
                limit: 10
                filterInput: { search: "pro" }
            ) {
                success
                message
                data {
                    id
                    slug
                    name
                    price
                }
            }
        }
    """)
    
    try:
        result = client.execute(query)
        plans_data = result["plans"]
        
        print(f"\n✅ {plans_data['message']}")
        print("\n📋 Search results for 'pro':")
        for plan in plans_data["data"]:
            print(f"  - {plan['name']} (${plan['price']})")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


# ============================================================================
# MUTATION EXAMPLES
# ============================================================================

def test_create_plan():
    """Example 5: Create a new plan"""
    print("\n" + "="*80)
    print("TEST 5: CREATE NEW PLAN")
    print("="*80)
    
    mutation = gql("""
        mutation {
            createPlan(
                input: {
                    slug: "demo"
                    name: "Demo Plan"
                    price: "24.99"
                    durationDays: 30
                    maxUsers: 5
                    maxStudies: 25
                    maxStorageGb: 50
                    features: [1, 2, 3]
                }
            ) {
                success
                message
                data {
                    id
                    slug
                    name
                    price
                    maxUsers
                    features
                    createdAt
                }
            }
        }
    """)
    
    try:
        result = client.execute(mutation)
        plan_data = result["createPlan"]
        
        if plan_data["success"]:
            plan = plan_data["data"]
            print(f"\n✅ {plan_data['message']}")
            print(f"  ID: {plan['id']}")
            print(f"  Slug: {plan['slug']}")
            print(f"  Name: {plan['name']}")
            print(f"  Price: ${plan['price']}")
            print(f"  Features: {plan['features']}")
            return plan['id']
        else:
            print(f"❌ {plan_data['message']}")
            return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def test_update_plan(plan_id):
    """Example 6: Update an existing plan"""
    print("\n" + "="*80)
    print("TEST 6: UPDATE PLAN")
    print("="*80)
    
    if not plan_id:
        print("⚠️  Skipping: No plan ID to update")
        return
    
    mutation = gql("""
        mutation {
            updatePlan(
                id: """ + str(plan_id) + """
                input: {
                    name: "Updated Demo Plan"
                    price: "34.99"
                    maxUsers: 10
                    features: [1, 2, 3, 4, 5]
                }
            ) {
                success
                message
                data {
                    id
                    name
                    price
                    maxUsers
                    features
                    updatedAt
                }
            }
        }
    """)
    
    try:
        result = client.execute(mutation)
        plan_data = result["updatePlan"]
        
        if plan_data["success"]:
            plan = plan_data["data"]
            print(f"\n✅ {plan_data['message']}")
            print(f"  Name: {plan['name']}")
            print(f"  Price: ${plan['price']}")
            print(f"  Max Users: {plan['maxUsers']}")
            print(f"  Features: {plan['features']}")
            print(f"  Updated: {plan['updatedAt']}")
        else:
            print(f"❌ {plan_data['message']}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def test_delete_plan(plan_id):
    """Example 7: Delete a plan"""
    print("\n" + "="*80)
    print("TEST 7: DELETE PLAN")
    print("="*80)
    
    if not plan_id:
        print("⚠️  Skipping: No plan ID to delete")
        return
    
    mutation = gql("""
        mutation {
            deletePlan(id: """ + str(plan_id) + """) {
                success
                message
            }
        }
    """)
    
    try:
        result = client.execute(mutation)
        plan_data = result["deletePlan"]
        
        if plan_data["success"]:
            print(f"\n✅ {plan_data['message']}")
        else:
            print(f"❌ {plan_data['message']}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def test_error_handling():
    """Example 8: Error handling examples"""
    print("\n" + "="*80)
    print("TEST 8: ERROR HANDLING")
    print("="*80)
    
    # Test 8a: Create plan with duplicate slug
    print("\n8a. Create plan with duplicate slug:")
    mutation = gql("""
        mutation {
            createPlan(
                input: {
                    slug: "free"
                    name: "Duplicate"
                    price: "0"
                    durationDays: 30
                }
            ) {
                success
                message
            }
        }
    """)
    
    try:
        result = client.execute(mutation)
        plan_data = result["createPlan"]
        print(f"  Result: {plan_data['message']}")
    except Exception as e:
        print(f"  Error: {str(e)}")
    
    # Test 8b: Update non-existent plan
    print("\n8b. Update non-existent plan:")
    mutation = gql("""
        mutation {
            updatePlan(
                id: 9999
                input: { name: "Ghost Plan" }
            ) {
                success
                message
            }
        }
    """)
    
    try:
        result = client.execute(mutation)
        plan_data = result["updatePlan"]
        print(f"  Result: {plan_data['message']}")
    except Exception as e:
        print(f"  Error: {str(e)}")
    
    # Test 8c: Delete non-existent plan
    print("\n8c. Delete non-existent plan:")
    mutation = gql("""
        mutation {
            deletePlan(id: 9999) {
                success
                message
            }
        }
    """)
    
    try:
        result = client.execute(mutation)
        plan_data = result["deletePlan"]
        print(f"  Result: {plan_data['message']}")
    except Exception as e:
        print(f"  Error: {str(e)}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Run all tests"""
    print("\n" + "🎯 "*40)
    print("PLAN CRUD GRAPHQL EXAMPLES")
    print("🎯 "*40)
    print(f"\nGraphQL Endpoint: {GRAPHQL_URL}")
    print(f"Time: {__import__('datetime').datetime.now()}")
    
    # Run tests
    test_get_all_plans()
    test_get_plan_by_id()
    test_get_plan_by_slug()
    test_search_plans()
    
    # CRUD operations
    new_plan_id = test_create_plan()
    test_update_plan(new_plan_id)
    test_delete_plan(new_plan_id)
    
    # Error handling
    test_error_handling()
    
    print("\n" + "="*80)
    print("✅ ALL TESTS COMPLETED")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()

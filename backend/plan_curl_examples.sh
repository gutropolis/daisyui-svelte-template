#!/bin/bash

# PLAN CRUD - CURL EXAMPLES
# Test GraphQL Plan operations using curl
# Usage: bash plan_crud_examples.sh

GRAPHQL_URL="http://localhost:8000/graphql"

echo "🎯 PLAN CRUD CURL EXAMPLES"
echo "=========================="
echo ""

# ============================================================================
# QUERY 1: Get All Plans
# ============================================================================
echo "1️⃣  GET ALL PLANS"
echo "---"
curl -s -X POST "$GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { plans(page: 1, limit: 10) { success message data { id slug name price durationDays } pagination { page total totalPages } } }"
  }' | jq '.'
echo ""

# ============================================================================
# QUERY 2: Get Plan by ID
# ============================================================================
echo ""
echo "2️⃣  GET PLAN BY ID (ID: 1)"
echo "---"
curl -s -X POST "$GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { plan(id: 1) { success message data { id slug name price durationDays maxUsers } } }"
  }' | jq '.'
echo ""

# ============================================================================
# QUERY 3: Get Plan by Slug
# ============================================================================
echo ""
echo "3️⃣  GET PLAN BY SLUG (pro)"
echo "---"
curl -s -X POST "$GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { planBySlug(slug: \"pro\") { success message data { id slug name price } } }"
  }' | jq '.'
echo ""

# ============================================================================
# QUERY 4: Search Plans
# ============================================================================
echo ""
echo "4️⃣  SEARCH PLANS (search: \"pro\")"
echo "---"
curl -s -X POST "$GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { plans(page: 1, limit: 10, filterInput: {search: \"pro\"}) { success data { id slug name } } }"
  }' | jq '.'
echo ""

# ============================================================================
# MUTATION 1: Create Plan
# ============================================================================
echo ""
echo "5️⃣  CREATE NEW PLAN"
echo "---"
curl -s -X POST "$GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { createPlan(input: {slug: \"test-plan\", name: \"Test Plan\", price: \"15.99\", durationDays: 30, maxUsers: 3, features: [1, 2]}) { success message data { id slug name price } } }"
  }' | jq '.'
echo ""

# ============================================================================
# MUTATION 2: Update Plan
# ============================================================================
echo ""
echo "6️⃣  UPDATE PLAN (ID: 2)"
echo "---"
curl -s -X POST "$GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { updatePlan(id: 2, input: {name: \"Updated Pro\", price: \"49.99\", maxUsers: 20}) { success message data { id name price maxUsers } } }"
  }' | jq '.'
echo ""

# ============================================================================
# MUTATION 3: Delete Plan
# ============================================================================
echo ""
echo "7️⃣  DELETE PLAN (ID: 4 - if exists)"
echo "---"
curl -s -X POST "$GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { deletePlan(id: 4) { success message } }"
  }' | jq '.'
echo ""

echo "✅ All examples completed!"

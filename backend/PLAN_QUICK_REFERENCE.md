# Plan CRUD - Quick Reference

## Endpoint

`http://localhost:8000/graphql`

## Queries

### Get All Plans

```graphql
query {
  plans(page: 1, limit: 10, filterInput: { search: "pro" }) {
    success
    message
    data {
      id
      slug
      name
      price
      durationDays
      maxUsers
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
```

### Get By ID

```graphql
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
    }
  }
}
```

### Get By Slug

```graphql
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
```

---

## Mutations

### Create

```graphql
mutation {
  createPlan(
    input: {
      slug: "starter"
      name: "Starter"
      price: "9.99"
      durationDays: 30
      maxUsers: 2
      maxStudies: 10
      maxStorageGb: 5
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
      createdAt
    }
  }
}
```

### Update

```graphql
mutation {
  updatePlan(
    id: 2
    input: {
      name: "Updated Name"
      price: "39.99"
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
      updatedAt
    }
  }
}
```

### Delete

```graphql
mutation {
  deletePlan(id: 4) {
    success
    message
  }
}
```

---

## Sample Plans

| ID  | Slug       | Name       | Price  | Users | Storage |
| --- | ---------- | ---------- | ------ | ----- | ------- |
| 1   | free       | Free Plan  | $0     | 1     | 1GB     |
| 2   | pro        | Pro Plan   | $29.99 | 5     | 100GB   |
| 3   | enterprise | Enterprise | $99.99 | ∞     | ∞       |

---

## Pagination

```graphql
pagination {
  page          # Current page (1-based)
  limit         # Items per page
  total         # Total items
  totalPages    # Total pages
  hasNext       # Has next page?
  hasPrev       # Has previous page?
}
```

---

## Filtering

```graphql
filterInput: {
  search: "pro"  # Searches name and slug (case-insensitive)
}
```

---

## Error Examples

**Duplicate Slug:**

```json
{ "success": false, "message": "Plan with slug 'pro' already exists" }
```

**Empty Name:**

```json
{ "success": false, "message": "Name cannot be empty" }
```

**Invalid Duration:**

```json
{ "success": false, "message": "Duration days must be at least 1" }
```

**Not Found:**

```json
{ "success": false, "message": "Plan with ID 999 not found" }
```

---

## Curl Examples

**List Plans:**

```bash
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ plans(page: 1) { success data { id name price } } }"}'
```

**Create Plan:**

```bash
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { createPlan(input: {slug: \"test\", name: \"Test\", price: \"10\", durationDays: 30}) { success data { id } } }"}'
```

---

## Key Points

✓ Slug must be **unique**
✓ Name cannot be **empty**
✓ Duration must be **≥ 1** day
✓ Price can be any decimal
✓ Features is an array of feature IDs
✓ max\_\* fields: NULL = unlimited
✓ Search is **case-insensitive**
✓ Pagination: default limit = 10, max = 100
✓ Cannot update slug after creation

---

## Files

- `PLAN_GRAPHQL_EXAMPLES.md` - Full examples
- `PLAN_CRUD_DOCUMENTATION.md` - Complete guide
- `test_plan_crud.py` - Python tests
- `plan_curl_examples.sh` - Bash examples

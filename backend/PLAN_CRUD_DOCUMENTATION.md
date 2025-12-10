# Plan CRUD - Complete Documentation

## Overview

The Plan CRUD system provides full Create, Read, Update, Delete operations for managing subscription plans in the DaisyUI Healthcare system.

**GraphQL Endpoint:** `http://localhost:8000/graphql`

---

## Database Schema

```sql
CREATE TABLE plans (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    slug VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    duration_days INT NOT NULL,
    max_users INT DEFAULT NULL,
    max_studies INT DEFAULT NULL,
    max_storage_gb INT DEFAULT NULL,
    features VARCHAR(500),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Fields

| Field          | Type          | Required | Notes                                   |
| -------------- | ------------- | -------- | --------------------------------------- |
| id             | BIGINT        | Yes      | Primary key, auto-increment             |
| slug           | VARCHAR(100)  | Yes      | Unique identifier for plan              |
| name           | VARCHAR(255)  | Yes      | Display name                            |
| price          | DECIMAL(10,2) | Yes      | Price per billing period                |
| duration_days  | INT           | Yes      | Billing period in days (30, 365, etc.)  |
| max_users      | INT           | No       | Maximum users, NULL = unlimited         |
| max_studies    | INT           | No       | Maximum studies, NULL = unlimited       |
| max_storage_gb | INT           | No       | Maximum storage in GB, NULL = unlimited |
| features       | VARCHAR(500)  | No       | JSON array of feature IDs               |
| created_at     | DATETIME      | Yes      | Creation timestamp                      |
| updated_at     | DATETIME      | Yes      | Last update timestamp                   |

---

## Sample Data

Three sample plans are pre-loaded:

### Free Plan

```json
{
  "id": 1,
  "slug": "free",
  "name": "Free Plan",
  "price": "0.00",
  "duration_days": 30,
  "max_users": 1,
  "max_studies": 5,
  "max_storage_gb": 1,
  "features": [1, 2]
}
```

### Pro Plan

```json
{
  "id": 2,
  "slug": "pro",
  "name": "Pro Plan",
  "price": "29.99",
  "duration_days": 30,
  "max_users": 5,
  "max_studies": 50,
  "max_storage_gb": 100,
  "features": [1, 2, 3, 4]
}
```

### Enterprise Plan

```json
{
  "id": 3,
  "slug": "enterprise",
  "name": "Enterprise Plan",
  "price": "99.99",
  "duration_days": 365,
  "max_users": null,
  "max_studies": null,
  "max_storage_gb": null,
  "features": [1, 2, 3, 4, 5]
}
```

---

## GraphQL Operations

### Queries

#### 1. Get All Plans

**Get paginated list of all plans with optional filtering**

```graphql
query GetPlans {
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
      maxStudies
      maxStorageGb
      features
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
```

**Parameters:**

- `page` (Int, optional): Page number (default: 1)
- `limit` (Int, optional): Items per page (default: 10, max: 100)
- `filterInput` (FilterPlansInput, optional): Filter options
  - `search` (String, optional): Search term (searches name and slug)

**Response:**

- `success` (Boolean): Operation success status
- `message` (String): Status message
- `data` (List[PlanType]): List of plans
- `pagination` (PaginationInfo): Pagination details

---

#### 2. Get Plan by ID

**Retrieve a specific plan by its ID**

```graphql
query GetPlanById {
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
      updatedAt
    }
  }
}
```

**Parameters:**

- `id` (Int!): Plan ID (required)

**Response:**

- `success` (Boolean): Operation success status
- `message` (String): Status message
- `data` (PlanType): Plan details

---

#### 3. Get Plan by Slug

**Retrieve a specific plan by its unique slug**

```graphql
query GetPlanBySlug {
  planBySlug(slug: "pro") {
    success
    message
    data {
      id
      slug
      name
      price
      durationDays
    }
  }
}
```

**Parameters:**

- `slug` (String!): Plan slug (required)

**Response:**

- Same as "Get Plan by ID"

---

### Mutations

#### 1. Create Plan

**Create a new subscription plan**

```graphql
mutation CreatePlan {
  createPlan(
    input: {
      slug: "starter"
      name: "Starter Plan"
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
      durationDays
      maxUsers
      maxStudies
      maxStorageGb
      features
      createdAt
      updatedAt
    }
  }
}
```

**Input Parameters:**

- `slug` (String!): Unique identifier (required, must be unique)
- `name` (String!): Display name (required)
- `price` (String!): Price (required)
- `durationDays` (Int!): Billing period in days (required)
- `maxUsers` (Int, optional): Maximum users
- `maxStudies` (Int, optional): Maximum studies
- `maxStorageGb` (Int, optional): Maximum storage in GB
- `features` (List[Int], optional): Feature IDs

**Validation:**

- Slug must be unique
- Name cannot be empty
- Duration must be at least 1 day
- Price can be any decimal value

**Response:**

- Returns created plan with generated ID and timestamps

---

#### 2. Update Plan

**Update an existing plan (all fields are optional)**

```graphql
mutation UpdatePlan {
  updatePlan(
    id: 2
    input: {
      name: "Professional Plan"
      price: "39.99"
      maxUsers: 10
      features: [1, 2, 3, 4, 5]
    }
  ) {
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
      updatedAt
    }
  }
}
```

**Parameters:**

- `id` (Int!): Plan ID (required)
- `input` (UpdatePlanInput!): Fields to update
  - All fields are optional
  - Slug cannot be updated
  - Only provided fields will be updated

**Response:**

- Returns updated plan with new `updatedAt` timestamp

---

#### 3. Delete Plan

**Delete a plan from the system**

```graphql
mutation DeletePlan {
  deletePlan(id: 4) {
    success
    message
  }
}
```

**Parameters:**

- `id` (Int!): Plan ID (required)

**Response:**

- `success` (Boolean): Operation success status
- `message` (String): Status message

---

## Error Handling

### Common Errors

#### Error 1: Duplicate Slug

```json
{
  "success": false,
  "message": "Plan with slug 'pro' already exists"
}
```

**Solution:** Use a unique slug

#### Error 2: Empty Name

```json
{
  "success": false,
  "message": "Name cannot be empty"
}
```

**Solution:** Provide a non-empty name

#### Error 3: Invalid Duration

```json
{
  "success": false,
  "message": "Duration days must be at least 1"
}
```

**Solution:** Use duration ≥ 1

#### Error 4: Plan Not Found

```json
{
  "success": false,
  "message": "Plan with ID 999 not found"
}
```

**Solution:** Verify the plan ID exists

---

## API Examples

### Example 1: List All Plans

```bash
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{
    "query": "{ plans(page: 1, limit: 10) { success data { id slug name price } pagination { total } } }"
  }'
```

### Example 2: Create a New Plan

```bash
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { createPlan(input: {slug: \"team\", name: \"Team Plan\", price: \"49.99\", durationDays: 30, maxUsers: 10}) { success data { id slug name } } }"
  }'
```

### Example 3: Update a Plan

```bash
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { updatePlan(id: 2, input: {price: \"39.99\", maxUsers: 20}) { success data { id price maxUsers } } }"
  }'
```

### Example 4: Delete a Plan

```bash
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { deletePlan(id: 4) { success message } }"
  }'
```

---

## Testing

### Manual Testing via GraphQL Playground

1. Open `http://localhost:8000/graphql`
2. Paste queries/mutations from examples
3. Execute and view results

### Automated Testing

Run the Python test script:

```bash
cd backend
python test_plan_crud.py
```

### Curl Testing

Run the bash script:

```bash
bash plan_curl_examples.sh
```

---

## Pagination Guidelines

### Parameters

- `page` (Int): 1-based page number
- `limit` (Int): Items per page (1-100)

### Example: Get Page 2

```graphql
query {
  plans(page: 2, limit: 10) {
    data {
      id
      name
    }
    pagination {
      page
      hasNext
      hasPrev
    }
  }
}
```

### Pagination Info

- `page`: Current page number
- `limit`: Items per page
- `total`: Total number of items
- `totalPages`: Total number of pages
- `hasNext`: Whether next page exists
- `hasPrev`: Whether previous page exists

---

## Filtering Guidelines

### Search by Name/Slug

```graphql
query {
  plans(page: 1, filterInput: { search: "pro" }) {
    data {
      id
      name
      slug
    }
  }
}
```

### Case-Insensitive Search

The search is case-insensitive and matches:

- Full name: "Pro Plan" matches "pro"
- Partial name: "Professional" matches "pro"
- Slug: "pro" matches "pro"

---

## Response Format

### Success Response

```json
{
  "success": true,
  "message": "Found 3 plans",
  "data": [
    {
      "id": "1",
      "slug": "free",
      "name": "Free Plan",
      "price": "0.00"
    }
  ]
}
```

### Error Response

```json
{
  "success": false,
  "message": "Plan with slug 'pro' already exists",
  "data": null
}
```

---

## Files

- `app/models/plan.py` - SQLAlchemy model
- `app/graphql/plan/types.py` - GraphQL type definitions
- `app/graphql/plan/queries.py` - GraphQL queries
- `app/graphql/plan/mutations.py` - GraphQL mutations
- `PLAN_GRAPHQL_EXAMPLES.md` - Detailed GraphQL examples
- `test_plan_crud.py` - Python test script
- `plan_curl_examples.sh` - Curl command examples

---

## Integration Checklist

- [x] Database model created
- [x] GraphQL types defined
- [x] Queries implemented (3)
- [x] Mutations implemented (3)
- [x] Pagination support added
- [x] Filtering/search support added
- [x] Error handling implemented
- [x] Sample data loaded
- [x] Schema integrated
- [x] Examples documented
- [ ] Frontend integration

---

## Next Steps

1. **Frontend Integration**: Create Plan CRUD UI components in Svelte
2. **Additional Features**: Add plan-user relationships
3. **Analytics**: Track plan usage and conversions
4. **Billing Integration**: Connect to payment providers

---

## Support

For issues or questions, refer to:

- GraphQL Playground: http://localhost:8000/graphql
- Documentation: `PLAN_GRAPHQL_EXAMPLES.md`
- Test Script: `test_plan_crud.py`

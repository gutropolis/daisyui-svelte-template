"""
GraphQL Examples for Plan CRUD Operations

This file contains example queries and mutations for working with Plans
in the DaisyUI Healthcare GraphQL API.

Access the GraphQL playground at: http://localhost:8000/graphql
"""

# ============================================================================

# QUERIES - READ OPERATIONS

# ============================================================================

"""

1. GET ALL PLANS WITH PAGINATION
   - Retrieve all plans with pagination (10 per page by default)
   - Max limit: 100 items per page
     """
     query GetAllPlans {
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

# Expected Response:

# {

# "data": {

# "plans": {

# "success": true,

# "message": "Found 3 plans",

# "data": [

# {

# "id": "1",

# "slug": "free",

# "name": "Free Plan",

# "price": "0.00",

# "durationDays": 30,

# "maxUsers": 1,

# "maxStudies": 5,

# "maxStorageGb": 1,

# "features": [1, 2],

# "createdAt": "2025-12-10T21:47:40.334785",

# "updatedAt": "2025-12-10T21:47:40.334785"

# },

# ...

# ],

# "pagination": {

# "page": 1,

# "limit": 10,

# "total": 3,

# "totalPages": 1,

# "hasNext": false,

# "hasPrev": false

# }

# }

# }

# }

""" 2. GET PLANS WITH PAGINATION (PAGE 2)

- Navigate through pages
  """
  query GetPlansPage2 {
  plans(page: 2, limit: 10) {
  success
  message
  data {
  id
  slug
  name
  price
  }
  pagination {
  page
  hasNext
  hasPrev
  }
  }
  }

""" 3. SEARCH PLANS BY NAME OR SLUG

- Filter plans using search term (searches in name and slug)
  """
  query SearchPlans {
  plans(
  page: 1
  limit: 10
  filterInput: {
  search: "pro"
  }
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

# Expected Response: Returns only "Pro Plan"

""" 4. GET SINGLE PLAN BY ID

- Retrieve a specific plan by its ID
  """
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

# Expected Response:

# {

# "data": {

# "plan": {

# "success": true,

# "message": "Plan found",

# "data": {

# "id": "1",

# "slug": "free",

# "name": "Free Plan",

# "price": "0.00",

# "durationDays": 30,

# "maxUsers": 1,

# "maxStudies": 5,

# "maxStorageGb": 1,

# "features": [1, 2],

# "createdAt": "2025-12-10T21:47:40.334785",

# "updatedAt": "2025-12-10T21:47:40.334785"

# }

# }

# }

# }

""" 5. GET PLAN BY SLUG (Unique Identifier)

- Retrieve a plan using its unique slug
- Slugs: "free", "pro", "enterprise"
  """
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
  maxUsers
  maxStudies
  maxStorageGb
  features
  }
  }
  }

# Expected Response:

# {

# "data": {

# "planBySlug": {

# "success": true,

# "message": "Plan found",

# "data": {

# "id": "2",

# "slug": "pro",

# "name": "Pro Plan",

# "price": "29.99",

# ...

# }

# }

# }

# }

# ============================================================================

# MUTATIONS - WRITE OPERATIONS

# ============================================================================

""" 6. CREATE A NEW PLAN

- Create a new subscription plan
- Slug must be unique
- Features is a list of feature IDs
  """
  mutation CreateNewPlan {
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

# Expected Response:

# {

# "data": {

# "createPlan": {

# "success": true,

# "message": "Plan created successfully",

# "data": {

# "id": "4",

# "slug": "starter",

# "name": "Starter Plan",

# "price": "9.99",

# "durationDays": 30,

# "maxUsers": 2,

# "maxStudies": 10,

# "maxStorageGb": 5,

# "features": [1, 2, 3],

# "createdAt": "2025-12-10T21:55:00.000000",

# "updatedAt": "2025-12-10T21:55:00.000000"

# }

# }

# }

# }

""" 7. CREATE PLAN WITHOUT OPTIONAL FIELDS

- Create a plan with only required fields
- Optional fields: maxUsers, maxStudies, maxStorageGb, features
  """
  mutation CreateMinimalPlan {
  createPlan(
  input: {
  slug: "basic"
  name: "Basic Plan"
  price: "19.99"
  durationDays: 30
  }
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

""" 8. UPDATE AN EXISTING PLAN

- Update only the fields you want to change
- Cannot update slug (immutable after creation)
- All fields in UpdatePlanInput are optional
  """
  mutation UpdatePlan {
  updatePlan(
  id: 2
  input: {
  name: "Professional Plan"
  price: "39.99"
  maxUsers: 10
  maxStudies: 100
  maxStorageGb: 500
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

# Expected Response:

# {

# "data": {

# "updatePlan": {

# "success": true,

# "message": "Plan updated successfully",

# "data": {

# "id": "2",

# "slug": "pro",

# "name": "Professional Plan",

# "price": "39.99",

# ...

# "updatedAt": "2025-12-10T21:56:00.000000"

# }

# }

# }

# }

""" 9. UPDATE PLAN - PARTIAL UPDATE

- Update only specific fields
- Other fields remain unchanged
  """
  mutation PartialUpdatePlan {
  updatePlan(
  id: 1
  input: {
  name: "Free Tier Plan"
  maxUsers: 2
  }
  ) {
  success
  message
  data {
  id
  name
  maxUsers
  updatedAt
  }
  }
  }

""" 10. UPDATE PLAN FEATURES - Modify the features associated with a plan
"""
mutation UpdatePlanFeatures {
updatePlan(
id: 2
input: {
features: [1, 2, 3, 4]
}
) {
success
message
data {
id
slug
features
}
}
}

""" 11. DELETE A PLAN - Remove a plan from the system - Warning: This is permanent!
"""
mutation DeletePlan {
deletePlan(id: 4) {
success
message
data {
id
}
}
}

# Expected Response:

# {

# "data": {

# "deletePlan": {

# "success": true,

# "message": "Plan deleted successfully",

# "data": null

# }

# }

# }

""" 12. DELETE PLAN - FAILURE CASE - Attempting to delete non-existent plan
"""
mutation DeleteNonExistentPlan {
deletePlan(id: 999) {
success
message
}
}

# Expected Response:

# {

# "data": {

# "deletePlan": {

# "success": false,

# "message": "Plan with ID 999 not found"

# }

# }

# }

# ============================================================================

# ERROR HANDLING EXAMPLES

# ============================================================================

"""
ERROR 1: CREATE PLAN WITH DUPLICATE SLUG
"""
mutation CreateDuplicateSlugPlan {
createPlan(
input: {
slug: "free" # This already exists!
name: "Another Free Plan"
price: "0"
durationDays: 30
}
) {
success
message
}
}

# Response:

# {

# "data": {

# "createPlan": {

# "success": false,

# "message": "Plan with slug 'free' already exists"

# }

# }

# }

"""
ERROR 2: CREATE PLAN WITH EMPTY NAME
"""
mutation CreateInvalidPlan {
createPlan(
input: {
slug: "invalid"
name: "" # Empty name!
price: "0"
durationDays: 30
}
) {
success
message
}
}

# Response:

# {

# "data": {

# "createPlan": {

# "success": false,

# "message": "Name cannot be empty"

# }

# }

# }

"""
ERROR 3: CREATE PLAN WITH INVALID DURATION
"""
mutation CreateInvalidDurationPlan {
createPlan(
input: {
slug: "invalid"
name: "Invalid Plan"
price: "0"
durationDays: 0 # Must be at least 1!
}
) {
success
message
}
}

# Response:

# {

# "data": {

# "createPlan": {

# "success": false,

# "message": "Duration days must be at least 1"

# }

# }

# }

"""
ERROR 4: UPDATE NON-EXISTENT PLAN
"""
mutation UpdateNonExistentPlan {
updatePlan(
id: 999
input: {
name: "Updated Name"
}
) {
success
message
}
}

# Response:

# {

# "data": {

# "updatePlan": {

# "success": false,

# "message": "Plan with ID 999 not found"

# }

# }

# }

# ============================================================================

# COMBINED WORKFLOWS

# ============================================================================

"""
WORKFLOW 1: CREATE AND RETRIEVE NEW PLAN
Step 1: Create a new plan
Step 2: Retrieve it by ID
Step 3: Search for it by name
"""

# Step 1: Create

mutation CreateWorkflowPlan {
createPlan(
input: {
slug: "workflow-test"
name: "Workflow Test Plan"
price: "14.99"
durationDays: 30
maxUsers: 3
maxStudies: 20
maxStorageGb: 10
features: [1, 2]
}
) {
success
message
data {
id
slug
name
}
}
}

# Step 2: Get by ID (use ID from Step 1)

query RetrieveWorkflowPlan {
plan(id: 5) {
success
data {
id
slug
name
price
}
}
}

# Step 3: Search by name

query SearchWorkflowPlan {
plans(
page: 1
filterInput: { search: "workflow" }
) {
success
data {
id
slug
name
}
}
}

"""
WORKFLOW 2: UPDATE AND VERIFY CHANGES
Step 1: Update plan details
Step 2: Retrieve to verify changes
"""

# Step 1: Update

mutation UpdateWorkflowPlan {
updatePlan(
id: 2
input: {
name: "Updated Pro Plan"
price: "49.99"
maxUsers: 20
}
) {
success
data {
id
name
price
maxUsers
updatedAt
}
}
}

# Step 2: Verify

query VerifyUpdate {
plan(id: 2) {
success
data {
id
name
price
maxUsers
updatedAt
}
}
}

# ============================================================================

# TESTING CHECKLIST

# ============================================================================

"""
Test Cases for Plan CRUD:

✓ CREATE

- Create plan with all fields
- Create plan with only required fields
- Create with duplicate slug (should fail)
- Create with empty name (should fail)
- Create with invalid duration (should fail)

✓ READ

- Get all plans with pagination
- Get all plans on different pages
- Search plans by name
- Search plans by slug
- Get plan by ID
- Get plan by unique slug
- Get non-existent plan (should fail)

✓ UPDATE

- Update all fields
- Update partial fields
- Update non-existent plan (should fail)
- Update with invalid data (should fail)

✓ DELETE

- Delete existing plan
- Delete non-existent plan (should fail)

✓ PAGINATION

- Test different page numbers
- Test different limits (1, 10, 50, 100)
- Verify has_next and has_prev flags

✓ FILTERING

- Search by exact match
- Search by partial match
- Case-insensitive search
- Empty search results
  """

# 🔐 Permissions API - Quick Reference

## 📍 GraphQL Endpoint

`http://localhost:8000/graphql`

---

## 📊 Database Schema

```
permissions table
├── id: BIGINT (PK, AUTO_INCREMENT)
├── key_name: VARCHAR(150) UNIQUE
├── name: VARCHAR(255)
├── description: TEXT (nullable)
├── icon: VARCHAR(255) (nullable)
├── feature_id: BIGINT (FK → plan_features.id)
├── created_at: DATETIME (auto)
└── updated_at: DATETIME (auto)
```

---

## 🔍 Query: Get All Permissions

```graphql
query GetPermissions {
  permissions(
    page: 1 # Page number (required)
    limit: 10 # Items per page (default: 10, max: 100)
    filterInput: {
      # Optional filter
      featureId: 1 # Filter by feature
      search: "create" # Search in name/key_name
    }
  ) {
    success # Boolean
    message # String
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
```

---

## 🔍 Query: Get Single Permission by ID

```graphql
query GetPermission {
  permission(id: 1) {
    success
    message
    data {
      id
      keyName
      name
      icon
      description
      featureId
    }
  }
}
```

---

## 🔍 Query: Get Permission by Key

```graphql
query GetByKey {
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
```

---

## 🔍 Query: Get by Feature

```graphql
query GetByFeature {
  permissionsByFeature(
    featureId: 1 # Required
    page: 1 # Optional (default: 1)
    limit: 10 # Optional (default: 10)
  ) {
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
      hasNext
      hasPrev
    }
  }
}
```

---

## ➕ Mutation: Create Permission

```graphql
mutation CreatePermission {
  createPermission(
    input: {
      keyName: "permission.export" # Required, unique
      name: "Export Data" # Required
      featureId: 1 # Required
      description: "Can export..." # Optional
      icon: "📤" # Optional
    }
  ) {
    success
    message
    data {
      id
      keyName
      name
      icon
      createdAt
    }
  }
}
```

---

## ✏️ Mutation: Update Permission

```graphql
mutation UpdatePermission {
  updatePermission(
    id: 1 # Required
    input: {
      name: "Export Data" # Optional
      description: "Can export..." # Optional
      icon: "📥" # Optional
      # Note: key_name is NOT editable
    }
  ) {
    success
    message
    data {
      id
      keyName
      name
      icon
      updatedAt
    }
  }
}
```

---

## 🗑️ Mutation: Delete Permission

```graphql
mutation DeletePermission {
  deletePermission(id: 1) {
    success
    message
  }
}
```

---

## 📋 Sample Requests

### Get First Page of Permissions

```graphql
{
  permissions(page: 1, limit: 10) {
    success
    message
    data {
      id
      keyName
      name
      icon
    }
    pagination {
      page
      limit
      total
      totalPages
      hasNext
    }
  }
}
```

### Get Next Page

```graphql
{
  permissions(page: 2, limit: 10) {
    success
    data {
      id
      keyName
      name
    }
    pagination {
      page
      total
    }
  }
}
```

### Search by Name

```graphql
{
  permissions(page: 1, limit: 10, filterInput: { search: "create" }) {
    success
    data {
      id
      keyName
      name
    }
    pagination {
      total
    }
  }
}
```

### Filter by Feature

```graphql
{
  permissions(page: 1, limit: 10, filterInput: { featureId: 1 }) {
    success
    data {
      id
      name
      featureId
    }
  }
}
```

### Combined Filter

```graphql
{
  permissions(
    page: 1
    limit: 10
    filterInput: { featureId: 1, search: "read" }
  ) {
    success
    data {
      id
      name
    }
    pagination {
      total
    }
  }
}
```

---

## 📊 Response Examples

### Success Response (List)

```json
{
  "data": {
    "permissions": {
      "success": true,
      "message": "Found 4 permissions",
      "data": [
        {
          "id": "1",
          "keyName": "permission.create",
          "name": "Create Permission",
          "icon": "➕",
          "featureId": "1",
          "description": "Permission to create permission",
          "createdAt": "2024-01-15T10:30:45",
          "updatedAt": "2024-01-15T10:30:45"
        }
      ],
      "pagination": {
        "page": 1,
        "limit": 10,
        "total": 4,
        "totalPages": 1,
        "hasNext": false,
        "hasPrev": false
      }
    }
  }
}
```

### Success Response (Single)

```json
{
  "data": {
    "permission": {
      "success": true,
      "message": "Permission found",
      "data": {
        "id": "1",
        "keyName": "permission.create",
        "name": "Create Permission",
        "icon": "➕"
      }
    }
  }
}
```

### Error Response

```json
{
  "data": {
    "permission": {
      "success": false,
      "message": "Permission with ID 999 not found",
      "data": null
    }
  }
}
```

### Create Success

```json
{
  "data": {
    "createPermission": {
      "success": true,
      "message": "Permission created successfully",
      "data": {
        "id": "5",
        "keyName": "permission.export",
        "name": "Export Data",
        "icon": "📤",
        "createdAt": "2024-01-15T14:20:30"
      }
    }
  }
}
```

---

## ⚠️ Validation Rules

| Field       | Rule                                  |
| ----------- | ------------------------------------- |
| keyName     | Required, unique, max 150 chars       |
| name        | Required, max 255 chars               |
| featureId   | Required, must exist in plan_features |
| description | Optional, no length limit             |
| icon        | Optional, max 255 chars               |
| page        | Optional (default: 1), must be > 0    |
| limit       | Optional (default: 10), 1-100         |

---

## 🔄 Pagination Logic

```
Total: 47 items, Limit: 10 items per page

Page 1 → Items 1-10   (hasNext: true, hasPrev: false)
Page 2 → Items 11-20  (hasNext: true, hasPrev: true)
Page 3 → Items 21-30  (hasNext: true, hasPrev: true)
Page 4 → Items 31-40  (hasNext: true, hasPrev: true)
Page 5 → Items 41-47  (hasNext: false, hasPrev: true)

totalPages = Math.ceil(47 / 10) = 5
```

---

## 🎨 Icon Examples

| Icon | Use Case      |
| ---- | ------------- |
| ➕   | Create/Add    |
| 👁️   | Read/View     |
| ✏️   | Edit/Update   |
| 🗑️   | Delete        |
| 📤   | Export        |
| 📥   | Import        |
| 🔒   | Restrict/Lock |
| 📊   | Analytics     |
| ⚙️   | Settings      |
| 🔑   | Access        |

---

## 💾 Data Types

```graphql
# Scalar Types
String     # Text (max 255 chars for names)
Int        # Whole numbers (for IDs, pagination)
Boolean    # true/false

# Object Types
PermissionType
├── id: Int
├── keyName: String
├── name: String
├── icon: String
├── featureId: Int
├── description: String
├── createdAt: String (ISO format)
└── updatedAt: String (ISO format)

PaginationInfo
├── page: Int
├── limit: Int
├── total: Int
├── totalPages: Int
├── hasNext: Boolean
└── hasPrev: Boolean

PermissionResponse
├── success: Boolean
├── message: String
└── data: PermissionType

PermissionListResponse
├── success: Boolean
├── message: String
├── data: [PermissionType]
└── pagination: PaginationInfo
```

---

## 🧪 Test Data

```
ID | Key Name | Name | Icon | Feature
---|----------|------|------|--------
1  | permission.create | Create Permission | ➕ | 1
2  | permission.read | Read Permission | 👁️ | 1
3  | permission.update | Update Permission | ✏️ | 1
4  | permission.delete | Delete Permission | 🗑️ | 1
```

---

## 🚀 Common Use Cases

### List All with Pagination

```graphql
{
  permissions(page: 1, limit: 20) {
    success
    data
    pagination
  }
}
```

### Search Specific Permission

```graphql
{
  permissionByKey(keyName: "permission.create") {
    success
    data
  }
}
```

### Get Feature Permissions

```graphql
{
  permissionsByFeature(featureId: 1, page: 1) {
    success
    data
  }
}
```

### Create New Permission

```graphql
mutation {
  createPermission(
    input: {
      keyName: "permission.new"
      name: "New Permission"
      icon: "✨"
      featureId: 1
    }
  ) {
    success
    message
    data {
      id
    }
  }
}
```

### Update Permission

```graphql
mutation {
  updatePermission(id: 1, input: { name: "Updated Name", icon: "🆕" }) {
    success
    data {
      id
      name
    }
  }
}
```

### Delete Permission

```graphql
mutation {
  deletePermission(id: 1) {
    success
    message
  }
}
```

---

## 📞 Error Handling

| Error                  | Cause                  | Solution                 |
| ---------------------- | ---------------------- | ------------------------ |
| "Key already exists"   | Duplicate key_name     | Use different key_name   |
| "Feature not found"    | Invalid feature_id     | Check feature exists     |
| "Permission not found" | Invalid ID or key      | Verify ID/key exists     |
| "Cannot be empty"      | Missing required field | Fill all required fields |
| "Page < 1"             | Invalid page number    | Use page ≥ 1             |

---

**Backend Status**: ✅ COMPLETE & READY
**GraphQL Endpoint**: http://localhost:8000/graphql
**Test with**: GraphQL Playground or GraphQL IDE

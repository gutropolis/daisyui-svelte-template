# Quick Reference Card - Plan Features CRUD

## 🎯 URL Map

| Page               | URL                                      | Purpose        |
| ------------------ | ---------------------------------------- | -------------- |
| Login              | http://localhost:5173/login              | Authentication |
| Plan Features CRUD | http://localhost:5173/admin/plan/feature | **MAIN PAGE**  |
| GraphQL Playground | http://localhost:8000/graphql            | API Testing    |
| Backend API        | http://0.0.0.0:8000                      | API Server     |

---

## 🔄 CRUD Operations

### CREATE

```
Form Field             | Type      | Required | Notes
keyName               | Text      | Yes      | Lowercase, underscores, unique
name                  | Text      | Yes      | Display name
description           | Textarea  | No       | Optional details
```

✅ Creates feature in database
✅ Adds to UI list immediately
✅ Resets form after success

### READ

```
Operation             | Data Returns
Load on Mount         | All features
Click Refresh         | All features (fresh)
```

✅ Displays name, key, description
✅ Shows created_at and updated_at

### UPDATE

```
Click Edit            → Load feature into form
Modify Fields         → Name, Description only (Key locked)
Click Update Feature  → Save changes to database
```

✅ Key name immutable
✅ Other fields editable

### DELETE

```
Click Delete          → Show confirmation
Confirm               → Remove from database
```

✅ Feature removed from list

---

## 📊 Component State

```
Variable          | Type              | Initial | Purpose
features          | PlanFeatureType[] | []      | All plan features
loading           | boolean           | false   | Fetch/save in progress
error             | string            | ''      | Error message
success           | string            | ''      | Success message
isEditing         | boolean           | false   | Edit mode flag
editingId         | number | null     | null    | Which feature editing
formData          | object            | {...}   | Form input values
```

---

## 🎨 UI Elements

### Form Section (Left Panel)

```
┌─────────────────────────────────────┐
│  Create New Feature / Edit Feature  │
├─────────────────────────────────────┤
│ Key Name: [_________] (disabled if editing)
│ Name:     [_________]
│ Desc:     [_________________]
│          (6 rows textarea)
│                                     │
│ [Create Feature] [Cancel if editing]
└─────────────────────────────────────┘
```

### Features List (Right Panel)

```
┌──────────────────────────────────────┐
│ Features List          [🔄 Refresh]  │
├──────────────────────────────────────┤
│ ┌────────────────────────────────────┐
│ │ Feature Name                      │
│ │ feature_key_name                  │
│ │ Description text...               │
│ │ [✏️ Edit] [🗑️ Delete]             │
│ │ Created: Jan 15, 2024 10:30 AM    │
│ │ Updated: Jan 15, 2024 10:45 AM    │
│ └────────────────────────────────────┘
│ (More features...)                   │
└──────────────────────────────────────┘
```

---

## 🔐 Authentication Flow

```
1. User Login
   ↓
2. JWT Token Stored
   ↓
3. Navigate to /admin/plan/feature
   ↓
4. Layout Checks Auth
   ↓
5. GraphQL Request Includes Token
   ↓
6. Backend Validates Token
   ↓
7. Returns Data / Error
```

---

## 📡 GraphQL Queries

### planFeatures (Get All)

```graphql
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
```

**Response Type**: PlanFeaturesListResponse

### planFeature (Get By ID)

```graphql
query {
  planFeature(id: 1) {
    success
    message
    data { ... }
  }
}
```

**Response Type**: PlanFeatureResponse

### planFeatureByKey (Get By Key)

```graphql
query {
  planFeatureByKey(keyName: "trial_management") {
    success
    message
    data { ... }
  }
}
```

**Response Type**: PlanFeatureResponse

---

## ✏️ GraphQL Mutations

### createPlanFeature

```graphql
mutation {
  createPlanFeature(input: {
    keyName: "new_feature"
    name: "New Feature"
    description: "Description"
  }) {
    success, message, data { ... }
  }
}
```

**Input Type**: CreatePlanFeatureInput
**Response Type**: PlanFeatureResponse

### updatePlanFeature

```graphql
mutation {
  updatePlanFeature(id: 1, input: {
    name: "Updated Name"
    description: "Updated Description"
  }) {
    success, message, data { ... }
  }
}
```

**Input Type**: UpdatePlanFeatureInput
**Response Type**: PlanFeatureResponse

### deletePlanFeature

```graphql
mutation {
  deletePlanFeature(id: 1) {
    success
    message
  }
}
```

**Response Type**: PlanFeatureResponse (no data)

---

## 🗄️ Database Schema

### plan_features Table

```sql
Column          | Type              | Constraints
id              | BIGINT            | PRIMARY KEY, AUTO_INCREMENT
key_name        | VARCHAR(100)      | UNIQUE, NOT NULL
name            | VARCHAR(255)      | NOT NULL
description     | TEXT              | NULL
created_at      | DATETIME          | DEFAULT CURRENT_TIMESTAMP
updated_at      | DATETIME          | ON UPDATE CURRENT_TIMESTAMP
```

**Indexes**:

- PRIMARY KEY on `id`
- UNIQUE on `key_name`
- INDEX on `id`
- INDEX on `key_name`

---

## 🧪 Test Data

### Create Test Feature

```
Key Name:     trial_management
Name:         Trial Management
Description:  Ability to create free trials for users
```

### Create Another

```
Key Name:     custom_branding
Name:         Custom Branding
Description:  White-label domain and logo customization
```

---

## ⚙️ Configuration

### Frontend (.env or vite.config.ts)

```
VITE_GRAPHQL_API_URL=http://localhost:8000/graphql
```

### Backend (.env)

```
DATABASE_URL=mysql+pymysql://root:root@localhost/2026_fastdb
```

---

## 🔍 Debugging Tips

### Check Frontend

```
1. Open browser console (F12)
2. Look for GraphQL request logs
3. Check Network tab → GraphQL requests
4. Inspect Response payload
```

### Check Backend

```
1. Look at terminal output
2. Check GraphQL playground
3. Run test query manually
4. Check database directly
```

### Common Errors

```
Error                          | Check
"Failed to load features"      | Backend running?
"401 Unauthorized"             | Logged in?
"Cannot read property 'data'"  | GraphQL response format?
"Key already exists"           | Unique key_name?
```

---

## 📋 Function Map

| Function       | Purpose              | Called By                  |
| -------------- | -------------------- | -------------------------- |
| loadFeatures() | Fetch all features   | onMount, after mutations   |
| handleCreate() | Create new feature   | Form submit (create mode)  |
| handleUpdate() | Update feature       | Form submit (edit mode)    |
| handleDelete() | Delete feature       | Delete button              |
| startEdit()    | Load feature to form | Edit button                |
| resetForm()    | Clear form           | After create/update/cancel |
| formatDate()   | Format timestamp     | Display in template        |

---

## 🎨 Styling Classes

### Status Messages

```
Success:  bg-green-50 border-green-200 text-green-800
Error:    bg-red-50 border-red-200 text-red-800
```

### Buttons

```
Primary:  bg-blue-600 hover:bg-blue-700
Danger:   bg-red-500 hover:bg-red-600
Secondary: bg-gray-300 hover:bg-gray-400
Disabled: bg-gray-400 disabled:bg-gray-400
```

### Containers

```
Main:      max-w-6xl mx-auto
Form:      lg:col-span-1
List:      lg:col-span-2
Card:      bg-white rounded-lg shadow-md p-6
```

---

## 📈 Data Flow

```
Component Mount
    ↓
loadFeatures() → GraphQL Query
    ↓
Response Received
    ↓
Update features array
    ↓
Re-render List
    ↓
User interacts → Action Handler
    ↓
GraphQL Mutation
    ↓
Mutation Response
    ↓
loadFeatures() (refresh)
    ↓
Update UI + Show Message
```

---

## ✅ Validation Rules

### Key Name

- ✓ Lowercase only
- ✓ Underscores allowed
- ✓ Numbers allowed
- ✓ Must be unique
- ✗ No spaces or special chars
- ✗ Cannot be empty

### Name

- ✓ Any characters
- ✓ Can be empty initially? No (required)
- ✓ Max 255 characters
- ✓ Can have spaces

### Description

- ✓ Any characters
- ✓ Can be empty
- ✓ Unlimited length (TEXT field)

---

## 🎯 Keyboard Shortcuts

| Key   | Action                  |
| ----- | ----------------------- |
| Enter | Submit form             |
| Esc   | Not handled (could add) |
| Tab   | Navigate form fields    |

---

## 📱 Responsive Breakpoints

```
Mobile (< lg):
- Form and List stack vertically
- Full width layout

Desktop (>= lg):
- Form: 1/3 width (left)
- List: 2/3 width (right)
- Side-by-side layout
```

---

## 🔗 Related Resources

**Backend Documentation**:

- FastAPI Docs: http://localhost:8000/docs
- GraphQL Schema: http://localhost:8000/graphql (explore)

**Frontend Docs**:

- Svelte: https://svelte.dev
- SvelteKit: https://kit.svelte.dev
- Tailwind CSS: https://tailwindcss.com

**Database**:

- MySQL Docs: https://dev.mysql.com/doc/

---

## 📞 Quick Support

| Problem                  | Solution                  |
| ------------------------ | ------------------------- |
| Page won't load          | Check backend is running  |
| Features don't appear    | Click Refresh button      |
| Can't create             | Check key_name is unique  |
| Edit button doesn't work | Try refreshing page       |
| Timestamps wrong         | Check server timezone     |
| CORS error               | Check backend CORS config |

---

**Last Updated**: January 2024
**Status**: Production Ready ✨

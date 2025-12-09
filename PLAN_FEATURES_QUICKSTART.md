# Plan Features CRUD - Quick Start Guide

## 🚀 Access the Application

### 1. Start the Backend

```bash
cd backend
source venv/Scripts/activate  # Windows: venv\Scripts\activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend running at: http://0.0.0.0:8000
✅ GraphQL endpoint: http://localhost:8000/graphql

### 2. Start the Frontend

```bash
cd frontend
npm run dev
```

✅ Frontend running at: http://localhost:5173

### 3. Login/Register

- Navigate to http://localhost:5173/login
- Create account or login with existing credentials

### 4. Access Plan Features CRUD

- Navigate to: http://localhost:5173/admin/plan/feature
- You should see the Plan Features management page

---

## 📝 Using the Plan Features CRUD Page

### Create a Feature

1. Fill in the form on the left side:
   - **Key Name**: `unique_feature_name` (lowercase with underscores)
   - **Name**: `Feature Display Name`
   - **Description**: Optional detailed description
2. Click "Create Feature"
3. Feature appears in the list on the right

### Edit a Feature

1. Click "✏️ Edit" on any feature in the list
2. Feature loads into the form
3. Modify the Name or Description (Key Name is locked)
4. Click "Update Feature"

### Delete a Feature

1. Click "🗑️ Delete" on any feature
2. Confirm deletion in the dialog
3. Feature is removed

### View/Refresh

- Features automatically load on page visit
- Click "🔄 Refresh" to manually refresh the list
- Each feature shows creation and update timestamps

---

## 🧪 Testing with GraphQL Playground

### Access GraphQL Playground

- Go to: http://localhost:8000/graphql
- Login token required in headers

### Example: Get All Features

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

### Example: Create Feature

```graphql
mutation {
  createPlanFeature(
    input: {
      keyName: "advanced_analytics"
      name: "Advanced Analytics"
      description: "Detailed analytics dashboard"
    }
  ) {
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

### Example: Update Feature

```graphql
mutation {
  updatePlanFeature(
    id: 1
    input: {
      name: "Premium Analytics"
      description: "Enhanced analytics with AI insights"
    }
  ) {
    success
    message
    data {
      id
      keyName
      name
    }
  }
}
```

### Example: Delete Feature

```graphql
mutation {
  deletePlanFeature(id: 1) {
    success
    message
  }
}
```

---

## 🛠️ Troubleshooting

### Page Not Loading

**Problem**: "Page not found" when accessing `/admin/plan/feature`

- **Solution**: Ensure backend is running and you're logged in

### GraphQL Errors

**Problem**: "Failed to load features: Network error"

- **Check**:
  - Backend running on http://0.0.0.0:8000
  - Frontend VITE_GRAPHQL_API_URL points to http://localhost:8000/graphql
  - Check browser console for CORS errors

### Features Not Displaying

**Problem**: Form works but list is empty

- **Check**:
  - Create a feature first
  - Click "Refresh" button to reload
  - Check browser console for GraphQL errors

### "Key name already exists"

**Problem**: Cannot create feature with same key_name

- **Solution**: Key names must be unique, use different name

### Cannot Edit Key Name

**Problem**: Key Name field is disabled when editing

- **This is correct behavior**: Key names are immutable in this system
- **Solution**: Delete and recreate feature if key name needs to change

---

## 📂 File Structure

```
frontend/
├── src/
│   ├── lib/
│   │   ├── modal/
│   │   │   └── user.ts (✨ PlanFeatureType added)
│   │   ├── stores/
│   │   │   └── auth.ts (authentication)
│   │   └── graphql/
│   │       └── client.ts (GraphQL client)
│   └── routes/
│       └── (app)/
│           ├── +layout.svelte (auth check)
│           └── admin/
│               └── plan/
│                   └── feature/
│                       └── +page.svelte (✨ NEW CRUD PAGE)
```

---

## 🔐 Authentication Flow

1. **User logs in** → JWT token stored in browser
2. **Navigate to admin area** → Layout checks authentication
3. **GraphQL requests** → Token included in Authorization header
4. **Backend validates** → Returns data if authorized
5. **Page displays** → Features shown in UI

All handled automatically by the framework!

---

## 📊 Database Schema

### Table: `plan_features`

```sql
CREATE TABLE plan_features (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  key_name VARCHAR(100) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX ix_plan_features_id (id),
  INDEX ix_plan_features_key_name (key_name)
);
```

---

## 🎯 What's Included

### ✅ Complete CRUD Operations

- **Create**: Add new plan features
- **Read**: View all features with filters
- **Update**: Modify existing features
- **Delete**: Remove features with confirmation

### ✅ Modern UI/UX

- Responsive design (mobile & desktop)
- Real-time form validation
- Loading states & spinners
- Error messages & success alerts
- Timestamp display
- Confirmation dialogs

### ✅ Security

- Authentication required
- Authorization via layout
- CORS configured
- Secure token handling

### ✅ Error Handling

- Network error handling
- Validation error messages
- Graceful fallbacks
- Console logging for debugging

---

## 📞 Support

### Common Issues

| Issue                           | Solution                                  |
| ------------------------------- | ----------------------------------------- |
| Can't create feature            | Check key_name is unique and lowercase    |
| Page shows "loading..." forever | Check backend is running                  |
| 401 Unauthorized                | Login again, token might be expired       |
| CORS error                      | Ensure backend CORS includes frontend URL |
| Feature not appearing           | Click Refresh button to reload            |

### Debug Mode

- Open browser Developer Console (F12)
- GraphQL requests are logged with ✅/❌ indicators
- Check Network tab for actual API responses

---

## 🚀 Next Steps

1. ✅ Create test plan features
2. ✅ Try editing and deleting features
3. ✅ Check GraphQL playground at `/graphql`
4. ✅ Monitor browser console for any errors
5. ✅ Consider adding features like:
   - Bulk operations
   - Search/filtering
   - Pagination
   - Export to CSV

---

## 📝 Notes

- **Key Name**: Immutable after creation, used as unique identifier
- **Name**: Editable display name for the feature
- **Description**: Optional detailed information
- **Timestamps**: Automatically managed by database
- **Auto-refresh**: List refreshes after each operation

Enjoy managing your plan features! 🎉

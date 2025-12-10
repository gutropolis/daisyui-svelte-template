# Plan CRUD - Restructured Routes

## 📍 Route Structure

Your Plan CRUD system is now organized with separate routes for each operation:

```
/admin/plan                    → List all plans (with filter, search, pagination)
/admin/plan/new                → Create new plan (with feature toggles)
/admin/plan/[id]               → View plan details
/admin/plan/[id]/edit          → Edit plan (with feature toggles)
```

## 🎯 Features

### a) Listing Page (`/admin/plan`)

- ✅ Display all plans in a responsive grid (1 col mobile → 3 cols desktop)
- ✅ Search & Filter modal
- ✅ Pagination modal with quick jump
- ✅ Action buttons per plan:
  - **✏️ Edit** → Navigate to `/admin/plan/[id]/edit`
  - **👁️ View** → Navigate to `/admin/plan/[id]`
  - **🗑️ Delete** → Delete with confirmation
- ✅ "New Plan" button in header → Navigate to `/admin/plan/new`
- ✅ Refresh, search, and pagination controls

### b) Create New Plan (`/admin/plan/new`)

- ✅ Form for all plan fields:
  - Slug (required, unique, immutable)
  - Name (required)
  - Price (required, decimal)
  - Duration Days (required, min 1)
  - Max Users (optional, blank = unlimited)
  - Max Studies (optional, blank = unlimited)
  - Max Storage GB (optional, blank = unlimited)
- ✅ **Feature Toggles** - Select features with checkboxes
  - Shows all available features
  - Displays selected count
  - Array of feature IDs sent with plan
- ✅ Create & Cancel buttons
- ✅ Redirect to listing on success

### c) Edit Plan (`/admin/plan/[id]/edit`)

- ✅ Pre-populated form with plan data
- ✅ Slug field is read-only (immutable)
- ✅ All other fields editable
- ✅ **Feature Toggles** - Update selected features
  - Pre-selected based on current plan features
  - Update feature selection
  - Same array-based storage
- ✅ Update & Cancel buttons
- ✅ Redirect to listing on success

### d) View Plan (`/admin/plan/[id]`)

- ✅ Display-only view of all plan details
- ✅ Price and duration highlighted
- ✅ Limits section (shows unlimited if NULL)
- ✅ Included features list with checkmarks
- ✅ Metadata (created, updated, ID, status)
- ✅ Edit and Back buttons

## 🔄 Data Flow

### Create New Plan

1. Click "New Plan" button on listing page
2. Navigate to `/admin/plan/new`
3. Fill form, select features with toggles
4. Click "Create Plan"
5. GraphQL mutation sends selected feature IDs as array
6. On success, redirect to `/admin/plan`

### Edit Existing Plan

1. Click "Edit" on plan card
2. Navigate to `/admin/plan/{id}/edit`
3. Form pre-populated with current data
4. Slug shown as read-only
5. Features pre-selected based on plan
6. Modify any field and feature selection
7. Click "Update Plan"
8. GraphQL mutation sends updated feature IDs
9. On success, redirect to `/admin/plan`

### View Plan Details

1. Click "View" on plan card
2. Navigate to `/admin/plan/{id}`
3. Display all plan information
4. Show selected features with checkmarks
5. Option to "Edit Plan" from detail page

### Delete Plan

1. Click "Delete" on plan card
2. Confirmation dialog
3. GraphQL mutation deletes plan
4. List refreshes, plan removed

## 📦 Components

### Main Pages

- **+page.svelte** (Listing) - List plans with filters & pagination
- **new/+page.svelte** - Create plan form with feature toggles
- **[id]/+page.svelte** - View plan details
- **[id]/edit/+page.svelte** - Edit plan form with feature toggles

### Shared Components

- **PlanCard.svelte** - Displays plan in grid with action buttons
- **PaginationModal.svelte** - Pagination controls
- **FilterModal.svelte** - Search & filter
- **PlanList.svelte** - (Legacy) No longer used in main list
- **PlanAddForm.svelte** - (Legacy) Replaced by new/+page.svelte
- **PlanEditForm.svelte** - (Legacy) Replaced by [id]/edit/+page.svelte

## ✨ Feature Toggles Implementation

Both new and edit forms include feature toggles:

```svelte
<!-- Feature Toggle Example -->
{#each features as feature}
	<label class="flex items-center gap-3">
		<input
			type="checkbox"
			checked={selectedFeatures.has(feature.id)}
			on:change={() => toggleFeature(feature.id)}
		/>
		<div>
			<p>{feature.name}</p>
			<p>Feature ID: {feature.id}</p>
		</div>
	</label>
{/each}

<!-- Selected features converted to array -->
{#if selectedFeatures.size > 0}
	<p>{selectedFeatures.size} feature(s) selected</p>
{/if}
```

Features are:

- ✅ Loaded from `planFeatures` GraphQL query
- ✅ Stored as `Set<number>` for toggle management
- ✅ Converted to `Array.from(selectedFeatures)` for GraphQL mutation
- ✅ Sent as array of IDs in `features` field

## 🎨 UI Improvements

- Responsive grid layout (1-3 columns)
- Consistent color scheme with Tailwind
- Clear action buttons with icons
- Confirmation dialogs for destructive actions
- Success/error messages
- Loading states
- Back navigation links
- Form validation with helpful messages

## 🔗 GraphQL Integration

### Queries

- `plans(page, limit, filterInput)` - List plans
- `plan(id)` - Get single plan
- `planFeatures()` - Get all features

### Mutations

- `createPlan(input)` - Create with features array
- `updatePlan(id, input)` - Update with features array
- `deletePlan(id)` - Delete plan

### Feature Array Handling

```typescript
// Send to GraphQL
features: Array.from(selectedFeatures)  // [1, 2, 3]

// Receive from GraphQL
plan.features: number[]  // [1, 2, 3]

// Initialize toggle
selectedFeatures = new Set(plan.features)
```

## 🚀 Usage Flow

```
User visits /admin/plan
    ↓
See list of plans with search & pagination
    ↓
Click "New Plan" OR Click "Edit" on a card
    ↓
Fill form with feature toggles
    ↓
Submit
    ↓
GraphQL mutation with feature array
    ↓
Redirect to /admin/plan
    ↓
List refreshed
```

## 📋 Checklist

- [x] Listing page with grid layout
- [x] Create new plan route with feature toggles
- [x] Edit plan route with feature toggles
- [x] View plan details route
- [x] Search & filter modal
- [x] Pagination modal
- [x] Action buttons (Edit, View, Delete)
- [x] Feature toggle implementation
- [x] GraphQL mutations with feature arrays
- [x] Success/error messages
- [x] Responsive design
- [x] Back navigation

## 🔄 Removed Components

The following components are no longer used in the main listing:

- `PlanList.svelte`
- `PlanAddForm.svelte`
- `PlanEditForm.svelte`

They can be deleted or kept for reference. The new structure uses dedicated pages instead.

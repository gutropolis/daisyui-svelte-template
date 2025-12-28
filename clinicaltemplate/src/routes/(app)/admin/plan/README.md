# Plan CRUD Components

This directory contains a complete CRUD system for managing subscription plans with separate Add and Edit forms.

## Components

### Main Page

- **+page.svelte** - Main plan management page with form switching between Add and Edit modes

### Forms

- **PlanAddForm.svelte** - Form for creating new plans
- **PlanEditForm.svelte** - Form for editing existing plans (slug is immutable)

### Display

- **PlanList.svelte** - Container displaying list of plans
- **PlanCard.svelte** - Individual plan card with edit/delete actions

### Modals

- **PaginationModal.svelte** - Modal for pagination controls
- **FilterModal.svelte** - Modal for searching/filtering plans

## Features

✅ **Create Plans** - Add new subscription plans with all details
✅ **Edit Plans** - Update existing plans (slug cannot be changed)
✅ **Delete Plans** - Remove plans with confirmation
✅ **Search/Filter** - Search by plan name or slug (case-insensitive)
✅ **Pagination** - Page-based navigation with quick jump
✅ **Separate Forms** - Add and Edit use distinct components
✅ **Form Validation** - Required fields and duration validation
✅ **Loading States** - Visual feedback during operations
✅ **Error Handling** - User-friendly error messages
✅ **Success Messages** - Confirmation on successful operations

## Usage

### Basic Flow

1. **View Plans** - See all plans in the list
2. **Add New Plan** - Fill out PlanAddForm, click "Create Plan"
3. **Edit Plan** - Click "Edit" on a card, form switches to PlanEditForm
4. **Delete Plan** - Click "Delete" with confirmation
5. **Search** - Use FilterModal to search by name/slug
6. **Navigate** - Use PaginationModal for pagination

### GraphQL Operations

All components use GraphQL mutations and queries:

**Queries:**

- `plans` - Get paginated list of plans (with filtering)
- `plan` - Get single plan by ID
- `planBySlug` - Get plan by slug

**Mutations:**

- `createPlan` - Create new plan
- `updatePlan` - Update existing plan
- `deletePlan` - Delete plan

## Component Props

### PlanAddForm

```svelte
export let loading: boolean
export let success: string
export let error: string
export let onSuccess: () => Promise<void>
```

### PlanEditForm

```svelte
export let plan: Plan
export let loading: boolean
export let success: string
export let error: string
export let onSuccess: () => Promise<void>
export let onCancel: () => void
```

### PlanList

```svelte
export let plans: Plan[] export let loading: boolean export let onEdit: (plan: Plan) => void export
let onDelete: (id: number) => void export let onRefresh: () => void
```

### PlanCard

```svelte
export let plan: Plan export let onEdit: (plan: Plan) => void export let onDelete: (id: number) =>
void export let isLoading: boolean
```

## Plan Interface

```typescript
interface Plan {
  id: number
  slug: string                    // Immutable unique identifier
  name: string                    // Plan name
  price: string                   // Price in USD (e.g., "9.99")
  durationDays: number            // Duration in days (min 1)
  maxUsers: number | null         // null = unlimited
  maxStudies: number | null       // null = unlimited
  maxStorageGb: number | null     // null = unlimited
  features: number[]              // Array of feature IDs
  createdAt: string               // ISO date string
  updatedAt: string               // ISO date string
}
```

## Form Validation

### PlanAddForm

- **Slug** - Required, must be unique
- **Name** - Required, display name for plan
- **Price** - Required, decimal format
- **Duration Days** - Required, minimum 1 day
- **Max Users** - Optional, leave blank for unlimited
- **Max Studies** - Optional, leave blank for unlimited
- **Max Storage (GB)** - Optional, leave blank for unlimited
- **Features** - Optional, comma-separated feature IDs

### PlanEditForm

- **Slug** - Read-only (immutable)
- **Name** - Required
- **Price** - Required
- **Duration Days** - Required, minimum 1 day
- **Max Users** - Optional
- **Max Studies** - Optional
- **Max Storage (GB)** - Optional
- **Features** - Optional, comma-separated feature IDs

## Error Handling

The components handle various error scenarios:

- Network errors
- Validation errors
- Duplicate slug errors
- Database errors
- GraphQL errors

Errors are displayed to the user in red alert boxes with clear messages.

## UI/UX

- **Responsive Design** - Grid layout with 1 column on mobile, 3 columns on desktop
- **Form Switching** - Seamless toggle between Add and Edit modes
- **Clear Visual Feedback** - Loading states, success/error messages
- **Intuitive Controls** - Buttons, modals, and confirmations
- **Professional Styling** - DaisyUI/Tailwind CSS

## Integration Notes

- Uses `$lib/graphql/client` for GraphQL requests
- Assumes Plan GraphQL schema is available
- Pagination is page-based with limit of 10 per page
- Search is case-insensitive across name and slug fields
- Features are stored as comma-separated IDs in the form

## Customization

### Change Items Per Page

Edit in `+page.svelte` line with `limit: 10` to desired value

### Add Feature Selection

Replace features string input with a select dropdown and load from GraphQL

### Add Additional Fields

Follow the pattern of existing fields in both form components

## Testing

Test the CRUD flow:

1. Create a plan ✓
2. View in list ✓
3. Edit the plan ✓
4. Delete the plan ✓
5. Search by name/slug ✓
6. Navigate pages ✓

All operations should complete successfully with appropriate feedback.

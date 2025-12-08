# 🚀 Complete Testing Guide - Authentication Flow

## Prerequisites

### 1. Backend Running

```powershell
cd e:\project\daisyui-svelte-template\backend
python -m uvicorn main:app --port 8000
```

**Expected Output:**

```
INFO:     Started server process [XXXX]
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 2. Frontend Dev Server

```powershell
cd e:\project\daisyui-svelte-template\frontend
npm run dev
```

**Expected Output:**

```
  VITE v5.x.x

  ➜  Local:   http://localhost:5173/
  ➜  press h to show help
```

### 3. MySQL Running

- Ensure MySQL server is running
- Database `2026_fastdb` exists

---

## Complete Authentication Flow Test

### Step 1: Verify Backend is Accessible

**URL:** `http://localhost:8000/graphql`

**Expected:** Strawberry GraphQL interface loads

**If it fails:**

- Check backend terminal for errors
- Verify port 8000 is not in use
- Check MySQL connection

---

### Step 2: Test GraphQL Connection

**URL:** `http://localhost:5173/test-graphql`

1. Click **"Test Connection"** button
2. Check browser **Console** (F12 → Console tab)
3. Should see: `✅ GraphQL Response`

**Expected Response:**

```json
{
	"hello": "Welcome to DaisyUI Healthcare GraphQL API!"
}
```

**If it fails:**

- Check Network tab (F12 → Network) for request
- Look for error in Response tab
- Verify VITE_GRAPHQL_API_URL in .env.local

---

### Step 3: Register New User

**URL:** `http://localhost:5173/auth/register`

1. Fill in form:
   - **Email:** `testuser@example.com`
   - **Password:** `TestPassword@123`
   - **Confirm Password:** `TestPassword@123`
   - **Full Name:** `Test User`
   - **Contact Number:** `1234567890` (optional)

2. Check **"I agree to terms"** checkbox

3. Click **"Create Account"** button

4. **Monitor Console (F12 → Console):**

   ```
   🔐 Attempting login with: { email: 'testuser@example.com' }
   📡 API URL: http://localhost:8000/graphql
   📤 GraphQL Request: { operation: 'Register', ... }
   ✅ GraphQL Response: { data: { register: { success: true, ... } } }
   🔑 Tokens saved successfully
   ```

5. **Should redirect to `/dashboard`** with "Verifying access..." spinner

**If it fails:**

- Check Console for error message
- Check Network tab for GraphQL request
- Look at backend terminal for Python errors

---

### Step 4: Verify User in Database

```powershell
mysql -u root -p

USE 2026_fastdb;

SELECT id, email, full_name, role, is_active FROM users WHERE email = 'testuser@example.com';
```

**Expected Output:**

```
+----+---------------------+-----------+-------+-----------+
| id | email               | full_name | role  | is_active |
+----+---------------------+-----------+-------+-----------+
|  1 | testuser@example.com| Test User | USER  |         1 |
+----+---------------------+-----------+-------+-----------+
```

---

### Step 5: View Dashboard

**URL:** `http://localhost:5173/dashboard`

**Expected:**

- Loading spinner disappears
- Full name displayed: "Test User"
- Email displayed: "testuser@example.com"
- Contact number displayed: "1234567890"
- Role displayed: "USER" (blue badge)
- Status displayed: "Active" (green badge)

**Console should show:**

```
✅ User authenticated, allowing access to protected route
```

---

### Step 6: Logout

1. Click **"Logout"** button on dashboard

2. **Should redirect to login page** (`/auth/login`)

3. **Check Console:**

   ```
   🔓 Auth token cleared
   ```

4. **Check localStorage (F12 → Application → Local Storage):**
   - `auth_tokens` key should be **gone**

---

### Step 7: Login Again

**URL:** `http://localhost:5173/auth/login`

1. Enter credentials:
   - **Email:** `testuser@example.com`
   - **Password:** `TestPassword@123`

2. Click **"Login"** button

3. **Monitor Console:**

   ```
   📝 Form submitted with: { email: 'testuser@example.com' }
   📤 Login result: { success: true, message: '...', token: {...} }
   ✅ Login successful, redirecting...
   ```

4. **Should redirect to `/dashboard`** again

---

## Network Tab Inspection

### How to View GraphQL Requests

1. Open **DevTools**: Press `F12`
2. Go to **Network** tab
3. Click login/register button
4. Look for request to `localhost:8000/graphql`
5. Click the request
6. Check **Response** tab

### Expected Register Request

```json
{
	"data": {
		"register": {
			"success": true,
			"message": "User registered successfully",
			"token": {
				"accessToken": "eyJ...",
				"refreshToken": "eyJ...",
				"tokenType": "bearer"
			}
		}
	}
}
```

### Expected Login Request

```json
{
	"data": {
		"login": {
			"success": true,
			"message": "Login successful",
			"token": {
				"accessToken": "eyJ...",
				"refreshToken": "eyJ...",
				"tokenType": "bearer"
			}
		}
	}
}
```

---

## Console Logging Guide

### Register Success

```
🔐 Attempting login with: { email: 'testuser@example.com' }
📡 API URL: http://localhost:8000/graphql
📤 GraphQL Request: { operation: 'Register', variables: {...} }
✅ GraphQL Response: { data: { register: { success: true, ... } } }
🔑 Tokens saved successfully
✅ Registration successful, redirecting...
```

### Login Success

```
📝 Form submitted with: { email: 'testuser@example.com' }
📤 Login result: { success: true, message: 'Login successful', token: {...} }
✅ Login successful, redirecting...
✅ User authenticated, allowing access to protected route
```

### Login Failure

```
📝 Form submitted with: { email: 'wrong@example.com' }
📤 Login result: { success: false, message: 'Invalid email or password', ... }
❌ Login failed: Invalid email or password
```

---

## Troubleshooting

### Error: "Failed to fetch" or Network Error

**Cause:** Backend is not running

**Solution:**

```powershell
# Terminal 1 (Backend)
cd backend
python -m uvicorn main:app --port 8000

# Check it's running:
curl http://localhost:8000/graphql
```

### Error: "Cannot POST /graphql"

**Cause:** GraphQL route not registered in FastAPI

**Solution:** Check backend `main.py` has GraphQL router:

```python
graphql_app = GraphQLRouter(schema, context_getter=lambda: get_db_for_graphql())
app.include_router(graphql_app, prefix="/graphql")
```

### Error: "Invalid email or password"

**Cause:** User doesn't exist OR password is wrong

**Solution:**

1. Register a new user first at `/auth/register`
2. Use the same credentials to login
3. Passwords are case-sensitive

### Error: "localStorage is not defined"

**Cause:** Code is running on server-side

**Solution:** Already fixed! All localStorage access is guarded by `isBrowser()` check

### Redirect Loop / Infinite Redirects

**Cause:** Auth check is running too often

**Solution:** Already fixed! Using `onMount()` instead of `$effect()`

---

## Expected User Journey

```
1. Visit http://localhost:5173
   ↓
2. Auto-redirects to /auth/login
   (because not authenticated)
   ↓
3. Click "Create an account" link
   ↓
4. Fill register form and submit
   ↓
5. Auto-redirects to /dashboard
   (because now authenticated)
   ↓
6. See user profile
   ↓
7. Click "Logout"
   ↓
8. Auto-redirects to /auth/login
   (because no longer authenticated)
   ↓
9. Fill login form and submit
   ↓
10. Auto-redirects to /dashboard
    (because authenticated again)
```

---

## Success Indicators

✅ **Register Page Works:**

- No console errors
- Form submits
- Redirects to dashboard

✅ **Dashboard Page Works:**

- Shows user info
- Shows sidebar + header + footer
- Logout button works

✅ **Login Page Works:**

- Accepts credentials
- Stores tokens in localStorage
- Redirects to dashboard

✅ **Protected Routes Work:**

- Unauthenticated users redirected to login
- Authenticated users see content
- Loading spinner shows briefly

✅ **No Errors:**

- Console is clean (no red errors)
- Network requests succeed (status 200)
- Backend terminal shows no errors

---

## Advanced Testing

### Test with Network Tab Filter

1. Open DevTools (F12)
2. Network tab
3. Click **"XHR"** button to filter requests
4. Register/Login
5. See GraphQL POST request
6. Click request → Response tab → See JSON

### Test localStorage

1. Open DevTools (F12)
2. Application tab
3. Local Storage
4. Click `http://localhost:5173`
5. Should see `auth_tokens` key after login
6. Should be empty after logout

### Test Redirect Logic

1. Register and get redirected to dashboard
2. Manually go to `/auth/login`
3. Should still be able to access (redirects if not auth)
4. Logout
5. Try to access `/dashboard`
6. Should redirect to `/auth/login`

---

## Complete Test Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 5173
- [ ] MySQL running with database
- [ ] Visit /test-graphql page - connection works
- [ ] Visit /auth/register page - loads without errors
- [ ] Register new user - form submits successfully
- [ ] Verify user in database with MySQL
- [ ] Dashboard shows - user info displays correctly
- [ ] Logout button works - redirects to login
- [ ] Login with same credentials - works successfully
- [ ] Check localStorage - auth_tokens present after login
- [ ] Check localStorage - auth_tokens cleared after logout
- [ ] Console has no red errors
- [ ] Network tab shows GraphQL requests (POST to /graphql)
- [ ] Verify user role, status, and dates display correctly

---

## What to Do If Something Fails

1. **Check Console (F12 → Console)**
   - Look for red error messages
   - Check for missing module errors
   - Check GraphQL error messages

2. **Check Network Tab (F12 → Network)**
   - Filter by XHR
   - Click GraphQL request
   - Check Response for error details
   - Check if status is 200 or error code

3. **Check Backend Terminal**
   - Look for Python errors
   - Check database connection errors
   - Check GraphQL schema errors

4. **Check Browser Console for Logs**
   - 📝 Form submitted
   - 📤 GraphQL Request
   - ✅ GraphQL Response
   - ❌ GraphQL Error
   - 🔑 Tokens saved

5. **Verify Files Exist**
   - `src/lib/auth.ts`
   - `src/lib/stores/auth.ts`
   - `src/lib/modal/user.ts`
   - `src/lib/graphql/client.ts`
   - `src/lib/graphql/operations.ts`

---

**Now you're ready to test the complete authentication flow!** 🎉

If you encounter any issues, check the console logs first - they're very detailed!

# 🔧 Login Troubleshooting Guide

## Quick Diagnosis Steps

### Step 1: Check if Backend is Running

The backend needs to be running on `http://localhost:8000` for login to work.

**In PowerShell terminal, run:**

```powershell
cd e:\project\daisyui-svelte-template\backend
.\venv\Scripts\python.exe -m uvicorn main:app --port 8000 --host 0.0.0.0
```

**Expected output:**

```
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
Starting DaisyUI Healthcare API v1.0.0
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ **If you see this**, backend is working!

---

### Step 2: Test GraphQL Connection

Visit this debug page:

```
http://localhost:5173/test-graphql
```

1. Click **"Test Connection"** button
2. Check if you get a response

**Expected Response:**

```json
{
	"hello": "Welcome to DaisyUI Healthcare GraphQL API!"
}
```

✅ **If you see this**, GraphQL is working!

---

### Step 3: Check if User Exists

The credentials `user@example.com / 123456` will only work if this user was already registered.

**Option A: Register a new user first**

1. Go to `http://localhost:5173/auth/register`
2. Fill in the form:
   - Email: `testuser@example.com`
   - Password: `SecurePass123`
   - Full Name: `Test User`
   - Contact Number: (optional)
3. Click "Register"
4. Then try logging in with these credentials

**Option B: Check database directly**

```powershell
# Open MySQL
mysql -u root -p

# Use the database
USE 2026_fastdb;

# View all users
SELECT id, email, full_name, is_active FROM users;
```

---

## Common Issues & Solutions

### ❌ Error: "Failed to fetch" or Network Error

**Problem:** Backend is not running or not accessible

**Solution:**

1. Open PowerShell terminal
2. Navigate to backend: `cd backend`
3. Start server: `.\venv\Scripts\python.exe -m uvicorn main:app --port 8000 --host 0.0.0.0`
4. Try login again

---

### ❌ Error: "Invalid email or password"

**Problem:** Either the email doesn't exist OR password is wrong

**Solution:**

1. Go to `/auth/register` and create a new account
2. Use the SAME credentials when logging in
3. Remember: Passwords are case-sensitive and require exact match

---

### ❌ Error: "User account is inactive"

**Problem:** The user exists but is marked as inactive in the database

**Solution:**

```powershell
mysql -u root -p
USE 2026_fastdb;
UPDATE users SET is_active = 1 WHERE email = 'user@example.com';
```

---

### ❌ CORS Error or 404 Not Found

**Problem:** Frontend and backend are not connecting

**Checks:**

1. Is backend running on port 8000? (Check terminal)
2. Is `.env.local` set correctly? Check:

   ```
   cat frontend/.env.local
   ```

   Should show: `VITE_GRAPHQL_API_URL=http://localhost:8000/graphql`

3. Try visiting backend directly:
   ```
   http://localhost:8000/graphql
   ```
   Should show Strawberry GraphQL interface

---

### ❌ "Module not found" or Import Errors

**Problem:** There's a Python or Node module missing

**Solution for Backend:**

```powershell
cd backend
.\venv\Scripts\pip install -r requirements.txt
```

**Solution for Frontend:**

```powershell
cd frontend
npm install
```

---

## Step-by-Step Working Flow

### 1️⃣ Start Backend

```powershell
cd e:\project\daisyui-svelte-template\backend
.\venv\Scripts\python.exe -m uvicorn main:app --port 8000 --host 0.0.0.0
```

### 2️⃣ In Another Terminal, Start Frontend

```powershell
cd e:\project\daisyui-svelte-template\frontend
npm run dev
```

Frontend should be at: `http://localhost:5173`

### 3️⃣ Test GraphQL Connection

Visit: `http://localhost:5173/test-graphql`
Click "Test Connection" - should show success message

### 4️⃣ Register a New User

Visit: `http://localhost:5173/auth/register`

Fill in:

- Email: `testuser@example.com`
- Password: `SecurePassword@123`
- Full Name: `Test User`
- Contact Number: `1234567890` (optional)

Click Register → Should redirect to dashboard

### 5️⃣ Go Back to Login

Visit: `http://localhost:5173/auth/login`

Enter:

- Email: `testuser@example.com`
- Password: `SecurePassword@123`

Click Login → Should redirect to dashboard

---

## Debug With Browser Console

### How to Open Console

- Press `F12` or `Ctrl+Shift+I`
- Click the "Console" tab

### What to Look For

**Successful login logs:**

```
🔐 Attempting login with: {email: 'testuser@example.com'}
📡 API URL: http://localhost:8000/graphql
✅ Login response: {login: {success: true, message: '...', token: {...}}}
🔑 Tokens saved successfully
📝 Form submitted with: {email: 'testuser@example.com'}
✅ Login successful, redirecting...
```

**Failed login logs:**

```
❌ Login error: GraphQLError: ...
Error details: {message: '...', error: Error ...}
❌ Login failed: Invalid email or password
💥 Exception during login: Error: ...
```

---

## Verify Backend Database

```powershell
# Check if database exists and has users table
mysql -u root -p 2026_fastdb

# In MySQL console:
SHOW TABLES;  -- Should show: users, alembic_version

-- Check all users
SELECT id, email, full_name, role, is_active, created_at FROM users;

-- Check specific user
SELECT * FROM users WHERE email = 'testuser@example.com'\G

-- Check migration status
SELECT * FROM alembic_version;
```

---

## API Endpoints Reference

| Endpoint                        | Purpose                     |
| ------------------------------- | --------------------------- |
| `http://localhost:8000/`        | Root API info               |
| `http://localhost:8000/graphql` | GraphQL interface           |
| `http://localhost:8000/docs`    | API documentation (Swagger) |
| `http://localhost:8000/health`  | Health check                |

---

## Quick Fix Checklist

- [ ] Backend is running (`python -m uvicorn main:app --port 8000`)
- [ ] Frontend is running (`npm run dev`)
- [ ] `.env.local` exists with `VITE_GRAPHQL_API_URL=http://localhost:8000/graphql`
- [ ] MySQL is running (`mysql -u root -p`)
- [ ] Database `2026_fastdb` exists
- [ ] User `user@example.com` exists in database
- [ ] No errors in browser console (F12)
- [ ] No errors in backend terminal
- [ ] Can access `/test-graphql` page successfully

---

## Getting Help

### Check Logs

**Browser Console (F12):**

- Shows frontend JavaScript errors
- Shows GraphQL request details
- Shows login flow logs

**Backend Terminal:**

- Shows Python errors
- Shows database errors
- Shows GraphQL query execution

### If Still Not Working

1. Make sure MySQL is running:

   ```powershell
   # Test MySQL connection
   mysql -u root -p -e "SELECT 1"
   ```

2. Verify database migrations are applied:

   ```powershell
   cd backend
   .\venv\Scripts\python -m alembic current
   ```

3. Check requirements are installed:

   ```powershell
   cd backend
   .\venv\Scripts\pip list | findstr strawberry
   ```

4. Restart everything:
   - Stop backend server (Ctrl+C)
   - Stop frontend server (Ctrl+C)
   - Restart both

---

## Success Indicators

✅ You'll know it's working when:

1. **Register Page**
   - Form submits without errors
   - Redirects to `/dashboard` after success
   - User appears in database

2. **Login Page**
   - Form submits without errors
   - Displays "Welcome Back! 👋"
   - Shows your user info on dashboard
   - Email and password match registered user

3. **Dashboard**
   - Shows your full name, email, role
   - Logout button works
   - Redirects to login when clicking logout

4. **Console Output**
   - No red error messages
   - Green ✅ checkmarks appear during flow
   - GraphQL responses show `success: true`

---

**Last Updated:** December 8, 2025
**Status:** Testing authentication flow

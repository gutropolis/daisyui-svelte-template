# 🌐 How to See GraphQL Responses in Network Tab

## Quick Steps

### 1. Open DevTools

- Press `F12` or `Ctrl+Shift+I`
- Click on **"Network"** tab

### 2. Go to Test Page

- Visit: `http://localhost:5173/test-graphql`

### 3. Click a Test Button

- Click **"Test Connection"** button
- In the Network tab, you should see a request appear

### 4. Find the GraphQL Request

- Look for a request with name containing "graphql" or "localhost:8000"
- It will be a **POST** request (not GET)
- Status should be **200** (success) or **4xx/5xx** (error)

### 5. Click the Request

- Click on the request in the Network tab
- You'll see tabs: **Headers**, **Response**, **Preview**, etc.

### 6. Check the Response Tab

- Click on **"Response"** tab
- You should see the JSON response from GraphQL

---

## What You Should See

### ✅ Success Response (Test Connection)

```json
{
	"data": {
		"hello": "Welcome to DaisyUI Healthcare GraphQL API!"
	}
}
```

### ✅ Success Response (Login)

```json
{
	"data": {
		"login": {
			"success": true,
			"message": "Login successful",
			"token": {
				"accessToken": "eyJ0eXAiOiJKV1QiLCJhbGc...",
				"refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGc...",
				"tokenType": "bearer"
			}
		}
	}
}
```

### ❌ Error Response (Invalid Credentials)

```json
{
	"data": {
		"login": {
			"success": false,
			"message": "Invalid email or password",
			"token": null
		}
	}
}
```

### ❌ Error Response (Backend Not Running)

```json
{
	"errors": [
		{
			"message": "Failed to fetch",
			"extensions": {
				"code": "NETWORK_ERROR"
			}
		}
	]
}
```

---

## Network Request Structure

### What You See in Headers Tab

**Request Headers** (what frontend sends):

```
POST /graphql HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Authorization: Bearer eyJ...

{
  "query": "mutation Login($email: String!, $password: String!) { ... }",
  "variables": {
    "email": "user@example.com",
    "password": "123456"
  }
}
```

**Response Headers** (what backend sends back):

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 1234
```

---

## If You Don't See Network Request

### Problem 1: Form Validation Failed

- **Solution:** Make sure email and password fields are filled before clicking button
- Check Console for validation error message

### Problem 2: Frontend Error

- **Check Console tab** (F12 → Console)
- Look for red errors like "Cannot find module" or "ReferenceError"
- Fix any JavaScript errors first

### Problem 3: No Network Request at All

- **Possible cause:** JavaScript error prevented the request from being sent
- **Solution:** Check Console tab for errors

---

## Debugging Network Issues

### Request Appears but Returns 404

```
Status: 404 Not Found
```

**Means:** Backend is running but GraphQL route is not registered

- Check backend `main.py` for GraphQL router configuration
- Restart backend server

### Request Appears but Returns 500

```
Status: 500 Internal Server Error
```

**Means:** Backend got the request but had an error processing it

- Check **backend terminal** for Python error messages
- Look in Response tab for error details

### No Response Tab Data

```
Status: (cancelled) or (blocked)
```

**Means:** Request was blocked or cancelled

- Check Console for CORS errors
- Verify backend CORS configuration allows your frontend URL

---

## Console Logging Guide

While you're testing, check the **Console** tab (F12) for detailed logs:

### ✅ Successful Test

```
🔗 GraphQL Client initialized with URL: http://localhost:8000/graphql
📤 GraphQL Request: { operation: 'Login', variables: {...} }
✅ GraphQL Response: { data: { login: { success: true, ... } } }
```

### ❌ Failed Test

```
🔗 GraphQL Client initialized with URL: http://localhost:8000/graphql
📤 GraphQL Request: { operation: 'Login', variables: {...} }
❌ GraphQL Error: { message: 'Failed to fetch', ... }
```

---

## Network Tab Tips & Tricks

### 1. Filter by XHR/Fetch

- In Network tab, click **"XHR"** or **"Fetch"** button
- This hides images, CSS, JS files and shows only data requests

### 2. Preserve Log

- Check **"Preserve log"** checkbox
- Logs stay even if you navigate to a new page

### 3. Disable Cache

- Check **"Disable cache"** checkbox
- Forces fresh requests (useful for testing)

### 4. Copy Request/Response

- Right-click the request
- **Copy** → **Copy as cURL** (for testing in terminal)

### 5. Search for GraphQL Requests

- Press `Ctrl+F` in Network tab
- Type "graphql" to find requests

---

## Quick Checklist

Before debugging, verify:

- [ ] Browser DevTools is open (F12)
- [ ] Network tab is selected
- [ ] Backend is running on port 8000
- [ ] Frontend is running on port 5173
- [ ] Visit `/test-graphql` page
- [ ] Click test button
- [ ] Check Network tab for request
- [ ] Click request and check Response tab
- [ ] Look at Console for detailed logs

---

## Common Network Issues

| Issue               | Response Status                 | Solution                                                |
| ------------------- | ------------------------------- | ------------------------------------------------------- |
| Backend not running | Failed to fetch / (blocked)     | Start backend: `python -m uvicorn main:app --port 8000` |
| Wrong API URL       | 404 Not Found                   | Check `.env.local` has correct URL                      |
| User doesn't exist  | 200 OK with `success: false`    | Register user first at `/auth/register`                 |
| Wrong password      | 200 OK with `success: false`    | Password is case-sensitive, verify exact match          |
| Database offline    | 500 Internal Server Error       | Check MySQL is running and database exists              |
| CORS error          | (blocked) or CORS error message | Check backend CORS config allows frontend URL           |

---

## Real World Example Flow

### Step 1: Open DevTools

```
Press F12 → Click Network tab
```

### Step 2: Go to Test Page

```
Navigate to http://localhost:5173/test-graphql
```

### Step 3: Watch Network Tab

```
Should be empty (no requests yet)
```

### Step 4: Click Test Connection

```
[Network tab] → Sees POST request appear
URL: http://localhost:8000/graphql
Status: 200 (if success) or error status (if failed)
```

### Step 5: Examine Request

```
Click on the request
Check "Headers" tab → See the GraphQL query
Check "Response" tab → See { "data": { "hello": "..." } }
Check "Console" tab → See GraphQL logs
```

### Step 6: Debug if Needed

```
If error, check:
- Response tab for error message
- Console tab for JavaScript logs
- Backend terminal for Python errors
```

---

**Now go to `/test-graphql` and test it yourself!**

You'll be able to see exactly what's being sent and received between frontend and backend.

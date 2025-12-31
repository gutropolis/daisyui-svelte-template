# GraphQL Architecture

This project uses a modular GraphQL layout that scales with each Django app.

```
backend/
├─ config/
│  └─ schema.py        # Root Query/Mutation aggregates every app schema
├─ apps/
│  ├─ plan/
│  │  └─ schema/
│  │     ├─ types.py       # DjangoObjectTypes for Plan/Feature/Permission
│  │     ├─ queries.py     # plan-specific query fields
│  │     └─ mutations.py   # plan-specific mutations
│  ├─ subscription/
│  │  └─ schema/
│  │     ├─ types.py
│  │     ├─ queries.py
│  │     └─ mutations.py
│  └─ user/
│     └─ schema/
│        ├─ types.py       # DjangoObjectTypes for User
│        ├─ queries.py     # user-specific query fields (includes auth queries like me, users)
│        └─ mutations.py   # user-specific mutations (includes auth mutations like register, login)
```

To add GraphQL support for another app:

1. Create an `apps/<app>/schema/` folder with `types.py`, `queries.py`, and `mutations.py`.
2. Export `FooQuery`/`FooMutation` from `apps.<app>.schema.__init__`.
3. Mix the new classes into `config/schema.py`:

   ```python
   from apps.foo.schema import FooMutation, FooQuery

   class Query(FooQuery, Query):
       ...
   class Mutation(FooMutation, Mutation):
       ...
   ```

4. Restart the server; the `/graphql` endpoint automatically exposes the new fields.

Use the built-in GraphiQL IDE at `http://localhost:8000/graphql` to explore the API.

## Authentication via `django-graphql-auth`

The project ships with [django-graphql-auth](https://github.com/PedroBern/django-graphql-auth) integrated into the user app schema (`apps/user/schema/`) so you can reuse the standard
registration/login flows in GraphQL:

- `MeQuery` / `UserQuery` are mixed into the `UserQuery` in `apps/user/schema/queries.py`, giving you `me` and user search helpers.
- `UserMutation` in `apps/user/schema/mutations.py` exposes common mutations such as `register`, `tokenAuth`, `refreshToken`,
  `verifyAccount`, `sendPasswordResetEmail`, and more.
- JWT middleware is enabled in `GRAPHENE['MIDDLEWARE']`, and authentication backends are configured in `settings.py`.

Typical client flow:

1. `register` ➜ create user (activation emails are disabled in dev, so account is usable immediately).
2. `tokenAuth` ➜ obtain short-lived JWT for authenticated requests.
3. `refreshToken` / `revokeToken` ➜ manage long-running sessions.

When adding a new app schema, no extra steps are required—just follow the folder convention above and import your query /
mutation classes into `config/schema.py`.

## GraphQL Mutation Examples

Here are complete examples of all authentication mutations available in the user schema. You can copy-paste these into the GraphiQL IDE at `http://localhost:8000/graphql` to test them.

### 1. User Registration

```graphql
mutation {
  register(
    email: "user@example.com"
    password1: "mypassword123"
    password2: "mypassword123"
  ) {
    success
    errors
    token
    refreshToken
    user {
      id
      email
      isActive
    }
  }
}
```

### 2. User Login (Token Authentication)

```graphql
mutation {
  tokenAuth(email: "user@example.com", password: "mypassword123") {
    success
    errors
    token
    refreshToken
    user {
      id
      email
      isActive
    }
  }
}
```

### 3. Refresh Token

```graphql
mutation {
  refreshToken(refreshToken: "your_refresh_token_here") {
    success
    errors
    token
    refreshToken
    payload
  }
}
```

### 4. Revoke Token (Logout)

```graphql
mutation {
  revokeToken(refreshToken: "your_refresh_token_here") {
    success
    errors
  }
}
```

### 5. Verify Account

```graphql
mutation {
  verifyAccount(token: "verification_token_from_email") {
    success
    errors
  }
}
```

### 6. Resend Activation Email

```graphql
mutation {
  resendActivationEmail(email: "user@example.com") {
    success
    errors
  }
}
```

### 7. Send Password Reset Email

```graphql
mutation {
  sendPasswordResetEmail(email: "user@example.com") {
    success
    errors
  }
}
```

### 8. Password Reset

```graphql
mutation {
  passwordReset(
    token: "password_reset_token_from_email"
    newPassword1: "newpassword123"
    newPassword2: "newpassword123"
  ) {
    success
    errors
  }
}
```

### 9. Password Change (Authenticated)

```graphql
mutation {
  passwordChange(
    oldPassword: "currentpassword123"
    newPassword1: "newpassword123"
    newPassword2: "newpassword123"
  ) {
    success
    errors
  }
}
```

### 10. Update Account (Authenticated)

```graphql
mutation {
  updateAccount(firstName: "John", lastName: "Doe") {
    success
    errors
  }
}
```

## Query Examples

### Get Current User (Authenticated)

```graphql
query {
  me {
    id
    email
    firstName
    lastName
    isActive
    dateJoined
  }
}
```

### Search Users

```graphql
query {
  users(email_Icontains: "example") {
    edges {
      node {
        id
        email
        isActive
      }
    }
  }
}
```

## Testing Tips

1. **Registration**: Works immediately in development (no email verification required)
2. **Authentication**: Use the `token` from login in the `Authorization` header for subsequent requests: `Bearer <token>`
3. **Token Expiration**: Access tokens expire quickly, use `refreshToken` to get new ones
4. **Errors**: Check the `errors` field in responses for validation messages
5. **Success**: All mutations return a `success` boolean indicating operation status

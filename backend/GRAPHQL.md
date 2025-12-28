# GraphQL Architecture

This project uses a modular GraphQL layout that scales with each Django app.

```
backend/
├─ config/
│  └─ schema.py        # Root Query/Mutation aggregates every app schema + auth
├─ apps/
│  ├─ plan/
│  │  └─ schema/
│  │     ├─ types.py       # DjangoObjectTypes for Plan/Feature/Permission
│  │     ├─ queries.py     # plan-specific query fields
│  │     └─ mutations.py   # plan-specific mutations
│  └─ subscription/
│     └─ schema/
│        ├─ types.py
│        ├─ queries.py
│        └─ mutations.py
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

The project ships with [django-graphql-auth](https://github.com/PedroBern/django-graphql-auth) so you can reuse the standard
registration/login flows in GraphQL:

- `MeQuery` / `UserQuery` are mixed into the root `Query`, giving you `me` and user search helpers.
- `AuthMutation` (see `config/schema.py`) exposes common mutations such as `register`, `tokenAuth`, `refreshToken`,
  `verifyAccount`, `sendPasswordResetEmail`, and more.
- JWT middleware is enabled in `GRAPHENE['MIDDLEWARE']`, and authentication backends are configured in `settings.py`.

Typical client flow:

1. `register` ➜ create user (activation emails are disabled in dev, so account is usable immediately).
2. `tokenAuth` ➜ obtain short-lived JWT for authenticated requests.
3. `refreshToken` / `revokeToken` ➜ manage long-running sessions.

When adding a new app schema, no extra steps are required—just follow the folder convention above and import your query /
mutation classes into `config/schema.py`.

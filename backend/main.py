"""FastAPI main application."""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from app.core.config import settings
from app.core.database import engine, Base, SessionLocal
from app.graphql.schema import schema
from app.routers import health


# Create database tables on startup
Base.metadata.create_all(bind=engine)


async def get_context():
    """Get GraphQL context with database session."""
    db = SessionLocal()
    try:
        return {"db": db}
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    # Startup
    print(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    yield
    # Shutdown
    print("Shutting down application")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_CREDENTIALS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

# Include routers
app.include_router(health.router)

# GraphQL router with context
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to DaisyUI Healthcare API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "graphql": "/graphql",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
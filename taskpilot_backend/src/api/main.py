from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth

app = FastAPI(
    title="TaskPilot Backend",
    description="Backend API for TaskPilot: Tasks, Projects, Users, Analytics, AI, Collab.",
    version="0.1.0",
    openapi_tags=[
        {"name": "Health", "description": "Health and status check endpoints."},
        {"name": "Authentication", "description": "User registration, login, and tokens."},
    ],
)

# Allow CORS for all origins for dev. Restrict in production!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health or welcome endpoint
@app.get("/", tags=["Health"], summary="Health check")
# PUBLIC_INTERFACE
def health_check():
    """Returns status for server health check."""
    return {"message": "Healthy", "status": "ok"}


# Auth endpoints
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

from fastapi import APIRouter, HTTPException, status
from ..schemas.auth import UserLogin, UserRegister, Token
from ..core.security import create_access_token, verify_password, get_password_hash

router = APIRouter()


# PUBLIC_INTERFACE
@router.post("/register", response_model=Token, summary="Register new user")
def register(user_in: UserRegister):
    """Registers a new user and returns an access token."""
    # TODO: Store user in DB and hash password
    # Example stub: In reality, implement user creation and DB
    if user_in.email == "existing@example.com":
        raise HTTPException(status_code=400, detail="Email already registered")
    # Would save user here; skipping
    token = create_access_token({"sub": user_in.email})
    return {"access_token": token, "token_type": "bearer"}


# PUBLIC_INTERFACE
@router.post("/login", response_model=Token, summary="User login and token return")
def login(user_in: UserLogin):
    """Authenticates user and returns JWT access token."""
    # TODO: Validate user from DB
    # Stub logic for demonstration
    correct_email = user_in.email == "test@example.com"
    correct_password = verify_password(user_in.password, get_password_hash("test123"))
    if not (correct_email and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials"
        )
    token = create_access_token({"sub": user_in.email})
    return {"access_token": token, "token_type": "bearer"}

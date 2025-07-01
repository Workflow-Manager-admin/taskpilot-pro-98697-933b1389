from pydantic import BaseModel, EmailStr, Field


# PUBLIC_INTERFACE
class UserRegister(BaseModel):
    email: EmailStr = Field(..., description="User's email")
    password: str = Field(..., min_length=6, description="User's password")


# PUBLIC_INTERFACE
class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="User's email")
    password: str = Field(..., min_length=6, description="User's password")


# PUBLIC_INTERFACE
class Token(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(..., description="Token type (bearer)")

from pydantic import BaseModel

class PostUserRequest(BaseModel):
    username: str
    email: str
    designation: str | None = None
    organization: str | None = None
from pydantic import BaseModel

class PostUserRequest(BaseModel):
    username: str
    email: str
    designation: str | None
    organization: str | None
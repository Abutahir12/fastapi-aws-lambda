from pydantic import BaseModel
from typing import Union

class PostUserRequest(BaseModel):
    username: str
    email: str
    designation: Union[str, None]  = None
    organization:  Union[str, None]  = None
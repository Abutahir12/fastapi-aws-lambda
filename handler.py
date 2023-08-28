import json
import os
from fastapi import FastAPI
from mangum import Mangum
from request_models.models import PostUserRequest

app = FastAPI()
handler = Mangum(app)


@app.post("/user")
def create_user(request: PostUserRequest):
    return {"statusCode": 200, "message": "User created successfully", "item": request }

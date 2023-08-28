import json
import os
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


@app.get("/")
def hello_world():
    return {"statusCode": 200, "body": json.dumps("Success")}

import json
import os
from fastapi import FastAPI

app = FastAPI()

def hello(event, context):
    print(os.environ["AWS_ACCESS_KEY_ID"])
    print(os.environ["AWS_SECRET_ACCESS_KEY"])

    return {"statusCode": 200, "body": json.dumps("Success")}

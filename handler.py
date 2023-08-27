import json
import os

def hello(event, context):
    print(os.environ("AWS_ACCESS_KEY_ID"))
    print(os.environ("AWS_SECRET_ACCESS_KEY"))

    return {"statusCode": 200, "body": json.dumps("Success")}

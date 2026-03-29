import os

AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

def connect():
    if not AWS_SECRET_KEY:
        raise ValueError("AWS_SECRET_KEY not found in environment variables")
    print("Connecting to AWS...")

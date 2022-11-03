from fastapi import FastAPI

api = FastAPI()

@api.get("/hello")
def hello():
    return "Hello"

@api.get("/status")
def status():
    return 1

@api.get("/dict")
def dic():
    return {"data":"hello"}

@api.get("/")
def test():
    return {}
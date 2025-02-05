from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# path parameters
@app.get("/greet/{name}")
async def greet(name: str):
    return {"message":f"Hello {name}"}

# query parameters
@app.get("/greetings")
async def greeting(name:str = "Guest"):
    return {"message":f"Hello {name}"}

@app.get("/profile")
async def profile(name:str , age: int):
    return {"name":name , "age":age}





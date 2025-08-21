from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

# Create FastAPI app
app = FastAPI()

# Input model for /greet
class GreetRequest(BaseModel):
    name: str

# POST /greet endpoint
@app.post("/greet")
def greet(request: GreetRequest):
    return {"message": f"Hello, {request.name}!"}

# GET /time endpoint
@app.get("/time")
def get_time():
    return {"server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

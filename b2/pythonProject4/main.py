from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow all origins for testing purposes
origins = [
    "http://127.0.0.1:5500",  # Replace with the port number used by Live Server
    "http://localhost:5500",  # Live Server default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OperationInput(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(inputs: OperationInput):
    return {"result": inputs.a + inputs.b}

@app.post("/subtract")
def subtract(inputs: OperationInput):
    return {"result": inputs.a - inputs.b}

@app.post("/multiply")
def multiply(inputs: OperationInput):
    return {"result": inputs.a * inputs.b}

@app.post("/divide")
def divide(inputs: OperationInput):
    if inputs.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return {"result": inputs.a / inputs.b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
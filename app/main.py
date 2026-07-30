from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Calculator API")

class CalculateRequest(BaseModel):
    operation: str
    a: float
    b: float

@app.get("/")
def read_root():
    return {"message": "Welcome to Calculator API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.post("/calculate")
def calculate(req: CalculateRequest):
    if req.operation == "add":
        return {"result": req.a + req.b}
    elif req.operation == "subtract":
        return {"result": req.a - req.b}
    elif req.operation == "multiply":
        return {"result": req.a * req.b}
    elif req.operation == "divide":
        if req.b == 0:
            return {"error": "division by zero"}
        return {"result": req.a / req.b}
    else:
        return {"error": "unsupported operation"}

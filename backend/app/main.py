from fastapi import FastAPI
from app.routes import funds

app = FastAPI(title="Public Funds Transparency MVP")

# Include routers
app.include_router(funds.router, prefix="/funds")

@app.get("/")
def root():
    return {"message": "Public Funds Transparency MVP Running"}

from fastapi import FastAPI
from .routes import router as tasks_router

app = FastAPI(title="Professional To-Do API")

app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "Welcome to To-Do API. Go to /docs for Swagger UI."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
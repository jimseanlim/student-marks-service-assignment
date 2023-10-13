from app.api.router import api_router

from fastapi import FastAPI
app = FastAPI()
app.include_router(router=api_router, prefix="/v1")



@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Marks API"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
import uvicorn
from fastapi import FastAPI
from routers import address_router


app = FastAPI()


app.include_router(address_router.router, prefix="/api")


@app.get("/")
def root():
    return {"greetings...."}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
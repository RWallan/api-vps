from fastapi import FastAPI

from api_vps.routers import books_router

app = FastAPI(title="API c/ VPS", description="API com deploy em uma VPS")


@app.get("/")
def health_check():
    return {"message": "OK"}


app.include_router(books_router)

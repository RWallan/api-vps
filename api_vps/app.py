from fastapi import FastAPI

app = FastAPI(title="API c/ VPS", description="API com deploy em uma VPS")


@app.get("/")
def health_check():
    return {"message": "OK"}

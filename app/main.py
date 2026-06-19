from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Golf Caddie is up and running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
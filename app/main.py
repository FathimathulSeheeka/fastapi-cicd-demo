from fastapi import FastAPI

app = FastAPI(
    title="CI/CD Demo API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Hello from CI/CD"}


@app.get("/health")
def health():
    return {"status": "healthy"}
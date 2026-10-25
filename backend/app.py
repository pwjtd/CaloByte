from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://wlabedz.github.io", 
        "http://localhost:4200",  
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "/hello"}


@app.get("/hello")
def hello():
    return {"message": "Hello World!"}


@app.get("/health")
def health():
    return {"status": "ok"}

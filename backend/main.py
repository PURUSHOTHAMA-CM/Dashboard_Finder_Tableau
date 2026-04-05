from fastapi import FastAPI
from query_engine import search_dashboards
from script import load_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    try:
        load_data()
        print("Startup complete")
    except Exception as e:
        print("Startup failed:", e)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/search")
def search(query: str):
    return  search_dashboards(query)

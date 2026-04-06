from fastapi import FastAPI
from query_engine import search_dashboard
from script import load_data
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Pre-loading data...")
        load_data()
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Loading failed: {e}")
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dashboardfindercb.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/search")
def search(query: str):
    return  search_dashboard(query)

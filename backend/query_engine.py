from fastapi import FastAPI
from vector_db import collection, get_model
from fastapi.middleware.cors import CORSMiddleware
from script import load_data


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
    load_data()

@app.get("/")
def home():
    return {"message":"API is running"}

@app.get("/search")
def search_dashboard(query: str):

    model = get_model()

    query_embedding = model.encode(query).tolist()

    print("Count:", collection.count())

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    print(results)
    best = results["metadatas"][0][0]

    return {
        "name": best["name"],
        "url": best["url"]
    }

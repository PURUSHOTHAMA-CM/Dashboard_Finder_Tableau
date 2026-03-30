from fastapi import FastAPI
from vector_db import collection, model
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
def home():
    return {"message":"API is running"}

@app.get("/search")
def search_dashboard(query: str):
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
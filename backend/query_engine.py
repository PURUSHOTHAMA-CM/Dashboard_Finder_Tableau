from vector_db import collection, get_model


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

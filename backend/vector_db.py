import chromadb
from sentence_transformers import SentenceTransformer
import os

# Load model once
model = None

def get_model():
    global model
    if model is None:
        from sentence_transformers import SentenceTransformer
        print("📦 Loading model...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

# Persistent DB (important)
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="dashboards")
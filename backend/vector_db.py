import chromadb
from sentence_transformers import SentenceTransformer
import os

os.environ["HF_HOME"]="/tmp"

# Load model once
model = None

def get_model():
    global model
    if model is None:
        print("📦 Loading model...")
        model = SentenceTransformer('all-MiniLM-L6-v2',cache_folder="/tmp")
    return model

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DB_PATH=os.path.join(BASE_DIR,"chroma_db")

# Persistent DB (important)
client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(name="dashboards")

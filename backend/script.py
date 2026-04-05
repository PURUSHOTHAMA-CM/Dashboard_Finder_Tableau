from vector_db import collection,get_model
# maintaining common db for both the query engine and script
import json
import os

def load_data():
    print("Starting the script")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "dashboard_data.json")
    with open("dashboard_data.json") as f:
        dashboards=json.load(f)

    print("Loaded dashboards")
    model=get_model()

    for dash in dashboards:

    # print("Processing Dashboards");
        embedding=model.encode(dash["description"]).tolist()

        collection.add(
            ids=[dash["id"]],
            documents=[dash["description"]],
            embeddings=[embedding],
            metadatas=[{"name":dash["name"],"url": dash["URL"]}]
        )

    print("Loaded the data")
# print("Count:", collection.count())


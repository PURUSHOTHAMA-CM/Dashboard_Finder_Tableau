from vector_db import collection,model
# maintaining common db for both the query engine and script
import json

print("Starting the script")

with open("dashboard_data.json") as f:
    dashboards=json.load(f)

print("Loaded dashboards")

for dash in dashboards:

    print("Processing Dashboards");
    embedding=model.encode(dash["description"]).tolist()

    collection.add(
        ids=[dash["id"]],
        documents=[dash["description"]],
        embeddings=[embedding],
        metadatas=[{"name":dash["name"],"url": dash["URL"]}]
    )

print("Inserted")
print("Count:", collection.count())

import lancedb
from lancedb.pydantic import LanceModel, Vector

# Assume `generate_embeddings` is your function to generate embeddings
def generate_embeddings(text):
    # Your model's embedding generation logic
    pass

class MyDataModel(LanceModel):
    text: str
    vector: Vector(128)  # Assuming your embeddings are 128-dimensional

# Connect to LanceDB
db = lancedb.connect("/path/to/your/database")

# Create a table
table = db.create_table("my_data", schema=MyDataModel)

# Add data
data = ["Sample text 1", "Sample text 2"]
embeddings = [generate_embeddings(text) for text in data]
table.add([{"text": text, "vector": embedding} for text, embedding in zip(data, embeddings)])

# Query the table
results = table.search("query text").limit(1).to_pydantic(MyDataModel)
for result in results:
    print(result.text)


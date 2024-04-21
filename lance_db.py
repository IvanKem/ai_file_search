import lancedb
import pyarrow as pa
from lancedb.pydantic import Vector, LanceModel
from pandas import DataFrame
from vectorizer import generate_embeddings


class Content(LanceModel):
    file_id: int
    vector: Vector(768)
    title: str
    pwd: str
    context: str



def create_db(table_name):
    uri = "data/"
    db = lancedb.connect(uri)
    db.create_table(table_name, schema=Content)


def add_to_table(docs, table_name):
    uri = "data/"
    db = lancedb.connect(uri)
    table = db.open_table(table_name)
    table.add(docs)


def search_in_table(str, table_name, k):
    uri = "data/"
    db = lancedb.connect(uri)
    table = db.open_table(table_name)
    vector = generate_embeddings(str)
    results = table.search(vector).limit(k).to_pydantic(Content)
    return results

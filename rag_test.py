from tqdm.notebook import tqdm
import torch
from vectorizer import generate_embeddings
import os
import pandas as pd
from typing import Optional, List, Tuple
import datasets
import matplotlib.pyplot as plt
from langchain.docstore.document import Document as LangchainDocument
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.utils import DistanceStrategy
from lance_db import *

pd.set_option("display.max_colwidth", None)  # this will be helpful when visualizing retriever outputs
folder_path = "test_files"

# Получаем список файлов в папке
file_list = os.listdir(folder_path)

# Создаем объекты doc из файлов
doc = []
id = 0

for file_name in file_list:
    id += 1
    if file_name.endswith(".txt"):  # Убеждаемся, что это текстовый файл
        source = file_name  # Имя файла без расширения ".txt"
        with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as file:
            text = file.read()
        doc.append({"text": text, "id": id, "source": source, "pwd": f"test_files/{file_name}"})

# Создаем объекты LangchainDocument из объектов doc
RAW_KNOWLEDGE_BASE = [
    LangchainDocument(page_content=doc["text"], metadata={"id": id, "source": doc["source"], "pwd": doc["pwd"]}) for doc in
    tqdm(doc)
]

MARKDOWN_SEPARATORS = [
    "\n#{1,6} ",
    "```\n",
    "\n\\*\\*\\*+\n",
    "\n---+\n",
    "\n___+\n",
    "\n\n",
    "\n",
    " ",
    "",
]

EMBEDDING_MODEL_NAME = "multilingual-e5-base"


def split_documents(chunk_size: int,
                    knowledge_base: List[LangchainDocument],
                    tokenizer_name: Optional[str] = EMBEDDING_MODEL_NAME,
                    ) -> List[LangchainDocument]:
    """
    Split documents into chunks of maximum size `chunk_size` tokens and return a list of documents.
    """
    text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        AutoTokenizer.from_pretrained(tokenizer_name, trust_remote_code=True, revision='v1.0.0'),
        chunk_size=chunk_size,
        chunk_overlap=int(chunk_size / 10),
        add_start_index=True,
        strip_whitespace=True,
        separators=MARKDOWN_SEPARATORS,
    )

    docs_processed = []
    for doc in knowledge_base:
        docs_processed += text_splitter.split_documents([doc])

    # Remove duplicates
    unique_texts = {}
    docs_processed_unique = []
    for doc in docs_processed:
        if doc.page_content not in unique_texts:
            unique_texts[doc.page_content] = True
            docs_processed_unique.append(doc)

    return docs_processed_unique


docs_processed = split_documents(
    512,  # We choose a chunk size adapted to our model
    RAW_KNOWLEDGE_BASE,
    tokenizer_name=EMBEDDING_MODEL_NAME,
)

'''Tokinezed documents'''
# print(docs_processed[49].metadata)
# for i in range(len(docs_processed)):
# print(docs_processed[i].metadata)
#page_content_list = [doc.page_content for doc in docs_processed]

#embeddings = generate_embeddings(page_content_list)
# print(len(embeddings))
#print(docs_processed[0].metadata["pwd"], embeddings[0])


def concatinate_with_embeddings(docs):
    page_content_list = [doc.page_content for doc in docs]
    embeddings = generate_embeddings(page_content_list)
    add_docs = []
    for doc, embedding in zip(docs, embeddings):
        add_docs.append({
            "file_id": doc.metadata["id"],
            "vector": embedding,
            "title": doc.metadata["source"],
            "pwd": doc.metadata["pwd"],
            "context": doc.page_content
        })
    return add_docs


table_name="files"
new_docs = concatinate_with_embeddings(docs_processed)
add_to_table(new_docs, table_name)
print(search_in_table("How to create a pipeline object?", table_name, 3))


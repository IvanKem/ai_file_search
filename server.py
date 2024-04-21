#FASTAPI SERVER LOGIC
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

table_name="files"
print(search_in_table("How to create a pipeline object?", table_name,1))

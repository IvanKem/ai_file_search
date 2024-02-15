import os

from sentence_transformers import SentenceTransformer, util

multi_lang_model="distiluse-base-multilingual-cased-v1"
high_score_model = "multi-qa-distilbert-cos-v1"
model = SentenceTransformer(high_score_model)

query=list(str(input()))
folder_path = "test_files/"  # Replace with the actual folder path

file_names = os.listdir(folder_path)
file_names_array = []

for file_name in file_names:
    file_names_array.append(file_name)


#Our sentences we like to encode
sentences=file_names_array

#Sentences are encoded by calling model.encode()

def vectorize(sentences:list):
    return model.encode(sentences)

sentences_embeddings = vectorize(sentences)
query_embedding = vectorize(query)

#Print the embeddings
#for sentence, embedding in zip(sentences, embeddings):
    #print("Sentence:", sentence)
    #print("Embedding:", embedding)
    #print("")


hits = util.semantic_search(query_embedding, sentences_embeddings, top_k=5)
hits = hits[0]      #Get the hits for the first query
for hit in hits:
    print(sentences[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))


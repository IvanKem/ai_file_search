import os
from sentence_transformers import CrossEncoder
folder_path = "test_files/"  # Replace with the actual folder path

Query= str(input())

file_names = os.listdir(folder_path)
file_names_array = []

for file_name in file_names:
    file_names_array.append(file_name)


def get_pairs(arr,query:str):

    pairs = []
    for i in range(len(arr)):
        pairs.append((query, arr[i]))
    return pairs


pairs=get_pairs(file_names_array, Query)


model = CrossEncoder('cross-encoder/stsb-TinyBERT-L-4', max_length=512)
scores = model.predict(pairs)
for i in range(len(scores)):
    print(pairs[i]," :",scores[i])

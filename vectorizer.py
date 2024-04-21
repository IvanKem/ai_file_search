from sentence_transformers import SentenceTransformer

sentences = [
    "A man is eating food.",
    "A man is eating a piece of bread.",
    "The girl is carrying a baby.",
    "A man is riding a horse.",
    "A woman is playing violin.",
    "Two men pushed carts through the woods.",
    "A man is riding a white horse on an enclosed ground.",
    "A monkey is playing drums.",
    "A cheetah is running behind its prey.",
]
def generate_embeddings(texts):
    model = SentenceTransformer('multilingual-e5-base')
    embeddings = model.encode(texts, normalize_embeddings=True ,device='cpu',)
    return embeddings

# Print the embeddings
#print(len(generate_embeddings(sentences)))

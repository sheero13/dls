# import pandas as pd

# data = pd.read_csv("dataset.csv")   # or json
# passages = data["passage"].tolist()
# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("all-MiniLM-L6-v2")
# embeddings = model.encode(passages)

# import faiss
# import numpy as np

# dimension = embeddings.shape[1]

# index = faiss.IndexFlatL2(dimension)
# index.add(np.array(embeddings))

# import pickle

# faiss.write_index(index, "faiss_index.index")
# pickle.dump(data, open("passages.pkl", "wb"))

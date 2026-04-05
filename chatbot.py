#my_ver
# import faiss
# import pickle
# import numpy as np
# from sentence_transformers import SentenceTransformer


# embed_model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

# index = faiss.read_index("faiss_index.index")

# with open("passages.pkl", "rb") as f:
#     data = pickle.load(f)

# if hasattr(data, "iloc"):
#     passages = data["passage"].tolist()
# else:
#     passages = data


# def get_answer(query, top_k=3):
    
#     query_vec = embed_model.encode([query], normalize_embeddings=True)
#     query_vec = np.array(query_vec).astype("float32")

    
#     D, I = index.search(query_vec, top_k)

#     for i in I[0]:
#         if 0 <= i < len(passages):
#             return passages[i]

#     return "No relevant answer found."


# if __name__ == "__main__":
#     print("Chatbot Ready (Lightweight Mode). Type 'exit' to quit.\n")

#     while True:
#         query = input("Ask: ")

#         if query.lower() == "exit":
#             break

#         print("Answer:", get_answer(query))


#----------------------------------------------------------------------------------------------------------
#suse_ver
# import faiss
# import pickle
# from sentence_transformers import SentenceTransformer, CrossEncoder
# from transformers import pipeline

# embed_model = SentenceTransformer("all-MiniLM-L6-v2")
# reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# qa_pipeline = pipeline(
#     "question-answering",
#     model="deepset/roberta-base-squad2"   
# )

# index = faiss.read_index("faiss_index.index")
# data = pickle.load(open("passages.pkl", "rb"))


# def get_answer(query, top_k=5):
  
#     query_vec = embed_model.encode([query])

#     D, I = index.search(query_vec, top_k)
#     contexts = [data.iloc[i]["passage"] for i in I[0] if 0 <= i < len(data)]

#     if not contexts:
#         return "No relevant context found."

    
#     pairs = [[query, c] for c in contexts]
#     scores = reranker.predict(pairs)

#     ranked = sorted(zip(scores, contexts), reverse=True)
#     contexts = [c for _, c in ranked]

#     combined_context = " ".join(contexts[:3])[:1000]

    
#     result = qa_pipeline({
#         "question": query,
#         "context": combined_context
#     })

#     answer = result.get("answer", "").strip()
#     score = float(result.get("score", 0.0))

#     if score > 0.4 and len(answer) > 3:
#         return answer

   
#     return contexts[0]

#--------------------------------------------------------------------------------------------------

# pip install sentence-transformers==2.6.1
# pip install transformers==4.37.2
# pip install tokenizers==0.15.2
# pip install faiss-cpu
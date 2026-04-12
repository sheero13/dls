# TRAIN - FINAL FIXED VERSION

# import numpy as np
# import pickle
# import json
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, LSTM, Dense
# from tensorflow.keras.utils import to_categorical

# print("Reading data...")

# with open(r"doc.txt", "r", encoding="utf-8") as f:
#     text = f.read().lower()

# chars = sorted(list(set(text)))
# char_to_index = {c: i for i, c in enumerate(chars)}
# index_to_char = {i: c for i, c in enumerate(chars)}

# vocab_size = len(chars)


# seq_length = 10   

# X = []
# y = []

# for i in range(seq_length, len(text)):
#     seq = text[i-seq_length:i]
#     label = text[i]

#     X.append([char_to_index[c] for c in seq])
#     y.append(char_to_index[label])

# X = np.array(X)
# y = to_categorical(y, num_classes=vocab_size)

# model = Sequential([
#     Embedding(vocab_size, 32, input_length=seq_length),
#     LSTM(64),
#     Dense(vocab_size, activation="softmax")
# ])

# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# print("Training...")
# model.fit(X, y, epochs=100, batch_size=32, verbose=1)


# model.save("char_model.h5")

# with open("char_map.pkl", "wb") as f:
#     pickle.dump((char_to_index, index_to_char), f)

# with open("config.json", "w") as f:
#     json.dump({"seq_length": seq_length}, f)

# print("Model saved!")

#----------------------------------------------------------------------------------
# import numpy as np
# import pickle
# import json
# from tensorflow.keras.models import load_model

# model = load_model("char_model.h5")

# with open("char_map.pkl", "rb") as f:
#     char_to_index, index_to_char = pickle.load(f)

# with open("config.json", "r") as f:
#     config = json.load(f)

# seq_length = config["seq_length"]

# print("Model loaded!\n")

# def predict_next_char(seed_text):
#     seed_text = seed_text.lower()

#     if len(seed_text) < seq_length:
#         seed_text = " " * (seq_length - len(seed_text)) + seed_text
#     else:
#         seed_text = seed_text[-seq_length:]

#     encoded = [char_to_index.get(c, 0) for c in seed_text]
#     encoded = np.array(encoded).reshape(1, seq_length)

#     pred = model.predict(encoded, verbose=0)[0]

   
#     top_k = 3
#     top_indices = pred.argsort()[-top_k:]
#     next_index = np.random.choice(top_indices, p=pred[top_indices]/np.sum(pred[top_indices]))

#     return index_to_char[next_index]

# while True:
#     seed = input("Enter text: ")

#     if seed == "exit":
#         break

#     print("Next character:", predict_next_char(seed))
#     print("-" * 40)

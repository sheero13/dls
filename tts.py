# import os
# from gtts import gTTS

# if not os.path.exists("audio"):
#     os.makedirs("audio")

# word_list = [
#     "welcome", "please", "select", "enter", "ticket",
#     "payment", "successful", "cancel", "exit",
#     "thank you", "number", "confirm", "back",
#     "next", "invalid", "try again", "the"
# ]

# print("Generating word audio files...")
# for word in word_list:
#     filename = word.replace(" ", "_")   
#     filepath = f"audio/{filename}.mp3"

#     if not os.path.exists(filepath):  
#         tts = gTTS(text=word, lang="en")
#         tts.save(filepath)
#         print(f"Created: {filepath}")

# print("All word audio files ready!\n")

# sentence = "welcome please select the ticket"
# words = sentence.lower().split()

# print("Input words:", words)

# output_file = "output.mp3"

# with open(output_file, "wb") as outfile:
#     for word in words:
#         filename = word.replace(" ", "_")
#         filepath = f"audio/{filename}.mp3"

#         if os.path.exists(filepath):
#             with open(filepath, "rb") as infile:
#                 outfile.write(infile.read())
#         else:
#             print(f"Warning: '{word}' audio not found!")

# print("\nFinal audio generated:", output_file)


# try:
#     from IPython.display import Audio
#     display(Audio(output_file))
# except:
#     print("Playback not supported here. Open output.mp3 manually.")
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

# sentence = "please select confirm"
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

#----------------------------------------------------------------------------------------------------------

# import os
# import random
# import numpy as np
# from IPython.display import Audio, display
# from pydub import AudioSegment

# DATA_PATH = r"free-spoken-digit-dataset\recordings"   


# def get_audio_for_digit(digit):
#     digit = str(digit)
    
#     files = [f for f in os.listdir(DATA_PATH) if f.startswith(digit + "_")]
    
#     if not files:
#         raise ValueError(f"No audio found for digit {digit}")
    
#     chosen_file = random.choice(files)
#     return os.path.join(DATA_PATH, chosen_file)


# def generate_tts_audio(number_string):
#     combined = AudioSegment.empty()
    
#     for digit in number_string:
#         file_path = get_audio_for_digit(digit)
#         sound = AudioSegment.from_wav(file_path)
        
#         combined += sound + AudioSegment.silent(duration=200)  
    
#     return combined


# print("\n--- DIGIT TTS USING DATASET ---\n")

# num = input("Enter a number (e.g., 36789): ")

# if not num.isdigit():
#     print("Please enter only digits!")
# else:
#     tts_audio = generate_tts_audio(num)
    
#     output_file = "output_tts.wav"
#     tts_audio.export(output_file, format="wav")
    
#     print("Playing generated audio...")
    
#     display(Audio(output_file))

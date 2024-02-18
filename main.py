import pyttsx3
import os

# Create a folder
folder_name = "sounds"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

text_list = ["Apple",'Ball',"Cat","Duck","Egg","Fish","Grasshopper","Horse","Ice Cream","Jacket","Key","Lemon","Map","Necklace","Oil","Peach","Queen","Robot","Star","Tank","Umbrella","Vegetable","Whale","Xylophone","Yatch","Zipper",
             "1","2","3","4","5","6","7","8","9","0"]


# Initialize the engine
engine = pyttsx3.init()

# Get all available voices
voices = engine.getProperty('voices')

# Set voice gender preference (0 for male, 1 for female - index might vary based on available voices)
voice_id = 1  # Assuming 1 corresponds to a female voice

# Set the preferred voice
engine.setProperty('voice', voices[voice_id].id)
engine.setProperty('rate', 140) 
# Convert text to speech and save to file


for text in text_list:
    file_name = f"{folder_name}/{text}.mp3"
    engine.save_to_file(text, file_name.lower())
    
engine.runAndWait()

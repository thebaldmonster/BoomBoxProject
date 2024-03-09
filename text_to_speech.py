from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")
    os.remove("temp.mp3")

# voice_interaction.py
import speech_recognition as sr
from gtts import gTTS
import pygame
import tempfile

def initialize_audio():
    pygame.mixer.init()

def speak(text):
    with tempfile.NamedTemporaryFile(delete=True, suffix='.mp3') as fp:
        tts = gTTS(text=text, lang='en')
        tts.save(fp.name)
        pygame.mixer.music.load(fp.name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "I didn't catch that."
        except sr.RequestError:
            return "Service is unavailable."

initialize_audio()

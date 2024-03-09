#   Dictado por voz

import speech_recognition as sr
import pyaudio

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = recognizer.listen(source)

    text=recognizer.recognize_google(audio, language = 'ES')

    print(f"Has dicho: {text}")
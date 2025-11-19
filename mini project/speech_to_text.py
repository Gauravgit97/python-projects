import pyttsx3
import speech_recognition as sr
import pyaudio


def get_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        audio = r.listen(source)
        print('Done!..')
    
    try:
        text = r.recognize_google(audio)
        print(text)
    except Exception as e:
        print(e)


get_text()
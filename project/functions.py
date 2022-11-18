import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests
import webbrowser

datetime = datetime.now()

def say(audio):

        # pyttsx3
        # text to speech
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

def greet():

    # Simple greet function
    say("Hello I am space, your Virtual Assistant. How can I help you?")

def listen():
    try:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something...\n")
            r.pause_threshold = 1
            r.energy_threshold = 1000
            audio = r.listen(source, timeout=30, phrase_time_limit=60)
            print("Listening...")
            print("Recognizing...\n")
            words = r.recognize_google(audio)
            print(f"User said: {words}")
    except sr.UnknownValueError:
                print("Oops! Didn't catch that\n")
                say("Oops! Didn't catch that")
                return "None"
    return words

def date():
    day = datetime.strftime("%A")
    date = datetime.strftime("%d")
    month = datetime.strftime("%B")
    year = datetime.strftime("%Y")
    x = f"Today it's {day}, {month} {date} {year}" 
    print(x)
    say(x)

def time():
    hour = datetime.strftime("%I")
    minute = datetime.strftime("%M")
    ampm = datetime.strftime("%p")
    print(f"The time is {hour}:{minute} {ampm}")
    say(f"The time is {hour} {minute} {ampm}")

def get_random_advice():
    advice = requests.get("https://api.adviceslip.com/advice").json()
    advice = advice["slip"]["advice"]
    print(advice) 
    say(advice)

def google_search(phrase):
    webbrowser.open(f"https://www.google.com/search?q={phrase}")
    exit()
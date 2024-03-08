import speech_recognition as sr
import pyttsx3
import datetime

# Initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices') # Get available voices

# Speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listener
recognizer = sr.Recognizer()

def listen():    
    with sr.Microphone() as source:
        print("Listening . . . .")
        audio = recognizer.listen(source)
    try:
        input = recognizer.recognize_google(audio)
        print(f"I heard: \n{input}")
        return input.lower()
    except:
        speak("I didn't quite get that!")
        return None
    
while True:
    human = listen()
    if human:
        if "alvin" in human:
            speak("Hi there! How can I help you?")

        else:
            speak("Sorry Im not yet that advanced!")
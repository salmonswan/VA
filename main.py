import speech_recognition as sr
import pyttsx3
import datetime


class Assistant:
  def __init__(self):
    self.engine = pyttsx3.init()
    self.voices = self.engine.getProperty('voices')
    self.engine.setProperty('voice', self.voices[24].id)
    self.recognizer = sr.Recognizer()

  def speak(self, text):
    self.engine.say(text)
    self.engine.runAndWait()

  def listen(self):
    with sr.Microphone() as source:
      print("Listening...")
      audio = self.recognizer.listen(source)
    try:
      text = self.recognizer.recognize_google(audio)
      print(f"I heard: \n{text}")
      return text.lower()
    except sr.UnknownValueError:
      print("Sorry, could not understand audio")
      return None
    except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))
      return None

  def run(self):
    while True:
      user_text = self.listen()
      if user_text:
        if "alvin" in user_text:
          self.speak("Hi there! How can I help you?")
        else:
          self.speak("Sorry, I'm not yet that advanced!")


if __name__ == "__main__":
  # Create an instance of the Assistant class
  alvin = Assistant()
  # Call the run method to start the assistant
  alvin.run()
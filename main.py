import pyttsx3  # For text-to-speech conversion.
import speech_recognition as sr # For recognizing speech 
import datetime
import wikipedia # For fetching data from Wikipedia
import webbrowser # For opening web pages in a browser
import os # For interacting with the operating system


# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 150)


#creat a speak function
def speak(text):
    '''
    This function take a text
    and returns voice

    Args:
        text(_type_) : string
    '''
    engine.say(text)
    engine.runAndWait()

#speech recognition function
def takeCommand():
    """this function will recognize voice and return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining...")
        r.pause_threshold
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en')
            print(f"User said: {query}\n")


        except Exception as e:
            print("say that agin please...")
            return "None"
        return query
        

text = takeCommand()
speak(text)



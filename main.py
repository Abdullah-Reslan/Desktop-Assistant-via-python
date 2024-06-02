import pyttsx3  # For text-to-speech conversion.
import speech_recognition as sr # For recognizing speech 
import datetime
import wikipedia # For fetching data from Wikipedia
import webbrowser # For opening web pages in a browser
import os # For interacting with the operating system

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# List available voices
# for idx, voice in enumerate(voices):
#     print(f"Voice {idx}: {voice.name}")

# Select the desired voice by index (change the index to select a different voice)
# For example, voices[0] is typically a male voice, and voices[1] is typically a female voice.
selected_voice = 1  # Change this index to select a different voice

engine.setProperty('voice', voices[selected_voice].id)
engine.setProperty('rate', 150)

# Create a speak function
def speak(text):
    '''
    This function takes a text
    and returns voice

    Args:
        text (_type_): string
    '''
    engine.say(text)
    engine.runAndWait()

# Speech recognition function
def takeCommand():
    """This function will recognize voice and return text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again, please...")
            return "None"
        return query

# Function to wish the user based on time
def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning sir, how are you doing today")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir, how are you doing today")
    else:
        speak("Good evening sir, how are you doing today")

    speak("I am JARVIS. Tell me sir, how may I help you")

if __name__ == "__main__":
    wish_me()

    while True: # this line to make it listen and answer always 
    
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif "youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif "google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif "github" in query:
            speak("Opening GitHub")
            webbrowser.open("github.com")
        
        elif "time" in query:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {startTime}")

        elif "stop" in query:
            speak("i was happy to be able to help you ")
            exit()
        

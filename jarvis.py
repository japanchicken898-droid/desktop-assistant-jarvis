import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import sys

# Initialize the Text-To-Speech (TTS) Engine
engine = pyttsx3.init('sapi5') if os.name == 'nt' else pyttsx3.init()
voices = engine.getProperty('voices')
# Index 0 is usually a male voice (Jarvis style), Index 1 is female
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 180) # Speed of speech

def speak(audio):
    """Makes the assistant speak out loud"""
    print(f"JARVIS: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Greets the user based on the current time of day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am JARVIS. How can I help you today, sir?")

def take_command():
    """Listens to the microphone and converts speech to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1 # Seconds of non-speaking audio before phrase is complete
        r.adjust_for_ambient_noise(source, duration=0.5) # Calibrate for background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query.lower()

if __name__ == "__main__":
    wish_me()
    
    while True:
        query = take_command()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception:
                speak("I couldn't find any specific match on Wikipedia.")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")

        elif 'open notepad' in query:
            speak("Opening Notepad")
            if os.name == 'nt': # For Windows
                os.system("notepad.exe")
            else:
                speak("Notepad app isn't natively mapped for this OS framework.")

        elif 'offline' in query or 'quit' in query or 'goodbye' in query:
            speak("Going offline. Goodbye, sir!")
            sys.exit()

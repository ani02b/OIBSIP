import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import webbrowser

#initialize recognizer
recognizer = sr.Recognizer()

#convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')

def greet():
    responses = ["Hello, how can I assist you?", "Hi there, how may I help you?", "Hey, what can I do for you?"]
    speak(responses[0])

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"Today's date is {current_date}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()

        print("User said:", command)

        if "hello" in command:
            greet()
        elif "time" in command:
            get_time()
        elif "date" in command:
            get_date()
        elif "search" in command:
            query = command.replace("search", "")
            search_web(query)
        elif "exit" in command:
            speak("Goodbye! See you soon")
            break
        else:
            speak("I'm sorry, I didn't understand that. Please try again.")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")

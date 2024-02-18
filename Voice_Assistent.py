import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    
    time2 = int(datetime.datetime.now().hour)
    if 0 <= time2 < 12:
        speak("Good Morning!")
    elif 12 <= time2 < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant Savvy. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening to what you're saying...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(f"Caught an exception: {e}")
        print("Would you mind repeating that?")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'what' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)    
        elif 'when' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)  
        elif 'greet' in query:
            speak('HELLO SIR , HELLO MAAM  , I AM SAVVY ,  AN AI VIRTUAL ASSISTENT  ,  HOW ARE YOU TODAY ,  HOPE YOU ARE HAVING A NICE DAY' )              
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("OPENING. ENJOY YOUR FAVOURITE VIDEOS")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("OPENING. EXPLORE AND SEARCH FOR ANYTHING.")
        elif 'amazon' in query:
            webbrowser.open("amazon.in")
            speak("OPENING. SHOP FOR ANYTHING you like ")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M %p")
            print(f"The current time is {strTime}")
            speak(f"The current time is {strTime}")  
        elif 'day' in query:
            current_day = datetime.datetime.now().strftime("%A")
            print(f"Today is {current_day}")
            speak(f"Today is {current_day}") 
        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f"Today's date is {current_date}")
            speak(f"Today's date is {current_date}")        
        elif 'thank' in query:
            speak("My pleasure human Is there anything else  you want me to do ?")
        elif 'favourite video' in query:
            speak("PLAYING NOW")
            webbrowser.open("https://www.youtube.com/watch?v=UBBHpoW3AKA")
        elif 'bye' in query:
            speak("Bye Human. See you soon")
            quit()
        elif 'playlist' in query:
            speak("OPENING YOUR PLAYLIST")
            webbrowser.open("https://www.youtube.com/watch?v=_z8UyrLlM7k")

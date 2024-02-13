import pyttsx3
import pywhatkit
from datetime import timedelta, datetime
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(text)
    engine.runAndWait()

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en")
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def sendMessage():
    speak("Who do you want to message? Please say the number.")
    person = speechrecognition()
    speak("What's the message?")
    message = speechrecognition()
    strTime = int(datetime.now().strftime("%H"))
    update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))
    if person and message:
        pywhatkit.sendwhatmsg("+91" + person, message, time_hour=strTime, time_min=update)

import pyttsx3
import speech_recognition as sr
import requests
import json
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
        try:
            audio = r.listen(source, timeout=8)
        except sr.WaitTimeoutError:
            print("Timeout occurred while listening.")
            return ""
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en")
        return query.lower()
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
        return ""
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""

def latestnews():
    api_key = "b7c4f75b5fe648d6b93d5d41fec58d44"
    api_dict = {
        "headlines": f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}",
        "business": f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={api_key}",
        "sports": f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={api_key}",
        "entertainment": f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={api_key}",
        "weather": f"https://newsapi.org/v2/top-headlines?country=in&category=weather&apiKey={api_key}",
        "technology": f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={api_key}"
    }

    content = None
    url = None
    speak("Which field news do you want, headlines, business, sports, entertainment, weather, or technology?")
    field = speechrecognition()
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("URL was found")
            break
        else:
            url = True
    if url is True:
        print("URL not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    articles = news["articles"]
    for article_data in articles:
        article_title = article_data["title"]
        print(article_title)
        speak(article_title)
        news_url = article_data["url"]
        print(f"For more info visit: {news_url}")

        speak("Do you want to continue or stop?")
        choice = speechrecognition()
        if "stop" in choice.lower():
            break
        
    speak("That's all")

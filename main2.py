from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pyttsx3
import speech_recognition as sr
from bs4 import BeautifulSoup
import datetime
import requests
import os
from datetime import datetime
import speedtest
from plyer import notification
import pyautogui
import mixer
from GreetMe import greetMe  
from SearchNow import searchGoogle, searchYoutube, searchWikipedia
from Dictapp import closeappweb, openappweb
from NewsRead import latestnews
from Whatsapp import sendMessage
import time
from chat import mains
pyttsx3.init()
pyautogui.FAILSAFE = False
from chat import mains
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
        
if __name__ == "__main__":
    greetMe()
    
    while True:
        query = speechrecognition().lower()
        print("Recognized Query:", query)  
        if "go to sleep" in query:
            speak("Ok , you can call me anytime.")
            break
        elif "sai" in query:
            speak("Yes i am here")
        elif "hello" in query:
            speak("Hello, how are you ?")
        elif "google" in query:
            searchGoogle(query)
        elif "youtube" in query:
            searchYoutube(query)
        elif "wikipedia" in query:
            searchWikipedia(query)
        elif "temperature" in query or "weather" in query:
            search = query
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
        elif "artificial intelligence" in query:
            speak("opening GPT")
            mains()
        elif "the time" in query:
            strTime = datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
        elif "finally sleep" in query:
            speak("Going to sleep")
            exit()
        elif "open" in query:
            openappweb(query)
        elif "close" in query:
            closeappweb(query)
        elif "pause" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")
        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down")
            volumedown()
        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("sai","")
            speak("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())
        elif "news" in query:
            latestnews()
        elif "whatsapp" in query:
            sendMessage()
        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            speak("Do you wish to shutdown your computer? (yes or no)")
            query=speechrecognition().lower()
            shutdown = query
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break
        elif "schedule my day" in query:
            tasks = []
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = speechrecognition().lower()
            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "show my schedule" in query:
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                mixer.init()
                mixer.music.load("notification.mp3")
                mixer.music.play()
                notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                )
        elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")
        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("screenshot.png")
            print("Screenshot saved successfully.")
        elif "Thankyou" in query:
            speak("Its Okay")
        elif "exit" in query:
            exit()
        
            
        
        
        


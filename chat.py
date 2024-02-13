from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyttsx3
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
# Path to Microsoft Edge WebDriver executable
edge_driver_path = 'msedgedriver.exe'

# Path to store cookies and credentials
cookies_file = 'cookies.pkl'
credentials_file = 'credentials.pkl'

def read_chat_number():
    try:
        with open("chatNumber.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

# Function to write the previous conversation ID for reference
def write_chat_number(chat_number):
    with open("chatNumber.txt", "w") as file:
        file.write(str(chat_number))

def pop_remover(driver):
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/button"))
    )
    send_button.click()
    sleep(1)
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/button"))
    )
    send_button.click()
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div[1]/div[1]/div[2]/button[1]"))
    )
    send_button.click()

# Function to interact with ChatGPT
def chat_with_gpt(driver, query):
    try:
        sleep(2)
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea"))
        )
        input_element.send_keys(query)
        sleep(2)
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button"))
        )
        send_button.click()
        sleep(10)
        
        response_element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div"))
        )

        return response_element.text

    except Exception as e:
        print(f"Error: {e}")
        return None

# Main function for executing the chat with GPT
def mains():
    try:
        # Instantiate the Edge WebDriver in headless mode
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--inspect-brk=9222')
        edge_options.use_chromium = True
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--log-level=3')
        driver = webdriver.Edge(options=edge_options)
        driver.maximize_window()
        sleep(10)
        
        # Navigate to the chat link
        driver.get("https://pi.ai/talk")
        # Minimize the browser window
        pop_remover(driver)
       
        chat_number = read_chat_number()

        # Main interaction loop
        while True:
            print("You: ")
            speak("How can i help you")
            query = speechrecognition()
            print(query)
            if "exit" in query:
                driver.quit()
            if query=="":
                query=speechrecognition()
            response = chat_with_gpt(driver, query)
            if response:
                print("GPT-4:", response)
                speak(response)
                chat_number += 1
                write_chat_number(chat_number)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser window after execution
        driver.quit()

# Execute the main function
if __name__ == "__main__":
    mains()

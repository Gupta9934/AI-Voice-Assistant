# Joke function

import pyttsx3 as pyt
import datetime
import SpeechRecognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import pyaudio

engine = pyt.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current Date is ")
    speak(date)
    speak(month)
    speak(year)


def wish():
    speak("Welcome back Sir!!")

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning ")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("Jarvis at your service. How can i help you today ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1  # wait for 1 sec before it start listening
        audio = r.listen(source)  # it can access the microphone

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, 'en=IN')
        print(query)

    except Exception as e:
        print(e)
        speak("unable to recognize your voice, Please Say that again.... ")

        return "None"

    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "123test")
    server.sendmail("test@gmail.com", to, content)
    server.close()


def screenshot():  # defining screenshot function
    img = pyautogui.screenshot()  # specifying the folder to save the screenshots
    # img.save("E:\Udemy")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_jokes())


if __name__ == "__main__":

    wish()

    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching.....")
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I say")
                content = takecommand()
                to = "saiyam9934gupta@gmail.com"
                # sendemail(to,content)
                speak("Email successfully sent")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search in chrome" in query:
            speak("What should I search")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play song" in query:
            songs_dir = "F:\musics\music"  # adding music directory path
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))


        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()  # for storing the said thing in text file

        elif "do you know anything" in query:
            remember = open("data.txt", "r")  # for reading the txts stored in txt file
            speak("you said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!!")


        elif " cpu" in query:
            cpu()

        elif "jokes" in query:
            jokes()

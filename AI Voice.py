import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
r = sr.Recognizer()


# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen for and recognize speech
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None


# Main loop
while True:
    # Listen for speech
    text = listen()

    # If speech was recognized, process the command
    if text:
        if "hello" in text.lower():
            speak("Hello there!")
        elif "what is your name" in text.lower():
            speak("My name is Jarvis.")
        elif "goodbye" in text.lower():
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

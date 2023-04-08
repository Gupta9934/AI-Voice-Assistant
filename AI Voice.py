import speech_recognition as sr
import pyttsx3
import PySimpleGUI as sg

# initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define the layout for the PySimpleGUI window
layout = [
    [sg.Text("Speak to me:")],
    [sg.Input(key="-INPUT-")],
    [sg.Button("Speak"), sg.Button("Exit")]
]

# create the PySimpleGUI window
window = sg.Window("AI Chatbot", layout)

# start the main event loop for the window
while True:
    event, values = window.read()

    # exit if the user closes the window or clicks the Exit button
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    # use speech recognition to transcribe the user's input
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio)
            window["-INPUT-"].update(user_input)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            continue

    # AI's response based on user's input
    if "hello" in user_input.lower():
        speak("Hi there!")
    elif "how are you" in user_input.lower():
        speak("I'm doing well, thanks for asking!")
    elif "goodbye" in user_input.lower():
        speak("Goodbye!")
        break
    else:
        speak("I'm sorry, I don't understand. Can you please rephrase your question?")

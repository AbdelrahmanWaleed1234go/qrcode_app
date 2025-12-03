from streamlit import *
import pyttsx3

en=pyttsx3.init()

write("Welcome in text to speech app")

t=text_input("Enter your text")

if button("genrate"):
    en.say(t)

    en.runAndWait()
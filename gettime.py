import time
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)    # speed of speech
engine.setProperty('volume', 0.7)  # volume of speech

now = datetime.now()

current_time = now.strftime("%H:%M")

def get_time():
    engine.say("The time is" + current_time)
    engine.runAndWait()

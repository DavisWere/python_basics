import pyttsx3
import datetime

engine = pyttsx3.init()
engine.say("the time is: "  + str(datetime.datetime.now()))
engine.setProperty('rate',200) # Speed of the audio (default=150)
engine.say('hello , ')
engine.say(input("enter your name: "))
engine.runAndWait()


import pyttsx3

engine = pyttsx3.init()
engine.say("good morning")
engine.say('hello victor, davis, were, enda numerical')
engine.say(input("enter your name: "))
engine.runAndWait()


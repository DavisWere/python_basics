import pyttsx3

def get_engine():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 200)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Get available voices
    voices = engine.getProperty('voices')

    # Select a female voice (if available)
    female_voice = None
    for voice in voices:
        if 'female' in voice.name.lower():
            female_voice = voice.id
            break

    if female_voice:
        engine.setProperty('voice', female_voice)
    else:
        print("Female voice not found, using default voice.")

    return engine

def speak_text(text):
    engine = get_engine()
    engine.say(text)
    engine.runAndWait()

def main():
    speak_text("Good morning!")
    speak_text("Hello Victor, Davis, were, Enda numerical")
    
    # Ask for user input and speak it
    name = input("Enter your name: ")
    speak_text(f"Hello {name}, welcome!")

    # Additional functionality
    speak_text("I can speak in different voices and adjust speech rate. What else would you like me to say?")
    custom_text = input("Enter text for speech: ")
    speak_text(custom_text)

if __name__ == "__main__":
    main()

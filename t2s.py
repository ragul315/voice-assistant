import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def speek(text):
      
    engine.say(text)
    engine.runAndWait()
    print(text)

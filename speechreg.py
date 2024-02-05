import speech_recognition as sr
from t2s import speek

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        speek("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        speek(f"Could not request results from Google Speech Recognition service; {e}")
        return None



import speech_recognition as sr
from resforwd import respond
from t2s import speek

def spreg():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)  # Adjust the timeout value as needed
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            print("Nova:", speek(respond(text)))
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Speech recognition request failed: {e}")



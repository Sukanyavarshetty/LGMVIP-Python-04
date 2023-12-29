import speech_recognition as sr
import pyttsx3
import webbrowser
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def assistant():
    speak("Hello! I'm your voice assistant. How can I help you?")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Processing...")
                command = recognizer.recognize_google(audio).lower()
                if "hello" in command:
                    speak("Hello there!")
                elif "how are you" in command:
                    speak("I'm doing great, thank you for asking!")
                elif "tell me a joke" in command:
                    speak("Why don't scientists trust atoms? Because they make up everything!")
                elif "what's the weather" in command:
                    speak("I'm sorry, I cannot provide the weather information right now.")
                elif "open website" in command:
                    speak("Opening a website for you.")
                    webbrowser.open("https://github.com/Sukanyavarshetty")
                elif "thank you" in command or "thanks" in command:
                    speak("You're welcome!")
                elif "exit" in command:
                    speak("Goodbye!")
                    break
                else:
                    speak("I'm sorry, I didn't catch that. Can you please repeat?")

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said. Can you please repeat?")
        except sr.RequestError:
            speak("Sorry, I'm having trouble processing your request. Please try again later.")

if __name__ == "__main__":
    assistant()

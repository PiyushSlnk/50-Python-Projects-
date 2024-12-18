import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio input and recognize speech."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        except Exception as e:
            print(e)
        return ""

def handle_command(command):
    """Handle recognized voice commands."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    elif "open browser" in command:
        speak("Opening browser.")
        webbrowser.open("http://google.com")
    elif "play music" in command:
        speak("Playing music.")
        music_dir = "C:\\Users\\YourUsername\\Music"  # Change to your music directory
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I can't do that yet.")

# Main loop
if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        user_command = listen()
        if user_command:
            handle_command(user_command)

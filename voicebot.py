import speech_recognition as sr
import subprocess
import pyttsx3

print("Ask ChatBOT anything by Voice. Press Ctrl+C to exit.")

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording User Response... ")
        audio = recognizer.listen(source, timeout=10)
        print("Recording complete. Processing Response")
    return audio

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not request results"

def run_chatbot_script(user_input):
    # Run the chatbot script and capture the output
    result = subprocess.run(['python', 'chatbot.py', user_input], capture_output=True, text=True)
    return result.stdout.strip()

def speak_text(text):
    # Convert text to speech and play it
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    while True:
        try:
            audio = record_audio()
            user_input = transcribe_audio(audio)
            print(f"You: {user_input}")
            response = run_chatbot_script(user_input)
            print(f"ChatBOT: {response}")
            speak_text(response)
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

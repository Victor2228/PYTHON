import speech_recognition
import pyttsx3 as tts
from neuralintents import GenericAssistant

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)


def hello():
    speaker.say("hello sir")
    speaker.runAndWait()


def exit1():
    speaker.say("bye sir")
    speaker.runAndWait()


mappings = {
    "greeting": hello,
    "exit": exit1
}
assistant = GenericAssistant('VOIE_CHAT.json', intent_methods=mappings)
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            message = message.lower()
        assistant.request(message)
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()

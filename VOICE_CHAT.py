import speech_recognition
import pyttsx3 as tts

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            speaker.say(f"{text}")
            speaker.runAndWait()
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        speaker.say("I did not understand you")
        speaker.runAndWait()

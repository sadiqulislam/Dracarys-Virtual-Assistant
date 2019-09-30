import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,Presence")
    elif hour>=12 and hour<16:
        speak("Good Noon,Presence")
    elif 
if __name__ == '__main__':
    speak("I am Dracrys And I Served Presence")
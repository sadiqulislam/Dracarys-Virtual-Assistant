import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,Presence")
    elif hour>=12 and hour<16:
        speak("Good Noon,Presence")
    elif hour>=16 and hour<19:
        speak("Good Afternoon,Presence")
    else:
        speak("Good Night,Presence")
    speak("I Am Dracarys,Sir! What may I Do Now,Sir?")


def takeCommand():
    #It Takes Command From Me Through Microphone and Returns My Speech As A Strings Output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....!")
        query = r.recognize_google(audio,language="en-US")
        print(f"User Said:{query}\n")


    except Exception as e:
        #print(e)

        print("Say That Again,Sir,Please!")
        return "None"
    return query







if __name__ == '__main__':
    #speak("I am Dracarys And I Served Presence")
    wishme()
    while True:
        query =takeCommand().lower()


        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("According To Wikipedia")
            speak(results)
        
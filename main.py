# basic AI project

"""
 speechrecognition pyaudio
 setuptools
 webbrowser
 pyttsx3
 pocketsphinx

"""
# new venv banavine first uuper na module install karva (pip install (module name))

import speech_recognition as sr
import webbrowser
import pyttsx3
import wp

recognition = sr.Recognizer()
engine = pyttsx3.init()

# speak j bolvanu hoy te mate 
def speak(text):
    engine.say(text)
    engine.runAndWait()

# j AI ni use thi sarech karvanu hoy te mate nu function chy aa
def process(c):
    print(c)
    if c.lower().startswith("open"):
      website = c.lower().split(" ")[1]
      link = wp.wb[website]
      webbrowser.open(link)   

    elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = wp.wb[song]
      webbrowser.open(link)      


# main work ahiya thi start thai chy
if __name__ == "__main__":
    speak("kya seva kru me aapki")
    while True:
            r = sr.Recognizer()
            print("recognizing.....")
            try:
                with sr.Microphone() as scoure:
                    print("listening....")
                    audio = r.listen(scoure,timeout=3,phrase_time_limit=2)
                word = r.recognize_google(audio)
                print(word)
                if word.lower() == "hello":
                    speak("bol bhai") 
                    with sr.Microphone() as socure:
                        print("sunn raha hu !!")
                        audio = r.listen(scoure,timeout=3,phrase_time_limit=2)  
                        command = r.recognize_google(audio)  
                        process(command)
            except Exception as e:
                print("Kutch to gadbad haiii bhai")            



import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)

voices =engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def  wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("This is David! Please tell me how may I help you")



def  takeCommand():
    #it takes microfone intput from user 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #  print(e)
        print("Say that again please...")
        return "None"

    return query



if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
    #logic for executing based on query
        if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query =query.replace("wekipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)

        elif 'play music' in query:
            music_dr="C:\\Users\\vidhi\\OneDrive\\Desktop\\songs"
            songs=os.listdir(music_dr)
            os.startfile(os.path.join(music_dr,songs[1]))

        elif 'search in chrome' in query:
            speak("what should I search?")    
            chromepath="C:\Program Files\Google\\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")





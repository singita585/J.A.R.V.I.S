#import needed for JARVIS find the word you are looking for
import difflib import get_close_matches
import pyttsx3
import json
import speech_recognition as sr 

data = json.oad(open("data.json"))
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#JARVIS WILL LISTEN TO YOUR COMMAND AND RESPOND TO YOU
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration = 1.5)
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query 

#JARVIS WILL MAKE SURE IF HE HEARD YOU
def translate(word):
    word = word.lower()
    if word in data:
        speak(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        speak("Did you mean " + X +
              " instead, respond with Yes or No.")
        ans = takeCommand().lower()
        if "yes" in ans:
            speak(data[x])
        elif "no" in ans:
            speak("Word doesn't exist. Please make sure you spelled it correctly.")
        else:
            #changed from we to I
            speak("I did not understand your entry.")
    
    else:
        speak("Word doesn't exist. Please double check it.")

if __name__ == "__main__":
    translate()
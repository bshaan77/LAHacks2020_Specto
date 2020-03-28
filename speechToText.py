import speech_recognition as sr                                                    
r = sr.Recognizer()
import database
import sys
import datetime

def start():
    print("Welcome to Specto")
    print("If at any time you would like to leave, respond \"leave\"")
##    status = input()
##    status = status.lower()
##    if status.startswith(l):
##        leave()
    while True:
        currentDT = datetime.datetime.now()
        currentDT = str(currentDT)
        print(currentDT)
        with sr.Microphone() as source:                                                                       
            print("Speak now")                                                                                   
            audio = r.listen(source)   
        try:
            print("You said " + r.recognize_google(audio))
            database.insert('speechToText.txt', currentDT, r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Not understandable")

def leave():
    print("We hoped that this has worked for you")
    exit()

while True:
    start()

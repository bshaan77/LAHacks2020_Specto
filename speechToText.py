import speech_recognition as sr                                                    
r = sr.Recognizer()
import database
import sys
import datetime

def start():
    print("Respond New to enter into a new document, or  Respond Find to look up a previous conversation.")
    userstatus = input()
    userstatus = userstatus.lower()
    if userstatus.stratswith(n):
        print("Great! Lets start a new conversation")
        print('Can I get your name')
        name = input()
        print(name + " What would you like to call the conversation")
        convoName = input()
        convoName = str(convoName)
        convoName = (convoName + ".txt")
    elif userstatus.startswith(f):
        print("Great! Lets find the conversation")
        print('Can I get your name')
        name = input()
        print(name + " What is the name of the conversation we are trying to find")
        convoName = input()
        convoName = str(convoName)
        convoName = (convoName + ".txt")
    else:
        print("You didn't enter a valid response. Lets try that again")
        
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
    print("Welcome to Specto")
    start()

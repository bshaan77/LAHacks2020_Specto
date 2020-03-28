with sr.Microphone() as source:                                                                       
    print("Speak now")                                                                                   
    audio = r.listen(source)   

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:

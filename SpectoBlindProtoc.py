import time
import os
import RPi.GPIO as GPIO
from gtts import gTTS 
from pygame import mixer
import pytesseract
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import speech_recognition as sr
from picamera import PiCamera

mixer.init()
r = sr.Recognizer()
camera = PiCamera()


with sr.Microphone() as source:
        print('Speak:')
        audio = r.listen(source)

att = r.recognize_google(audio)

if att == "take picture" or "take a picture":
        camera.capture('picture.jpg')
        img = mpimg.imread('download-1.jpg')
        text = pytesseract.image_to_string(img)
        print(text)

GPIO.setmode(GPIO.BCM)

#Green Wire
GPIO.setup(14,GPIO.IN)
#GPIO.PWM(14,160)
t = gTTS(text="t")
t.save("object.mp3")
#setup over
while True:
        sensor = GPIO.input(14)
        if sensor == 0:
                alert = mixer.Sound("object.mp3")
                alert.play()            
                print("Object Detected")
                print('hi')  


# Audio To Text
 
## Motivation

Today, the technology exists as a support for all people, it has helped make our traffic signals work, allow us to use the internet, and even goes as far as powering our toaster at home. Our inspiration was the supporting role that technology plays in society today. With this project, we plan to expand that support to help a new category of people.

## What it does

The project has 2 protocols, the blind protocol which is able to help the visually impaired user with visualizing the world around him through his other senses. The user at any time could ask Specto to take a picture. Specto could take a picture and will tell the user all the objects in the area and if there is any text in front of a user, like a book. It would read out the text for the user. Specto also has the ability to alert the user if there is a wall or object in front of the user, to guide the user through the world. Specto's deaf protocol is a web app that is able to detect any audio in the real world and turn it into text for the user to understand. The user could type back and it would turn in to audio for the other person to understand. These two protocols help support both blind and deaf people through their everyday life.

## How it works
This project has multiple parts and was split up by each of the members in our team. We built the blind protocol using infrared sensors to tell the user when there is an object in front of them. The computing for the blind protocol happens inside the raspberry pi. We used the Pi Camera so when we asked Specto to take a picture it would take it. And the image to text algorithm and the detect multiple objects program would run to insight the user on what is in front of him or her. For the detect multiple objects program we used the Google vision API to make it work, and for the image, to text we used a python library known as pytesseract. To take a picture the user says "Specto take a picture" which could be detected using the speech recognition library. For the deaf protocol, we used the speech recognition library again to help deaf people communicate with someone else. The speech recognition detects the other person's voice and turns it into text for the other person to understand.  The deaf person could speak back by typing on the web app and using gTTS we turn that text into speech.


## Installation
### Blind Protocol

Install all the dependencies on Terminal
Pip install playsound
Pip install SpeechRecognition
Pip install gTTS
Pip install pytesseract
Pip install tensorflow-gpu
Run the specto blind protocol code

### Google Vision API (Part of blind protocol)

Install JSON file for Google Vision API
Download
Find Service key
Using the service key enable Google vision API 
import it in your code and use Detect multiple objects code

### Deaf Protocol

Info can be found here https://pypi.org/project/SpeechRecognition/
Install the following
pip install SpeechRecognition
pip install pyaudio *PyAudio to use the microphone input


## Acknowledgments
Zhang, A. (2017). Speech Recognition (Version 3.8) [Software]. Available from https://github.com/Uberi/speech_recognition#readme. 

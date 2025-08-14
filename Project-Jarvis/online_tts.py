import gtts 
from playsound import playsound
from speechrecognition 
tts = gtts.gTTS("Hello World")

tts.save("hello.mp3")

playsound("hello.mp3")
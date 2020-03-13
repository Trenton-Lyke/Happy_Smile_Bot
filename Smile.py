import datetime
import json
import numpy as np
import cv2
import pygame, time
import requests
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
from gpiozero import LED
import tweepy
import random
import urllib

def textToSpeech(text,language,isSlow):

  

  
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    textToSpeechEngine = gTTS(text=text, lang=language, slow=isSlow) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    sf = TemporaryFile()
    textToSpeechEngine.write_to_fp(sf)
    sf.seek(0)
    mixer.music.load(sf)

    ##os.system("start welcome.mp3")
    
    
    mixer.music.play()
    

    while not pygame.mixer.music.get_pos() == -1:
        pass

led = LED(18)
mixer.init()
led.on()
textToSpeech("Yay I am smiling",'en',False)
time.sleep(60)

